
def main():
    while True: #This infinite loop helps us to ask as many times as the user enter a wrong date format. We will break the loop when the user enter a correct date 
        try: #to make this reprompt we use a try except block. We will raise a ValueError when the user enter a wrong date format and we will catch that error to reprompt the user.
            date = input("Date: ")
            date = date.title().strip() #we standardize the input by converting it to title case and stripping 

            if date[0].isalpha(): #if the first letter of the input is an alphabet, we will assume that the user enter a date in the format "Month Day, Year" 
                alpha_date = convert_alpha_date(date) #we call the function that convert "month day, year" into a tuple of (month, day, year) and we store it in a variable called alpha_date
                print(f"{alpha_date[2]}-{alpha_date[0]:02}-{alpha_date[1]:02}") #we print the date in the format "Year-Month-Day" using f-string and we use :02 to add a leading zero to the month and day if they are less than 10. We also convert the day to an integer to remove any leading zeros that the user might have entered.
                break

            else: #same as above but for the format "Month/Day/Year" all with numbers
                digit_date = convert_digit_date(date)
                print(f"{digit_date[2]}-{digit_date[0]:02}-{digit_date[1]:02}")
                break

        except ValueError: #we catch any ValueError that we raised in the try block and we simply reprompt the user to enter a date
            continue

           

def convert_alpha_date(date): #this function recives the input if it's alphabetic
    if date.count(",") != 1: #to make sure the input is in the correct format we check if it contains exactly one comma, if not we raise a ValueError
        raise ValueError #it will be read as an error and we will reprompt the user to enter a date
    
    months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]

    date = date.replace(",","") #we replace the comma by nothing
    month, day, year = date.split()#we split the date from any space and we store the month, day and year in separate variables

    try:
        month = months.index(month)+1 #we identify the index of month in the list of months, but as it start from 0 we add 1 to get the correct month number
        
        #next we convert the values of month, day and year to integers to make sure they are valid numbers and to remove any leading zeros that the user might have entered. If the conversion fails, it will raise a ValueError and we will reprompt the user to enter a date.
        month = int(month) 
        day = int(day)
        year = int(year)


    except ValueError:
        raise ValueError # if a valueerror is detected we raise a value error that will be read on line 18

    else: #if everthing goes well on the try block, we check if the month and day enter into valid range (month 1-12 and day 1-31)
        if not (1 <= month <= 12):
            raise ValueError

        if not (1 <= day <= 31):
            raise ValueError

        return month, day, year #we return the month, day and year as a tuple and save into a variable called alpha_date on line 17


def convert_digit_date(date): #this function is similar to the previous one but for the format "Month/Day/Year" all with numbers
    if date.count("/") != 2: #we check if the input contains exactly two slashes, if not we raise a ValueError
        raise ValueError
    
    month, day, year = date.split("/") #we split into three parts from each slash and we store the month, day and year as we did in the previous function
                  
    month = int(month)
    day = int(day)
    year = int(year)

    if not (1 <= month <= 12):
        raise ValueError

    if not (1 <= day <= 31):
        raise ValueError

    return month, day, year


main()
