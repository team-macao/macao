import sys

import macao

GAME_NAME = "Macao"
SAVES_PATH = "saved_games/"


def main():
    print_menu()
    valid_users_selection = get_valid_users_selection()
    select_valid_menu_option(valid_users_selection)


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
    pass


def new_game():
    num_of_players = get_num_of_players()
    macao.Game(num_of_players)


def get_num_of_players():
    while True:
        try:
            num_of_players = int(input("\nEnter number of players for this game: "))
        except ValueError:
            print("Invalid input! Try entering a number instead!\n")
        else:
            if num_of_players not in range(2, 5):
                print("Invalid selection! Number of players must be between 2 to 4 players!")
            else:
                return num_of_players


def quit_program():
    print(f"\nQuiting {GAME_NAME}...")
    sys.exit(0)


if __name__ == '__main__':
    main()
