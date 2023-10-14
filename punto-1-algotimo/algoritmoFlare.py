def organizar_palabra(palabra):
    palabra_filtrada = ''.join(caracter for caracter in palabra if not caracter.isspace() and (not caracter.isdigit() or int(caracter) <= 5))
    arreglo_de_caracteres = list(palabra_filtrada)
    return arreglo_de_caracteres


palabra = input("Ingrese una palabra: ")
resultado = organizar_palabra(palabra)
print(resultado)

