#!/usr/bin/env python
cad = input("Dame un número:")
try:
    print(10 / int(cad))
except ValueError:
    print("No se puede convertir a entero")
except ZeroDivisionError:
    print("No se puede divdir por cero")
except Exception as e:
    print("Otro error")
