import telebot
from data.dados_gerador import gerar_cpf, gerar_cc
from data.mensagens import welcome_message, regras_message, manual_message
from data.love_calculator import calculadora_do_amor
from data.pesquisa_de_dado import get_user_info_username, get_user_info_id
from data.asalto import executar_roubo_com_sucesso, executar_roubo_com_falha, comparar_saldos, executar_roubo_com_sucesso2, executar_roubo_com_falha2
from data.free_api import nasa, pokemon_data, get_type_emojis
from data.adicional import load_users, adicionar_usuario , formatar_horarios
from data.reload_game import update_users_data
import random
import re
import json


# Inicializa o bot com seu token
bot = telebot.TeleBot("6397278735:AAErtF9rERXZCS1Gxd-Reo1Zkx_7lZqrcWw")

fortunes = {
    "🐯FORTUNE TIGER🐯": [],
    "🐮FORTUNE OX🐮": [],
    "🐭FORTUNE MOUSE🐭": [],
    "🐘GANESHA FORTUNE🐘": [],
    "🐰FORTUNE RABBIT🐰": [],
    "👫DOUBLE FORTUNE👫": [],
    "🤠WILD BANDITO🤠": [],
    "🥊MUAI THAY🥊": [],
    "🐒JUNGLE MADAGASCAR🐒": [],
    "🧞GENIES WISHES🧞": [],
    "🐘🥇GANESHA GOLD🥇🐘": [],
    "🍹COCKTAIL🍹": [],
    "⚔️NINJA vs SAMURAY⚔️": []
}

# Link para incluir após cada horário
link = "https://t.me/+4W9E1HsJ_N5mOWIx"

# Gerar horários aleatórios
for fortune in fortunes:
    for _ in range(15):
        minute = str(random.randint(0, 59)).zfill(2)
        time = f"13:{minute}"
        fortunes[fortune].append(time) 

# Função para enviar os horários
@bot.message_handler(commands=['bets'])
def enviar_horarios(message):
    chat_id = message.chat.id
    for fortuna, lista_horarios in fortunes.items():
        horarios_formatados = formatar_horarios(lista_horarios)
        mensagem = f"{fortuna}\n{horarios_formatados}\n"
        bot.send_message(chat_id=chat_id, text=mensagem + link)

@bot.message_handler(content_types=['new_chat_members'])
def welcome_message_handler(message):
    new_members = message.new_chat_members
    for member in new_members:
        user_id = member.id
        first_name = member.first_name
        last_name = member.last_name 
        username = member.username
        resposta = welcome_message()
        regra = regras_message()
        manual = manual_message()
        welcome_text = f"Bem-vindo, {first_name}!, 🎉.\n\n{resposta}\n\n {manual_message}"
        bot.reply_to(message, welcome_text)
        bot.reply_to(message, regra)


@bot.message_handler(commands=['comandos'])
def status_command(message):
    user_id = str(message.from_user.id)
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:
        manual = manual_message()
        bot.reply_to(message, manual)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)


@bot.message_handler(commands=['updat'])
def update_command(message):
    user_id = str(message.from_user.id)
    if user_id == "6550987404":
        bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
        update_users_data()

       

@bot.message_handler(commands=['pokemon'])                     
def send_random_pokemon_info(message):
    user_id = str(message.from_user.id)
    users = load_users()
    if user_id in users:
        pokemon_info = pokemon_data()  # Renomeando a variável para evitar conflito de nomes

        if pokemon_info:  # Renomeando para evitar conflito de nomes
            # Monta a mensagem informativa com emojis
            info_text = f"<b>Nome:</b> {pokemon_info['Nome']}\n"
            info_text += f"<b>ID:</b> {pokemon_info['ID']}\n"
            info_text += f"<b>Altura:</b> {pokemon_info['Altura']} decímetros\n"
            info_text += f"<b>Peso:</b> {pokemon_info['Peso']} hectogramas\n"
            info_text += f"<b>Tipos:</b> {' '.join(get_type_emojis(pokemon_info['Tipos']))} {' '.join(pokemon_info['Tipos'])}\n"
            info_text += f"💬 <b>Descrição:</b> {pokemon_info['Descrição']}"

            # Envia a mensagem com as informações e a imagem do Pokémon
            bot.send_photo(message.chat.id, pokemon_info['Imagem'], caption=info_text, parse_mode='HTML')
        else:
            bot.reply_to(message, "Desculpe, não foi possível obter informações sobre um Pokémon aleatório no momento.")
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)

