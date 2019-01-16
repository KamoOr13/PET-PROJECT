#User interface module
import data_manager
import common

title_list = ['numer','nazwa składnika','ilość','miara']


def print_table(table, title_list): 
    table = common.enumerate_lists_in_table(table)

    title_length_list = []
    for i in range (len(title_list)):
        title_length_list.append(len(title_list[i]))

    table_length_list = []
    list = []
    for j in range(len(table[0])):
        list += (len(table[i][j]) for i in range(len(table))) 
        table_length_list.append(max(list))

    columns_width = []
    for i in range(len(title_length_list)):
        columns_width.append(max(table_length_list[i], title_length_list[i]))

    total_width = -3
    for x in columns_width:
        total_width += x + 1
    
    print("/", "-" * (total_width), "\\")

    #prints headers
    header = ""
    for i in range(len(columns_width)):
        header += "|" + title_list[i].center(columns_width[i], " ") 
    header += "|"
    print(header)

    for i in range(len(table)):
        separating_line = "|"
        row = "|"
        #prints seperation lines
        for j in range(len(table[i])):
            separating_line += "-" * (int(columns_width[j])) + "|"
        print(separating_line)
        #prints ingredients consistent with table format
        for j in range(len(table[i])):
            row += table[i][j].center(int(columns_width[j]), " ") + "|"
        print(row)

    print("\\", "-" * (total_width), "/")


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for i in range(len(list_labels)):
        user_input = input('Wprowadź %s: ' % (list_labels[i]))
        inputs.append(user_input)
    return inputs

def print_menu(title, list_options, exit_message):
    print(title)
    for number, option in enumerate(list_options, 1):
        print("    ({}) {}".format(number, option))
    print("    (0)", exit_message)


'''
def print_results(result, label):
        print(label)
        print(result)
        print('/n')
    
def print_menu(title, list_options, exit_message):
        print(title)
    for k, l in enumerate(list_options):
        print("({}) {}".format(k + 1, l))
    print("(0)", exit_message)

def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for i in range(len(list_labels)):
        inputs.append(input('Enter ' + list_labels[i] + ': ')) 
    return inputs

def print_error_message(message):
        print('Error: {}'.format(message))
'''

if __name__ == "__main__":
    print_table(data_manager.get_table_from_file('recipe_ingredients/jajecznica.txt'), title_list)
