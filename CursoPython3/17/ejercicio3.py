#!/usr/bin/env python

def guardar_agenda(l_agenda, **kwars):
    l_agenda.append(kwars)
    return l_agenda


def main():
    agenda = []
    cantidad = int(input("¿Cuántos contactos vas a introducir?"))
    for i in range(cantidad):
        contacto = {}
        contacto["nombre"] = input("Indica el nombre:")
        contacto["teléfono"] = input("Indica el teléfono:")
        campo = input("Introduce otro campo:")
        while campo != "*":
            contacto[campo] = input("Introduce valor:")
            campo = input("Introduce otro campo:")
        agenda = guardar_agenda(agenda, **contacto)
    print(agenda)


if __name__ == '__main__':
    main()
