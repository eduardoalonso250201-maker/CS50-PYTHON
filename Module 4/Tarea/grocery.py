def main():

    list = []
    dictionary = {}

    while True:

        try:
            item = input()

            if item.isdigit():
                raise ValueError

        except ValueError:
            continue

        except EOFError: 
            print()
            break

        else:
            grocery = list.append(item)
            grocery = [product.upper() for product in list]

    for i in grocery:
        if i in dictionary:
            dictionary[i] += 1

        else:
            dictionary[i] = 1

    for value in dictionary:
        print(f"{dictionary[value]} {value}")

main()