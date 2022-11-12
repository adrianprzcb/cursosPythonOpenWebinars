cad = input("Dime un numero: ")
try:
    print(10/int(cad))
except ValueError:
    print("debes introducir un numero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("Error inesperado")
finally:
    print("hola")