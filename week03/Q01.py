'''
Problem Statement

Problem type - Standard Input - Standard Output

NOTE: None of this problem statements can be written using a for since the number of repetition is indefinite.

Implement different parts of a multi-functional program based on an initial input value. Each part of the program will handle various tasks related to accumulation, filtering, mapping, and combinations of these operations. None of the tasks should use explicit loops for definite repetitions, and the program should handle indefinite inputs gracefully.

Tasks

Accumulation - Accumulating a final result
sum_until_0: Continuously read integers from standard input until you receive a zero. Print the sum of these integers.
total_price: Continuously read pairs of integers from standard input, representing the quantity and price of items, until you receive the string "END". Print the total price of all items.
Filtering - Selecting based on a criterion
only_ed_or_ing: Continuously read strings from standard input until you encounter the word "STOP" (case insensitive and not included in the output). Print only those strings that end with "ed" or "ing" (case insensitive).
reverse_sum_palindrome: Continuously read positive integers from standard input until you encounter a "-1"(not included in the output). Print only those integers for which the sum of the number and its reverse is a palindrome.
Mapping - Applying the same operation to different items
double_string: Continuously read lines from standard input until an empty line is encountered. Print each line repeated twice.
odd_char: Continuously read strings from standard input until you encounter a string ending with a "."(include that string with the "." in the output). Extract characters at odd positions (starting from 1) of each line, and print the results in a single line separated by spaces.
Filter and Map - Applying an operation to selected items
only_even_squares: Continuously read numbers from standard input until "NAN" is encountered. Print the square of each number only if it is even.
Filter and Accumulate - Accumulating a result with selected items
only_odd_lines: Continuously read lines from standard input until "END"(not included in the output) is encountered. Create a string by prepending only the odd lines (starting from 1) with a newline character in between, and print the result which will be the odd lines in reverse order.
'''
# Note this prefix code is to verify that you are not using any for loops in this exercise. This won't affect any other functionality of the program.
with open(__file__) as f:
    content = f.read().split("# <eoi>")[2]
if "for " in content:
    print("You should not use for loop or the word for anywhere in this exercise")

# This is the first line of the exercise
task = input()
# <eoi>

if task == "sum_until_0":
    total = 0
    n = int(input())
    while ...: # the terminal condition
        ... # add n to the total
        ... # take the next n form the input
    print(total)

elif task == "total_price":
    total_price = 0
    while ...: # repeat forever since we are breaking inside
        line = input()
        if ...: # The terminal condition
            break
        quantity, price = line.split() # split uses space by default
        quantity, price = ... # convert to ints
        ... # accumulate the total price
    print(total_price)
elif task == "only_ed_or_ing":
    ...

elif task == "reverse_sum_palindrome":
    ...

elif task == "double_string":
    ...

elif task == "odd_char":
    ...

elif task == "only_even_squares":
    ...

elif task == "only_odd_lines":
    ...