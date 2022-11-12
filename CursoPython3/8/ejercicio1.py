#!/usr/bin/env python
dicti = {}
frase = input("Frase:")
lista_palabras = frase.split(" ")
for palabra in lista_palabras:
    if palabra in dicti:
        dicti[palabra] += 1
    else:
        dicti[palabra] = 1

for campo, valor in dicti.items():
    print(campo, "->", valor)
