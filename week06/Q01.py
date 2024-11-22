'''
Implement the given functions where you have to read the input from the standard input with the input format given in the docstring of the function and return the output in the required type.

'''

# heterogeneous - multi line
def get_student_details():
    '''
    Get the student details over multiple lines

    Input format:

    name
    age
    rollno

    Return: name:str, age:int, rollno:int
    '''
    ...
    return name, age, rollno

# heterogeneous - single line 
def get_student_details_same_line():
    '''
    Get the student details from the same line

    Input format:(separated by space)

    name age rollno

    Return: name:str, age:int, rollno:int
    '''
    ...

    return name, age, rollno

# homogeneous - single line
def get_comma_separated_integers():
    '''
    Get a list of comma separated integers from input

    Return: numbers:list[int]
    '''
    ...

    return numbers

# homogeneous - multi-line - definite
def get_n_float_numbers():
    '''
    Get n float numbers with one number in each line 
    and the first line has n.

    Input Format:
    n
    num1
    num2
    ...
    numn

    Return: nums:list[float]
    '''
    ...

    return nums

# homogeneous - multi-line - indefinite
def get_nums_until_end():
    '''
    Get float numbers with one number in each line 
    until the input is "end"(case insensitive)

    Input Format:
    num1
    num2
    ...
    numx
    End

    Return: nums:list[float]
    '''
    ...

    return nums

# hybrid - single line
def get_batsman_runs():
    '''
    Get batsman name, number and runs as a list

    Input format: (separated by space)
    name no run1 run2 run3 ...

    Return: name:str, no:int, runs:list[int]
    '''
    ...

    return name, no, runs

# key value 
def get_course_scores():
    '''
    Get course name and scores of the over multiple lines where 
    course name and scores are separated by a hypen in each line.
    First line corresponds to the number or entries.

    Input format:
    2
    course1-score1
    course2-score2

    Return: dict[str,int] - with course name as key and score as value
    '''
    ...

    return course_scores

# dict with list as values
def get_all_batsman_runs():
    '''
    Given the batsman name and the comma separated runs 
    where both are seperted by a hypen in multiple lines, 
    create a dictionary with batsman name and list of runs as value.
    The number of lines is given in the first line

    Input format:
    3
    batsman1-1,2,1,4,6,2,2,1
    batsman2-2,2,6,4,1
    batsman3-6,1,2,4,4,2

    Return: dict[str,list[int]] - with batsman name as key and list of runs as values
    '''
    ...

    return batsman_runs

# csv - list of dicts
def get_student_marks():
    '''
    Given the student rollno, city, age,
    course1_marks, course2_marks and course3_marks 
    as comma separated values over multiple lines,
    create a list of dict with the above attributes as keys 
    and the corresponding value as values.
    The number of lines is given in the first line

    Input Format:
    n
    1,citya,23,86,69,86
    2,cityb,19,78,65,89
    ...
    n,cityx,35,89,57,76

    Return: 
    student_data - list[dict]: where each dict would be 

    {'rollno':int, 'city':str,'age':int, 
    'course1':int, 'course2':int, 'course3':int}
    '''
    ...

    return student_data

# list of dicts
def get_student_data_over_multiple_lines():
    '''
    Given each attribute as described above in given over multiple lines 
    and multiple entries are given create a dictionary as described above.

    Input format:
    n
    1
    citya
    23
    86
    69
    86
    2
    cityb
    19
    78
    65
    89
    ...
    n
    cityx
    35
    89
    57
    76
    '''

    ...

    return student_data