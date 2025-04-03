import json
import requests

class gestorjson:
    def __init__(self,arch):
        self.arch = arch

    def leerjson(self):
        try:
            with open(self.arch, 'r') as f:
               return json.load(f)      

 
        except FileNotFoundError:
            print("archivo no existe")
            return{}
        
        except json.JSONDecodeError:
            print("el archivo no esta en json")
            return{}
        
    def escribir(self,datos):
        with open(self.arch,'w') as f:
            return json.dump(datos,f,ident = 4)  