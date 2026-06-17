'''
En este codigo se pide un archivo con su extension y devuelve el "MIME type" el cual se puede consultar en 
https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types/Common_types

se pide que acepte la cadena de texto sin importar mayusculas o minusculas y que se eliminen los espacios al principio y al final de la cadena de texto
pide que consultemos el link para ver la correcta MIME type de cada extension, y que si no se encuentra la extension se devuelva "application/octet-stream"


'''

phrase = input("File name: ").strip().lower()

if phrase.endswith((".gif",".png")): #si la frase termina en .gif o .png
    p = phrase.rfind(".") #busca la ultima aparicion del punto y devuelve su posicion
    print("image/"+phrase[p+1:]) #imprime "image/" concatenado con la extension del archivo, para eso se usa slicing con [p+1:] para obtener la parte de la cadena que va despues del punto
   #imprime la extension sin el punto, para eso se usa slicing con [p+1:]
    #es importante destacar que rfind busca el primer punto de adelante hacia atras, por lo que si el nombre del archivo tiene varios puntos, se tomara el ultimo como la extension
    #tambien destacar que "P" toma el valor de la posicion del punto, devuelve el numero de la posicion del punto en el string
    #por este motivo se impirme phrase pero solo desde la posicion del punto hacia adelante, para obtener la extension sin el punto

elif phrase.endswith((".jpg",".jpeg")):
    print("image/jpeg") #como el link declara que tanto .jpg como .jpeg tienen el mismo MIME type, no es necesario usar slicing para obtener la extension, ya que ambos casos se imprimira "image/jpeg"


elif phrase.endswith((".pdf","zip")): #lo mismo que .gif y.png solo cambia la parte incial del MIME type, que en este caso es "application/" en lugar de "image/"
    p = phrase.rfind(".")
    print("application/",end="")
    print(phrase[p+1:])

elif phrase.endswith((".txt")):
    p = phrase.rfind(".")
    print("text/"+phrase[:p])#aqui en lugar que se imprima del punto hacia la derecha de phrase,
    #se imprime del punto hacia la izquierda, para obtener el nombre del archivo sin la extension, ya que el link declara que el MIME type de los archivos .txt es "text/" seguido del nombre del archivo sin la extension


else:
    print("application/octet-stream") #esto se imprime si no se encuentra
