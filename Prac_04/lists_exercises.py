
''' Basic List Operations '''

numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("the first number is", numbers[0])
print("the last number is", numbers[-1])
print("the smallest number is", min(numbers))
print("the largest number is", max(numbers))
print("the average of numbers is", sum(numbers)/len(numbers))



'''Woefully inadequate security  checker'''

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
             'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
             'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter Username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")


