import json

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

# Função para atualizar os dados dos usuários
def update_users_data():
    users_data = load_users()
    for user_id in users_data:
        users_data[user_id]["saldo"] = 100
        users_data[user_id]["escudo"] = 1
        users_data[user_id]["roubos"] = 5
    save_users(users_data)
    return "Dados dos usuários atualizados."