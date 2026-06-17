# here we use the library sys to take inputs from the terminal
# without asking the user to input something
# In this kind of code where we run the program from the terminal
# we need to be on the correct directory where the program is located, otherwise we will get an error
# for example in this case we need to be on the following
# PS C:\Users\Ching\OneDrive\Documents\Eduardo\Programación\class\Module 5\Tareas>
# now that we are in the directory we can run the program with the following command
# python figlet.py Eduardo
#
# if we want to be on the correct directory we have two options,
# we can go to file/open folder/ and select the folder where the program is located
# Or we can use the command line to navigate to the correct directory, as follows:
# cd "C:\Users\Ching\OneDrive\Documents\Eduardo\Programación\class\Module 5\Tareas"
# we can not use ''' ''' to make comments when the command sys is used, because the program will not run, we need to use # to make comments

import pyfiglet #importamos la libreria pyfiglet para poder usar sus funciones
import sys #importamos la libreria sys para poder dar inputs desde la terminal 
import random #importamos la libreria random para poder elegir un formato de letra al azar


fonts = pyfiglet.Figlet().getFonts() #esta funcion sirve para obtener una lista de los formatos de letra disponibles en la libreria pyfiglet, y la guardamos en la variable fonts 
if len(sys.argv) == 1: #si el usuario no da ningun argumento al correr el programa (ya que el nombre del programa es el argumento [0]), en este caso se correria python figlet.py sin nada mas
    format = random.choice(fonts)#se iguala una variable a la funcioin random.choice, que elige un elemento al azar de la lista fonts

#la siguiente linea evalua si el usuario dio tres argumentos en la terminal, el primer argumento es el nombre del programa, el segundo argumento es -f o --font
# y el tercer argumento es un formato de letra que forsozamente se encuentra en la lista fonts, 
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in fonts:
    format = sys.argv[2] #en dado caso que las tres condiciones se cumplan, se iguala la variable format al tercer argumento que el usuario dio en la terminal, que es el formato de letra  

else: #si ninguna de las condiciones anteriores se cumple, se le pide al usuario que ingrese un formato de letra valido
    sys.exit("Enter a valid font")

text = input("Input: ") #una vez que se evaluo el formato de la terminal, se pide el texto que se quiere convertir 
text_w_format = pyfiglet.figlet_format(text, font=format) #esta linea sirve para convertir el texto, se ve en el argumento que tiene el texto introducido y el formato dado por la variable format
print("Output:  ")#se impirme output con un salto de linea 
print(text_w_format)#se imprime el texto ya con el formato