@bot.message_handler(commands=['status'])
def status_command(message):
    user_id = str(message.from_user.id)
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:
        usuario = users[user_id]
        # Extrair informações do usuário
        nome = usuario["nome"]
        username = usuario["username"]
        saldo = str(usuario["saldo"])
        escudo = str(usuario["escudo"])
        roubos = str(usuario["roubos"])
        # Formatando as informações em um texto
        resposta = (
            f"👋 Olá, {nome}! Aqui estão algumas informações sobre você:\n"
            f"👤 Nome: {nome}\n"
            f"📱 Username: @{username}\n"
            f"💰 Saldo: {saldo} unidades\n"
            f"🛡️ Escudo: {escudo}\n"
            f"🔫 Roubos realizados: {roubos}\n"
        )
        bot.reply_to(message, resposta)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)
        
   
@bot.message_handler(commands=['top10'])
def top10_command(message):
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    
    user_id = message.from_user.id  # Obtendo o ID do usuário
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:
            top_users = sorted(users.values(), key=lambda x: x.get("saldo", 0), reverse=True)[:10]
            resposta = "🏆 Top 10 Usuários:\n"
            for i, usuario in enumerate(top_users, start=1):
                resposta += f"{i}. {usuario.get('nome', 'Nome Desconhecido')} - Saldo: {usuario.get('saldo', 0)} unidades\n"
            bot.reply_to(message, resposta)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)

        
# Função para lidar com o comando /nasaday
@bot.message_handler(commands=['nasaday'])
def meme_command(message):
    user_id = str(message.from_user.id)
    users = load_users() 
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:
        try:
            dados = nasa()

            # Construir a mensagem a ser enviada para o Telegram
            mensagem = f"Olá {message.from_user.first_name}, aqui está a Imagem Astronômica do Dia (APOD):\n\n"
            mensagem += f"Data: {dados['date']}\n\nTítulo: {dados['title']}\n\nExplicação: {dados['explanation']}\n\n"
            mensagem += f"URL da imagem: {dados['url']}\n\nURL em alta resolução: {dados['hdurl']}"

            bot.send_message(message.chat.id, mensagem)  # Enviando a mensagem correta
            print("Mensagem enviada com sucesso para o Telegram.")
        except Exception as e:
            print("Erro ao enviar mensagem para o Telegram:", e)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)


# Função para lidar com o comando /gerarcpf
@bot.message_handler(commands=['gerarcpf'])
def gerar_cpf_command(message):
    user_id = message.from_user.id 
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:
        resposta = gerar_cpf()
        bot.reply_to(message, resposta)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)

# Função para lidar com o comando /gerarcc
@bot.message_handler(commands=['gerarcc'])
def gerar_cc_command(message):
    user_id = message.from_user.id 
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:  
        resposta = gerar_cc()
        bot.reply_to(message, resposta)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)

# Função para lidar com o comando /status
@bot.message_handler(commands=['status'])
def status_command(message):
    user_id = message.from_user.id 
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:  
        resposta = welcome_message()
        bot.reply_to(message, resposta)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)

# Função para lidar com o comando /regras
@bot.message_handler(commands=['regras'])
def regras_command(message):
    user_id = message.from_user.id 
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:  
        resposta = regras_message()
        bot.reply_to(message, resposta)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)

