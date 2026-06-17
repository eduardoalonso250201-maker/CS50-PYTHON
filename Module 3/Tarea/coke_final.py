while True: #we create an infinite loop to keep asking the user to insert coins until they have paid the full amount
    print("Amount Due: 50") #we print this message to let them know how much they have to pay
    money = int(input("Insert Coin: "))

    if money == 25 or money == 10 or money == 5 or money == 50: #we check if the user has inserted a valid coin, if not we would start from the beginning of the loop and ask them to insert a coin again
        if money == 50:
            print("Change Owed: 0") #if this condition is true we end the loop and we print that there is no change owed
        
        else: #now that we filter the types of coins (50, 25, 10, 5) and make sure that the user still owes money, we procedure to make the calculation
            change = 50 - money #we calculate the change that the user still owes
            while change > 0: #this line helps us to loop the code until the user has paid the full amount
                print(f"Amount Due: {change}") #we print the amount of change that the user still owes
                money = int(input("Insert Coin: ")) #we ask the user to input the amount of money as an integer
                change = change - money #this is the new value that change takes to iterate form line 14, until change reaches 0 or less
                if change < 0: #we add this to line in case the user has inserted more money than they owe, so we can calculate the change that we have to give back to them
                    print(f"Change Owed: {abs(change)}") #we use the abs function to get the absolute value of change, since change is negative
                elif change == 0: #if change is 0 we end the loop and we print that there is no change owed
                    print("Change Owed: 0")

        break #we end the loop once one of the conditions from line 7 or line 17 is true
    