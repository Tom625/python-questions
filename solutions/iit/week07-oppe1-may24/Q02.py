def is_all_same_word_twice(strings: list) -> bool:
    '''
    Checks if all strings follow the format where 
    the same word is repeated exactly twice with a hyphen in-between them.

    Args:
        strings (list): A list of strings to be checked.

    Returns:
        bool: True if all strings are of the given format, otherwise False.
    '''

    # basic
    for string in strings:
        words = string.split('-')
        if not (len(words)==2 and words[0] and words[0]==words[1]):
            return False
    return True

    # feel free to try the below solutions also
    # using comprehensions
    '''
    separated_words_list = [string.split("-") for string in strings]
    return all(
        len(words)==2 and words[0]==words[1] and words[0]
        for words in separated_words_list
    )
    '''

    # functional
    '''
    separated_words_list = map(lambda x: x.split('-'),strings)
    return all(map(lambda x: len(x)==2 and x[0] and x[0]==x[1],separated_words_list))
    '''
