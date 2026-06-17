def main(): #the main function is the entry point of the program. It is where the execution starts when the program is run. In this case, the main function is defined to call the phrase function with user input. The main function is typically used to organize the flow of the program and to call other functions as needed
    phrase(input()) #phrase is the name of the function that I create, and input is a built-in function

def phrase(g): # we create a funtion that calls the variable g (g is the paramter got on the input, g=parameter obtained from the input), wich came from the previous function (phrase)
    if ":)" or ":(" in g: # if the string ":)" or ":(" is found in the variable g, then the code inside this if statement will be executed. The condition checks if either of the two strings is present in g. If either of them is found, the condition will evaluate to True, and the code block inside the if statement will be executed.
        print(g.replace(":)", "🙂",).replace(":(", "🙁"))

    elif g: #if the string does not contain ":)" or ":(", but it is not empty (g is a non-empty string) it will print the strigs as they are, without any modifications
        print(g)

main()
