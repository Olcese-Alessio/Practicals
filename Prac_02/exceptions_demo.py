"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
A ValueError will occur if a value gets inputted that is not a number, for example if the letter
'C' was inputted for the numerator it would error

2. When will a ZeroDivisionError occur?
This error will occur if a 0 is inputted as the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Done (if statement)
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Invalid denominator")
        denominator = int(input("Enter the new denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")