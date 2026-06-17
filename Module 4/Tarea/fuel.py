def main():
    while True:
        fraction = input("Fraction: ")
        if "/" not in fraction:
            continue
        x, y = fraction.split("/")

        try:
            x = int(x)
            y = int(y)

            if x < 0:
                raise ValueError

        except ValueError:
            continue

        else:
            if x >= 0 and y >= 0 and x <= y:
                try:
                    percentage = round(x / y * 100)
                except ZeroDivisionError:
                    continue
                else:
                    if percentage >= 99:
                        print("F")
                        break
                    elif percentage <= 1:
                        print("E")
                        break
                    else:
                        print(f"{percentage}%")
                        break

main()


        

            





  