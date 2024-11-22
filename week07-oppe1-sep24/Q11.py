'''
Count Positive Integers Ignoring None
Given a list which contains integers and None, count the number of positive integers while ignoring None values. Zero should not be counted.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

For the list [1, -2, 3, 0, None, 4], the result should be 3 because the positive integers are 1, 3, and 4.

Explanation

We ignore None values.
We also ignore 0 because it is not positive.
The positive integers are 1, 3, and 4, so the count is 3.
'''

def count_positive_ignore_none(nums: list):
    '''
    Count the number of positive integers in the list, ignoring `None` values and zeros.

    Args:
        nums (list): A list of numbers, possibly containing `None` values.

    Returns:
        int: The count of positive integers in the list.
    '''
    ...