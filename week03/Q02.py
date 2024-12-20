'''
Write a multi functional program that takes input task from standard input and does the corresponding taks accordingly. Note that the useage of for loop is not allowed in this exercise.

Part 1 - while loop to for loop
factorial - print factorial of a given non-negative integer n (Type: Accumulation)
Input - n:int
even_numbers - Print the even numbers from 0 (including) till the given input number n(including) in multiple lines (Type: Just Iterating)
Input - n:int
power_sequence - Print the sequence 1, 2, 4, 8, 16, ... n terms in same line in multiple lines, where n is taken from the input(Type: Mapping)
Input - n:int
Part 2 - for loop With range
sum_not_divisible - Print the sum of positive less that the given number n and not divisible by 4 and 5. (Type: Filtered Accumulation)
Input - n:int
from_k - Starting from 100 and going in the decreasing order, print the reverse(digits reversed) of first n numbers starting from k which do not have the digit 5 and 9 and is odd number in multiple lines.
Input - n:int, k:int
part 3 - for loop with iterables.
string_iter - Given a string s of digits print the numerical value of the digit multiplied by the previous digit. Assume the pevious digit for the first element to be 1.
Input - s:str
list_iter - Print the elements of a list l line by line in the format {element} - type: {type} where the element is the current element being iterated by the for loop and type is the type of the element. (Even though list are not covered in this week, this is included to demonstrate the similarity between iterating characters in a str and items in a list)
Input - l:list
'''
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "while " in content:
    print("You should not use while loop or the word while anywhere in this exercise")

# your code should not use more than 7 for loops 
# assuming one for loop per problem
if content.count("for ")>7:
    print("You should not use more than 7 for loops")

# This is the first line of the exercise
task = input()
# <eoi>

if task == 'factorial':
    n = int(input())
    result = 1
    i = 1
    while i <=n:
        result*=i
        i+=1

    print(result)
elif task == 'even_numbers':
    n = ...
    while i< n+1:
        print(i)
        i+=2

elif task == 'power_sequence':
    n = ...
    result = 1
    while i<n:
        print(result)
        result*=2
        i+=1

elif task == 'sum_not_divisible':
    ...

elif task == 'from_k':
    ...

elif task == 'string_iter':
    ...

elif task == 'list_iter':
    lst = eval(input()) # this will load the list from input

else:
    print("Invalid")