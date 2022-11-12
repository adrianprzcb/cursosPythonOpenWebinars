#!/usr/bin/env python
letra = input("Letra:")
if "A" <= letra <= "Z":
    print("Mayúscula")
elif "a" <= letra <= "z":
    print("Minúscula")
else:
    print("Otro carácter")
