# Função para obter informações do usuário pelo nome de usuário em uma lista fornecida
def get_user_info_username(username, users_data):
    for user_id, user_info in users_data.items():
        if user_info.get('username') == username:
            saldo_roubos = user_info.get('roubos', 0)
            saldo_escudo = user_info.get('escudo', 0)
            saldo_total = user_info.get('saldo', 0)
            nome = user_info.get('nome', '')
            return user_id, nome, saldo_roubos, saldo_escudo, saldo_total
    return None, None, None, None, None  # Se o nome de usuário não for encontrado, retorne None em todas as informações

# Função para obter informações do usuário pelo id do usuário em uma lista fornecida
def get_user_info_id(user_id, users_data):
    user_info = users_data.get(user_id)
    if user_info:
        saldo_roubos = user_info.get('roubos', 0)
        saldo_escudo = user_info.get('escudo', 0)
        saldo_total = user_info.get('saldo', 0)
        nome = user_info.get('nome', '')
        return user_id, nome, saldo_roubos, saldo_escudo, saldo_total
    return None, None, None, None, None  # Se o id do usuário não for encontrado, retorne None em todas as informações
