import inflect

p = inflect.engine()


def main():
    names = []
    while True:

        try:
            name = input("Input: ")
            names.append(name)

        except EOFError:
            break

    print()
    print(f"Adieu, adieu, to {p.join(names)}")


main()
