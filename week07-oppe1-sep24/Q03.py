'''
Remove elements at given two indices of a list
Write a function remove_elements_at_two_indices that takes a list l and two indices i1 and i2. The function should remove the elements at these two indices from the list l.

Assume the indices are non-negative and unique.

The function should not return anything but should modify the input list directly.

NOTE: This is a function type question, you don't have to take input or print the output, just have to complete the required function definition.

Example

>>> l = [1, 2, 3, 4, 5, 6, 7]
>>> i1 = 5
>>> i2 = 1
>>> remove_elements_at_two_indices(l, i1, i2)
>>> l
[1, 3, 4, 5, 7]
Explanation
The elements at indices 5 and 1 are 6 and 2, respectively. These elements are removed from the list l.
'''

def remove_elements_at_two_indices(l: list, i1: int, i2: int):
    '''Remove elements at two specified indices in the list.

    Args:
        l : list - input list
        i1, i2 : int - indices of elements to remove
            both are non-negative and unique

    Returns:
        None - modifies the list in place
    '''
    
    ...