import json
import random

# Função para atualizar os dados do usuário no dicionário de usuários permitidos
def atualizar_dados_usuario(permitidos, id_mencionado, escudo_mencionado, saldo_mencionado, id_atacante, roubos_atacante, saldo_atacante):
    if id_mencionado in permitidos:
        permitidos[id_mencionado]["escudo"] = escudo_mencionado
        permitidos[id_mencionado]["saldo"] = saldo_mencionado
    if id_atacante in permitidos:
        permitidos[id_atacante]["roubos"] = roubos_atacante
        permitidos[id_atacante]["saldo"] = saldo_atacante


    save_users(permitidos)


def comparar_saldos(attacker_saldo, mentioned_saldo):
    if attacker_saldo < mentioned_saldo:
        return random.randint(0, attacker_saldo)
    elif attacker_saldo > mentioned_saldo:
        return random.randint(0, mentioned_saldo)
    else:
        return random.randint(0, attacker_saldo)

def executar_roubo_com_sucesso(roubos_atacante, id_atacante, saldo_atacante, saldo_mencionado, id_mencionado, escudo_mencionado, valor_roubo, permitidos):
    escudo_mencionado -= 1
    roubos_atacante -= 1
    saldo_mencionado -= valor_roubo
    saldo_atacante += valor_roubo
    
    # Chamada da função para atualizar os dados do usuário
    atualizar_dados_usuario(permitidos, id_mencionado, escudo_mencionado, saldo_mencionado, id_atacante, roubos_atacante, saldo_atacante)
    return valor_roubo

def executar_roubo_com_falha(roubos_atacante, id_atacante, saldo_atacante, saldo_mencionado, id_mencionado, escudo_mencionado, valor_roubo, permitidos):
    escudo_mencionado -= 1
    roubos_atacante -= 1
    saldo_mencionado += valor_roubo
    saldo_atacante -= valor_roubo

    # Chamada da função para atualizar os dados do usuário
    atualizar_dados_usuario(permitidos, id_mencionado, escudo_mencionado, saldo_mencionado, id_atacante, roubos_atacante, saldo_atacante)
    return valor_roubo

def executar_roubo_com_sucesso2(roubos_atacante, id_atacante, saldo_atacante, saldo_mencionado, id_mencionado, escudo_mencionado, valor_roubo, permitidos):
    saldo_mencionado -= valor_roubo
    saldo_atacante += valor_roubo
    roubos_atacante -= 1
    
    # Chamada da função para atualizar os dados do usuário
    atualizar_dados_usuario(permitidos, id_mencionado, escudo_mencionado, saldo_mencionado, id_atacante, roubos_atacante, saldo_atacante)
    return valor_roubo

def executar_roubo_com_falha2(roubos_atacante, id_atacante, saldo_atacante, saldo_mencionado, id_mencionado, escudo_mencionado, valor_roubo, permitidos):
    saldo_mencionado += valor_roubo
    saldo_atacante -= valor_roubo
    roubos_atacante -= 1

    # Chamada da função para atualizar os dados do usuário
    atualizar_dados_usuario(permitidos, id_mencionado, escudo_mencionado, saldo_mencionado, id_atacante, roubos_atacante, saldo_atacante)
    return valor_roubo


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
