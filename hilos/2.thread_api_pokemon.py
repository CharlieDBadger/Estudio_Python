import requests
import logging
from threading import Thread

logging.basicConfig(
    level=20,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def get_pokemon_name_by_id(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json().get("forms")[0].get("name")
    else:
        return None


def print_pokemon(pokemon_id):
    poke_name = get_pokemon_name_by_id(pokemon_id)
    logging.info(f'Pokemon: {poke_name}')


print_pokemon(1)

for p in range(1, 100):
    thread = Thread(
        target=print_pokemon(p),
        args=(p,))

    thread.start()
    