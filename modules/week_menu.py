import common
import ui
from os import sys

WEEK_MENU = ('Wyświetl jadłospis', 'Dodaj jadłospis', 'Usuń jadłospis', 'Aktualizuj jadłospis*')

def start_module():
    common.common_clear()
    ui.print_menu('Menu Jadłospisów:', WEEK_MENU, 'Wróc do menu głownego')
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
