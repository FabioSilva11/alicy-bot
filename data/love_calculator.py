import json
import random

def calculadora_do_amor(lista_usuarios):
    # Verificar se há pelo menos dois usuários na lista
    if len(lista_usuarios) < 2:
        return "Desculpe, não há usuários suficientes para calcular a compatibilidade."
    
    # Converter o dicionário em uma lista de usuários
    usuarios = list(lista_usuarios.values())
    
    # Escolher aleatoriamente dois usuários da lista
    usuario1, usuario2 = random.sample(usuarios, 2)
    
    # Obter os nomes dos usuários escolhidos
    nome_usuario1 = usuario1['nome']
    nome_usuario2 = usuario2['nome']
    
    # Calcular a compatibilidade com base nos nomes fornecidos
    compatibilidade = sum(ord(char.lower()) for char in nome_usuario1) + sum(ord(char.lower()) for char in nome_usuario2)
    
    # Normalizar a compatibilidade para um valor entre 0 e 100
    compatibilidade = (compatibilidade % 100) + 1

    # Dividir a faixa de porcentagem em 4 intervalos
    if compatibilidade <= 25:
        mensagem = mensagem_amor_baixo(nome_usuario1, nome_usuario2, compatibilidade)
    elif compatibilidade <= 50:
        mensagem = mensagem_amor_medio(nome_usuario1, nome_usuario2, compatibilidade)
    elif compatibilidade <= 75:
        mensagem = mensagem_amor_alto(nome_usuario1, nome_usuario2, compatibilidade)
    else:
        mensagem = mensagem_convite_festa(nome_usuario1, nome_usuario2)
    
    return mensagem

# Mensagens para diferentes resultados de amor
def mensagem_amor_baixo(usuario1_nome, usuario2_nome, amor):
    mensagem = f"{usuario1_nome} e {usuario2_nome} parecem ser mais amigos do que um casal. O amor entre eles é de {amor}%! 👫"
    return mensagem

def mensagem_amor_medio(usuario1_nome, usuario2_nome, amor):
    mensagem = f"{usuario1_nome} e {usuario2_nome} estão se estranhando um pouco, mas quem sabe dá certo. O amor entre eles é de {amor}%! 🤔"
    return mensagem

def mensagem_amor_alto(usuario1_nome, usuario2_nome, amor):
    mensagem = f"🎉 Parabéns! 🎉\n\n{usuario1_nome} e {usuario2_nome} estão realmente apaixonados! O amor entre eles é de {amor}%! 💖"
    return mensagem

def mensagem_convite_festa(usuario1_nome, usuario2_nome):
    mensagem = f"Ei, {usuario1_nome} e {usuario2_nome}, não se esqueçam de me convidar para a festa! 🎉🎈"
    return mensagem
