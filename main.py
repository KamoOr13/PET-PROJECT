import ui
import common
from os import sys

#MODULES
from modules import recipes
from modules import groceries
from modules import week_menu


def choose_menu_option():
    inputs = ui.get_inputs(["Please enter a number: "], "")
    option = str(inputs[0])
    if option == "1":
        recipes.start_module()
    elif option == "2":
        groceries.start_module()
    elif option == "3":
        week_menu.start_module()
    elif option == "4":
        week_menu.random_menu()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")

def main():
    MENU_OPTIONS = ('Przepisy', 'Lista zakupów', 'Jadłospis', 'Random')
    ui.print_menu('Menu główne:', MENU_OPTIONS, 'Wyjdź')
    choose_menu_option()



if __name__ == "__main__":
    main()