# Função para lidar com o comando /love
@bot.message_handler(commands=['love'])
def love_command(message):
    user_id = message.from_user.id 
    users = load_users()
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:  
        resposta = calculadora_do_amor(load_users())
        bot.reply_to(message, resposta)
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)


@bot.message_handler(commands=['roubar'])
def roubar_command(message):
    user_id = message.from_user.id 
    users = load_users()
    mentioned_user_match = re.search(r'@(\w+)', message.text)
    bot.send_chat_action(message.chat.id, 'typing')  # Indicando que o bot está digitando
    if str(user_id) in users:  
        if mentioned_user_match:
            mentioned_user = mentioned_user_match.group(1)
            attacker_id, attacker_nome, attacker_roubos, attacker_escudo, attacker_saldo = get_user_info_id(str(user_id), users)
            mentioned_id, mentioned_nome, mentioned_roubos, mentioned_escudo, mentioned_saldo = get_user_info_username(mentioned_user, users)
            chance = random.random()
            # Verifica se alguma informação do usuário mencionado não foi encontrada
            if mentioned_id is None or mentioned_nome is None or mentioned_roubos is None or mentioned_escudo is None or mentioned_saldo is None:
                bot.reply_to(message, "Desculpe, o usuário mencionado não está na lista de permissão.")
            else:
                if attacker_roubos > 0 and attacker_saldo > 0 and mentioned_saldo > 0: 
                    if mentioned_escudo > 0:
                        if chance > 0.5:  # 50% de chance de sucesso de roubo
                            valor_roubo = comparar_saldos(attacker_saldo, mentioned_saldo)
                            valor = executar_roubo_com_sucesso(attacker_roubos, attacker_id, attacker_saldo, mentioned_saldo, mentioned_id, mentioned_escudo, valor_roubo, users)
                            bot.reply_to(message, f"Parabéns,{mentioned_nome} estava com escudo e você conseguiu quebrar  conseguindo roubar {valor} moedas! Que grande feito!")
                        else:  # 50% de chance de falha no roubo e perder o que deveria ganhar
                            valor_roubo = comparar_saldos(attacker_saldo, mentioned_saldo)
                            valor = executar_roubo_com_falha(attacker_roubos, attacker_id, attacker_saldo, mentioned_saldo, mentioned_id, mentioned_escudo, valor_roubo, users)       
                            bot.reply_to(message, f"Infelizmente, apesar de quebrar o escudo, você não conseguiu roubar com sucesso e perdeu {valor} moedas para {mentioned_nome}")                  
                    else:
                        if chance > 0.5:  # 50% de chance de sucesso de roubo
                            valor_roubo = comparar_saldos(attacker_saldo, mentioned_saldo)
                            valor = executar_roubo_com_sucesso2(attacker_roubos, attacker_id, attacker_saldo, mentioned_saldo, mentioned_id, mentioned_escudo, valor_roubo, users)
                            bot.reply_to(message, f"Parabéns,{mentioned_nome} estava sem escudo e conseguiu roubar {valor} moedas! Que grande feito!")
                        else:  # 50% de chance de falha no roubo e perder o que deveria ganhar
                            valor_roubo = comparar_saldos(attacker_saldo, mentioned_saldo)
                            valor = executar_roubo_com_falha2(attacker_roubos, attacker_id, attacker_saldo, mentioned_saldo, mentioned_id, mentioned_escudo, valor_roubo, users)
                            bot.reply_to(message, f"Infelizmente, apesar de o usuário não ter o escudo, você não conseguiu roubar com sucesso e perdeu {valor} moedas para {mentioned_nome}")
                else:
                    bot.reply_to(message, f"{attacker_nome} não possui qualificações nessesarias para uma tentaiva de roubo, tente novamente amanhã.")
        else:
            bot.reply_to(message, "Por favor, mencione o usuário que deseja roubar.")
    else:
        adicionar_usuario(users, user_id, message.from_user.first_name, message.from_user.username, message)



# Inicia o bot
bot.polling()


