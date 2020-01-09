import sys

import macao

GAME_NAME = "Macao"
SAVES_PATH = "saved_games/"


def launch():
    print_menu()
    valid_users_selection = get_valid_users_selection()
    select_valid_menu_option(valid_users_selection)
    return result


def print_menu():
    print(f"\n{GAME_NAME}\n")
    print("1. Continue last game")
    print("2. New game")
    print("3. Quit\n")


def get_valid_users_selection():
    is_users_selection_valid = False
    valid_users_selection = None

    while not is_users_selection_valid:
        users_selection = input("Enter a valid number from menu for your selection: ")
        is_users_selection_valid, valid_users_selection = validate_users_selection(users_selection)
    return valid_users_selection


def validate_users_selection(users_selection):
    validated_users_selection = None
    is_users_selection_valid = False
    try:
        users_selection_int = int(users_selection)
    except ValueError:
        print("Invalid input! Try entering a number instead\n")
    else:
        if users_selection_int not in range(1, 4):
            print("Invalid selection! Possible selections between 1 to 3!\n")
        else:
            validated_users_selection = users_selection_int
            is_users_selection_valid = True

    return is_users_selection_valid, validated_users_selection


def select_valid_menu_option(valid_users_selection):
    menu_options = {1: continue_last_game,
                    2: new_game,
                    3: quit_program, }

    menu_options[valid_users_selection]()


def continue_last_game():
    global result
    result = "continue"


def new_game():
    global result
    result = "new"


def quit_program():
    print(f"\nQuiting {GAME_NAME}...")
    sys.exit(0)
