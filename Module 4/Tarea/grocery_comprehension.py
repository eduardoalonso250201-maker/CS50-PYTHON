def main():

    list = [] #we create an empty list to store the items that the user will input
    dictionary = {} #we create an empty dictionary to store the items and their counts

    while True: #we create an infinite loop

        try:
            item = input() #we ask for input without any prompt

            if item.isdigit(): #if the item is a number we raise a ValueError to skip it
                raise ValueError

        except ValueError:
            continue #we skip the rest of the loop and ask for input again

        except EOFError: #if the user gives a ctrl + z or ctrl + d we catch the EOFError and break the loop
            print() #we print an empty line \n
            break

        else: #everytime the try block runs without any exception we execute the else block
            grocery = list.append(item) #we add the item to the list
            grocery = [product.upper() for product in list] #list comprehension to convert to create a new list with the items in uppercase 
            dictionary = {product: grocery.count(product) for product in grocery} #dictionary comprehension to create a dictionary with the items as keys and their counts as values

    for value in sorted(dictionary.keys()): #once the dictionary is created we loop through it to print the items in alphabetical orderand values 
        print(f"{dictionary[value]} {value}") #first we print the value and then a space and then the key

main()