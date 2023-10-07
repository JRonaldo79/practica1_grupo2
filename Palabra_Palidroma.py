
# Funcion para comprobar si la palabra es palíndroma
def es_palindroma(palabra):

    # Elimina espacios en blanco y convierte la palabra a minusculas
    palabra = palabra.replace(" ", " ").lower()

    # Compruba si la palabra es igual a su inversa
    if palabra == palabra[::-1]:
        return True
    else:
        return False


# Funcion para inrgresar una palabra y verificar si es o no palíndroma
def main():
    palabra = input("Ingrese una palabra: ")

    if es_palindroma(palabra):
        print(f"'{palabra}' es una palabra palíndroma. ")

    else:
        print(f"'{palabra}' no es una palabra palíndroma. ")


if __name__ == "__main__":
    main()
