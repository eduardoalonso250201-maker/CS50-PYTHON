
def main():
    dollars = dollars_to_float(input("How much was the meal? ")) #we create the variable dollar and set it equal to the function dollars_to_float, which takes the user input as an argument. The user input is a string that represents the cost of the meal, and the function will convert it to a float after removing the dollar sign and any extra spaces. 
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent #now that dollar_to_float and percent_to_float have converted the strings to floats, and the variables are equal to the return values of those functions, we can multiply them together to get the tip amount. 
    print(f"Leave ${tip:.2f}") #print the result, formatted to 2 decimal places, and include a dollar sign in the output. 


def dollars_to_float(d): #this function recieves a string as an argument,from the user input   
    dollar = d.replace("$"," ").strip() #we create a variable wich is equal to the string d, but we use the replace function to remove the dollar sign and replace it with a space. We also use the strip function to remove that space
    dollar = float(dollar) #then we convert that string to a float 
    return dollar #now the function "dollars_to_float" will return the dollar variable


def percent_to_float(p):
    percent = p.replace("%"," ").strip()#here we repleace the percent sign with a space and then we strip that space
    percent = (float(percent))/100
    return percent


main()