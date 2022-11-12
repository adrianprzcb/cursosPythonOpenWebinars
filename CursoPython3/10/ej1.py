import json

datos_json = '{"nombre":"carlos","edad":23}'
datos = json.loads(datos_json)
type(datos)
print(datos)


with open("ejemplo1.json") as fichero:
    datos2 = json.load(fichero)
type(datos2)
print(datos2)

