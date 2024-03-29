import json
import telebot
import random

# Inicializa o bot com seu token
bot = telebot.TeleBot("6397278735:AAErtF9rERXZCS1Gxd-Reo1Zkx_7lZqrcWw")
# Constante para o nome do arquivo de usuários
users_file = "usuarios_permitidos.json"


# Função para carregar os dados dos usuários do arquivo
def load_users():
    try:
        with open(users_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}  # Retorna um dicionário vazio se o arquivo não existir

# Função para salvar os dados dos usuários no arquivo
def save_users(users_data):
    with open(users_file, 'w') as file:
        json.dump(users_data, file)

# Função para adicionar usuário
def adicionar_usuario(loadusers, user_id, first_name, username, message):
    if user_id not in loadusers.values():
        if username:
            loadusers[user_id] = {
                "id": user_id,
                "nome": first_name,
                "username": username,
                "saldo": 100,
                "escudo": 1,
                "roubos": 5
            }
            save_users(loadusers)  # Salva os dados após adicionar o usuário
            bot.reply_to(message, "Você foi adicionado à lista de permissão. Agora você pode usar o comando livremente!")
        else:
            bot.reply_to(message, "Você não tem permissão para usar este comando. Para utilizá-lo, vá até o seu perfil e configure o seu nome de usuário.")
    else:
        bot.reply_to(message, "Você já está na lista de usuários.")


# Função para formatar os horários
def formatar_horarios(horarios):
    formatted_horarios = ""
    for horario in horarios:
        formatted_horarios += f"{horario}, "
    return formatted_horarios.rstrip(", ")  # Remover a vírgula final
