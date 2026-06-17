def main():
    text = input("camelCase: ")
    print("snake_case: ", end="") #se impirme el texto que para darle formato a la salida, el end="" es para que no se imprima un salto de linea al final del texto
    adding_low_bar(text) #se llama a la funcion con el input como argumento
    print() #se impirme un salto de linea al final del texto
  


def adding_low_bar(text): #se crea la funcion con su argumento en donde se llamo la funcion
    for letter in text: #se itera por cada letra del texto
        if letter.isupper(): #si en la iteracion la letra es mayuscula
            print("_", end="") #se imprime un guion bajo antes de la letra mayuscula, el end="" es para que no se imprima un salto de linea al final del texto
        print(letter.lower(), end="") #se imprime la letra en minuscula, el end="" es para que no se imprima un salto de linea al final del texto


main()
        