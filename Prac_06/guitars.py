from Prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        added_guitar = Guitar(name, year, cost)
        guitars.append(added_guitar)
        print(added_guitar, "added.")
        name = input("Name: ")

    if guitars:
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}"
                  " {}".format(i, guitar.name, guitar.year, guitar.cost, vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
