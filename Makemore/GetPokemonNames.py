import requests

url = "https://pokeapi.co/api/v2/pokemon/"
parametros = {'limit': 1352}
repuesta = requests.get(url, params=parametros)
    
if repuesta.status_code == 200:
        datos = repuesta.json()
        nombres = [pokemon['name'] for pokemon in datos['results']]
        nombres = '\n'.join(nombres)
        nombres_sin_numeros = ''.join([i for i in nombres if not i.isdigit()])
        with open('Makemore/pokemones.txt', 'w', encoding='utf-8') as file:
            file.write(nombres_sin_numeros)
else:
    print("Error al realizar la solicitud:", repuesta.status_code)
    
nombres_sin_guiones = nombres_sin_numeros.replace('-','')
with open('Makemore/pokemones_sin_guiones.txt', 'w', encoding='utf-8') as file:
    file.write(nombres_sin_guiones)
    
