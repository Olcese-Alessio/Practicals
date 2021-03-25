numbers = [3, 1, 4, 1, 5, 9, 2]

'''Question 1. numbers[0]'''
''' Answer = 3'''
print(numbers[0])           #test

'''Question 2. numbers[-1] is assigned the last digit in the array (2)'''
''' Answer = 2'''
print(numbers[-1])          #test

'''Question 3. numbers[3] is assigned the 4th number in the array (1)'''''
''' Answer = 1'''
print(numbers[3])           #test

'''Question 4. numbers[:-1] is all the numbers minus the last 1'''
''' Answer = [3, 1, 4, 1, 5,9]'''
print(numbers[:-1])         #test

'''Question 5. numbers[3:4] is assigned the numbers in the array from 4th position to the 5th'''
''' Answer = [5]'''
print(numbers[4:5])         #test

'''Question 6 & 7. Both these functions check to see if the number 5 or 7 appears in the array'''
''' Answer = True, False'''
print(5 in numbers)         #test
print(7 in numbers)         #test


'''Question 8. "3" in numbers searches for the string 3 not the value 3'''
''' Answer = False'''
print("3" in numbers)       #test

'''Question 9. numbers = [6, 5, 3] adds those numbers to the array'''
'''Answer = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]'''
print(numbers + [6, 5, 3])  #test

numbers[0] = "ten"
print(numbers[0])           #test
numbers[-1] = 1
print(numbers[-1])          #test
numbers[2:]
print(numbers[2:])          #test
9 in numbers
print(9 in numbers)         #test




