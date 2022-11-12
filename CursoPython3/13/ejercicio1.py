#!/usr/bin/env python
import os
import shutil

ruta = os.getcwd() + os.sep
origen = ruta + 'origen.txt'
destino = ruta + 'destino.txt'

try:
    shutil.copyfile(origen, destino)
    print("Archivo copiado")
except:
    print("Se ha producido un error")
