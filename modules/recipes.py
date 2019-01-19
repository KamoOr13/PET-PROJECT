#IMPORTING MODULES
import common
import ui
import os
import sys

RECIPES_LABELS = ("No.", "Przepis")
RECIPES_MENU = ('Szczegóły przepisu', 'Dodaj przepis', 'Usuń przepis')

recipe_names_path_folder = 'recipe_ingredients'
def start_module():
    common.common_clear()
    make_recipes_name_list()
    ui.print_menu('Menu przepisów:', RECIPES_MENU, 'Wróc do menu głownego')
    choose_option = ui.get_inputs(['Wybierz którąś z opcji:'], '')

    if choose_option[0] == "1":
        pass
    elif choose_option[0] == "2":
        pass
    elif choose_option[0] == "3":
        pass
    elif choose_option[0] == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")

def make_recipes_name_list():
    r_list = os.listdir(recipe_names_path_folder)
    r_list.remove('README.txt')

    recipe_names_conainer = []
    for recipe_name in r_list:
        recipe_name = recipe_name.strip('.txt')
        recipe_names_conainer.append(recipe_name)
    ui.print_list(recipe_names_conainer, RECIPES_LABELS)
