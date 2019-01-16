from os import system, name
import ui


def enumerate_lists_in_table(table):
    numbers = list(range(1, len(table) + 1))

    for i in range(len(table)):
        table[i].insert(0, str(numbers[i]))
    return table

def common_clear(): #clears terminal
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else: 
        _ = system('clear')
