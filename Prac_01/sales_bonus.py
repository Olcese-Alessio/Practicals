sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = 0.1 * sales
        print("Your bonus is ${:.2f}".format(bonus))
    else:
        bonus = 0.15 * sales
        print("Your bonus is ${:.2f}".format(bonus))
    sales = float(input("Enter new sales: $"))


