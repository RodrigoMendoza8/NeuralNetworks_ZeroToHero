import requests

url = "https://pokeapi.co/api/v2/pokemon/"
parametros = {'limit': 1352}
repuesta = requests.get(url, params=parametros)
    
if repuesta.status_code == 200:
        datos = repuesta.json()
        nombres = [pokemon['name'] for pokemon in datos['results']]
        nombres = '\n'.join(nombres)
        with open('pokemones.txt', 'w', encoding='utf-8') as file:
            file.write(nombres)
else:
    print("Error al realizar la solicitud:", repuesta.status_code)
    