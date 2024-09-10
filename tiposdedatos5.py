#DEFINIMOS UN DICCIONARIO CON INFORMACION PERSONAL
persona = {"nombre": "tezna","edad":20,"ciudad":"cali"}
for clave, valor in persona.items():
    print(f"{clave.capitalize()}:{valor}")