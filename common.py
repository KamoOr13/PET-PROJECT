
def enumerate_lists_in_table(table):
    numbers = list(range(1, len(table) + 1))

    for i in range(len(table)):
        table[i].insert(0, str(numbers[i]))
    return table
