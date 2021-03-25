
import random

numbers_per_line = 6
min_number = 1
max_number = 45


def main():
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("Invalid amount")
        quick_picks = int(input("How many quick picks? "))
    for i in range(quick_picks):
        quick_pick = []
        for j in range(numbers_per_line):
            number = random.randint(min_number, max_number)
            while number in quick_pick:
                number = random.randint(min_number, max_number)
            quick_pick.append(number)
        quick_pick.sort()
        print(quick_pick)


main()
