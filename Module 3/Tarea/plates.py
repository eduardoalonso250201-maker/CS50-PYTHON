def main():
    plate = input("Plate: ") #Here we ask for a string as an input and we store it in the variable "plate"
    if is_valid(plate): #we call the function "is_valid" taking the string "plate" as an argument, if the function returns true we print "Valid", if not we print "Invalid" 
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() or s.isalpha: #First we check if our string is alphanumeric or just alphabetic, if not we return false and the function ends, if it is we continue with the next condition
        if s[:2].isalpha() and (2 <= len(s) <= 6): #We cjeck if the first two characters of the string are alphabetic and if the length of the string is between 2 and 6, if not we return false and the function ends, if it is we continue with the next condition
            i = 0 #we declare a iterator variable to 0, this variable will help us to iterate through the string as index of each letter
            while i < len(s) and s[i].isalpha(): #we loop through the string until we find a character that is not alphabetic, we also check that we are not out of the string with the condition i < len(s)
                i += 1 #we sum 1 to the variable i to iterate through the string, so we sould move forward in each letter and check if that letter (iteration) achieve the conditions
            if i < len(s): #we check if the iteration variable still less than the length of the string,  
                if s[i] == '0': #With this line we make sure that the first value after the alphabetics letters of our string is not "0", if it is we return false and the function ends, if not we continue
                    return False
                while i < len(s) and s[i].isdigit(): #This line is almost the same as 13-14 but now we check if the character is a digit, this helps to make sure that if the string contains numbers, those numbers are at the end of the string and they are digits, if not we return false and the function ends, if it is we continue
                    i += 1
            return i == len(s) #This line is really important, here we check if the iteration variable is equal to the length of the string, this means that we have iterated through all the characters of the string and all of them achieve the conditions, so we return true, if not we return false and the function ends
        else:
            return False #if the condition of line 11 is not achieved we return false and the function ends
    else:
        return False #if the condition of line 10 is not achieved we return false and the function ends


main()
