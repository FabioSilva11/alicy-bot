import requests
import random


# Função para obter os detalhes do Astronomy Picture of the Day da API da NASA
def nasa():
    try:
        response = requests.get("https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY")
        if response.status_code == 200:
            data = response.json()
            return {
                "date": data["date"],
                "explanation": data["explanation"],
                "hdurl": data["hdurl"],
                "media_type": data["media_type"],
                "title": data["title"],
                "url": data["url"]
            }
        else:
            return "Desculpe, não foi possível obter os detalhes do Astronomy Picture of the Day. Tente novamente mais tarde."
    except Exception as e:
        print("Erro ao obter os detalhes do Astronomy Picture of the Day:", e)
        return "Ocorreu um erro ao processar sua solicitação. Por favor, tente novamente mais tarde."

# Função para obter emojis correspondentes aos tipos de Pokémon
def get_type_emojis(types):
    emojis = {
        "Normal": "🟦",
        "Fire": "🔥",
        "Water": "💧",
        "Electric": "⚡",
        "Grass": "🌱",
        "Ice": "❄️",
        "Fighting": "🥊",
        "Poison": "☠️",
        "Ground": "⛰️",
        "Flying": "🦅",
        "Psychic": "🔮",
        "Bug": "🐛",
        "Rock": "🪨",
        "Ghost": "👻",
        "Dragon": "🐉",
        "Dark": "🌑",
        "Steel": "⚙️",
        "Fairy": "🧚"
    }
    emojis_list = [emojis.get(type, "") for type in types]
    return emojis_list


# Função para buscar dados de um Pokémon na API
def pokemon_data():
    random_id = random.randint(1, 898)  # Existem 898 Pokémon no total até a geração mais recente
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pokemon_info = {
            "Nome": data['name'].capitalize(),
            "ID": data['id'],
            "Altura": data['height'],
            "Peso": data['weight'],
            "Tipos": [type_data['type']['name'].capitalize() for type_data in data['types']],
            "Imagem": data['sprites']['other']['official-artwork']['front_default']  # URL da imagem do Pokémon em alta qualidade
        }
        species_url = data['species']['url']
        species_response = requests.get(species_url)
        if species_response.status_code == 200:
            species_data = species_response.json()
            pokemon_info["Descrição"] = species_data['flavor_text_entries'][0]['flavor_text'].replace('\n', ' ')
        else:
            pokemon_info["Descrição"] = "Não foi possível obter a descrição do Pokémon."
        return pokemon_info
    else:
        return None