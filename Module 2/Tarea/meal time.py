'''en este programa se pidió que el usuario metiera una hora en formato ##:## de 24h 
se requiere que solo se acepten tres intervalos de tiempo 7-8 12-13 y 18-19
se pidió que lo hieceramos con dos funciones, una que pidiera el input ##:## y otra que convirtiera ese input 
a un formato de horas solamente (7:30 = 7.5)
También se destacó la importancia de no eliminar la función que llama al main() al final del programa
con la finalidad de hacer posible su revisón y evaluación por parte de los profesores'''


def main(): #main function that calls the other functions
    meal_time = convert(input("What time is it? ")) #we call the convert function to convert the input and asign that value to the variable meal_time
    if 7 <= meal_time <= 8:
        print("breakfast time")

    elif 12 <= meal_time <=13:
        print("lunch time")

    elif 18 <= meal_time <=19:
        print("dinner time")


def convert(time): #this function recives a string value from the input when it's called
    time = time.strip().lower()

    if "am" in time or "pm" in time:
        time, period = time.split()
        hours, minutes = time.split(":") #we split the string value into two variables from ":" and we asign everything before ":" to hours and everything after ":" to minutes
        hours = float(hours) #convert the hours variable to a float value 
        minutes = float(minutes)

        if period == "am":
            if hours == 12:
                hours = 0
        elif period == "pm":
            if hours != 12:
                hours += 12
    else:
        hours, minutes = time.split(":") #we split the string value into two variables from ":" and we asign everything before ":" to hours and everything after ":" to minutes
        hours = float(hours) #convert the hours variable to a float value 
        minutes = float(minutes)

    h = hours + (minutes/60) #the final value will be the sum of the hours plus the minutes converted to hours by dividing it by 60
    return h #we return the finnal value to the main function where it was called


if __name__ == "__main__": #this line is used to check if the script is being run directly (as the main program) or if it is being imported as a module in another script. If the script is being run directly, the code inside this block will be executed. If it is being imported, the code inside this block will not be executed. This is a common practice in Python to allow for both direct execution and importation of code.
    main()
