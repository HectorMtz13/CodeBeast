import json
import requests

class gestorjson:  # Crea un archivo JSON
    def __init__(self, arch):
        self.arch = arch

    def leerjson(self):  # Lee el contenido del archivo y lo retorna como diccionario
        try:
            with open(self.arch, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print("Error: El archivo no existe.")
            return {}
        except json.JSONDecodeError:
            print("Error: El archivo no está en formato JSON válido.")
            return {}

    def escribir(self, datos):  # Escribe los datos en el archivo, recibe un diccionario como parámetro
        with open(self.arch, 'w') as f:
            json.dump(datos, f, indent=4) 

    def modificarjson(self, llave, valor):  # Modifica o agrega una clave en el JSON
        datos = self.leerjson()
        datos[llave] = valor
        self.escribir(datos) 

    def obtenerPokemon(self, Pokemon):  # Obtiene información de un Pokémon desde una API y lo guarda en JSON
        try:
            url = f"https://pokeapi.co/api/v2/pokemon/{Pokemon}"  
            response = requests.get(url)
            response.raise_for_status()  # Lanza una excepción si la solicitud falla
            data = response.json()
            self.escribir(data)  #
        except requests.exceptions.HTTPError: 
            print("Error: La URL no existe o la petición falló.")
        except requests.exceptions.RequestException: 
            print("Error: No se pudo realizar la petición.")
        
gjson = gestorjson("pokemon.json")
gjson.obtenerPokemon("pikachu")
pokemoninfo = gjson.leerjson()
print(pokemoninfo)
#seleccionamos un conjunto del diccionario
x = pokemoninfo['name']
print(x)