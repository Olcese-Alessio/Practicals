total = 0
number = int(input("Number of items: "))
while number <= 0:
    print("Invalid item number")
    number = int(input("Number of items: "))
while number > 0:
    for i in range(number):
        price = float(input("Price of item: "))
        total += price

    if total > 100:
        total = total * 0.9
    print("Total price for {} items is ${:.2F}".format(number, total))
    number = int(input("Number of items: "))





