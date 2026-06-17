arithmetic=input("Expression: ")
arithmetic=arithmetic.replace(" ","") #we use the replace function to remove any spaces from the user input, and we set the variable arithmetic equal to the result of that replacement. This is done to ensure that the expression can be evaluated correctly without any issues caused by extra spaces.
if arithmetic[2] == "0" and arithmetic[1] in ("/","%"): #we check if the third character of the string is "0" and if the second character is one of the division operators ("/", "//", "%").
    #If both conditions are true, it means that the expression involves division by zero, which is undefined.
    # the 'in' operator checks if the operator is any of these three. helps to make the code shorter instead of putting mulple == for each operator, we can just check if the second character is in a string that contains all the division operators.
    print("undetermined result")
else:
    print("%.1f" % eval(arithmetic))