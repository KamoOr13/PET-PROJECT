import common
import ui
from os import sys

RECIPES_MENU = ('Szczegóły przepisu', 'Dodaj przepis', 'Usuń przepis')
def start_module():
    common.common_clear()
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
