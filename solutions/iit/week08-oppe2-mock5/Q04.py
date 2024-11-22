def calculate_total_spent(filename):
    '''
    Args:
        filename (str): The path to the file containing transaction data.

    Returns:
        dict: A dictionary where keys are customer names and values are the total amount spent.
    '''

    total_spent = {}

    file = open(filename, 'r')
    for line in file:
        customer, amount, date = line.strip().split(',')
        amount = float(amount)

        if customer in total_spent:
            total_spent[customer] += amount
        else:
            total_spent[customer] = amount
    file.close()
    return total_spent
