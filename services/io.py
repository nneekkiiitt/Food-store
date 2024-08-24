from enum import Enum


class MenuOptions(Enum):
    PURCHASE_MENU = 1
    PRINT_PURCHASE_HISTORY = 2
    PRINT_MONEY_IN_ACCOUNT = 3
    EXIT = 4


def get_menu_option() -> MenuOptions:
    option = input(
        "Please choose an option from the menu options list:\n1. Go to purchase menu\n2. Print purchase history\n"
        "3. Print money from account\n4. Exit\n"
    )
    if option != "1" and option != "2" and option != "3" and option != "4":
        print("Invalid option selected!")
        return get_menu_option()
    options_map = {
        "1": MenuOptions.PURCHASE_MENU,
        "2": MenuOptions.PRINT_PURCHASE_HISTORY,
        "3": MenuOptions.PRINT_MONEY_IN_ACCOUNT,
        "4": MenuOptions.EXIT,
    }
    return options_map[option]