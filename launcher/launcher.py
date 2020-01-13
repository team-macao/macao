import sys


class InternalLauncherError(Exception):
    pass


def continue_last_game():
    global result

    result = "continue"


def get_valid_users_selection():
    is_users_selection_valid = False
    valid_users_selection = None

    while not is_users_selection_valid:
        users_selection = input("Enter a valid number from menu for your selection: ")
        is_users_selection_valid, valid_users_selection = validate_users_selection(users_selection)

    return valid_users_selection


def launch(saves_path, games_name="NO GAME NAME GIVEN"):
    set_globals(games_name, saves_path)

    try:
        main()
    except Exception:
        raise InternalLauncherError
    else:
        return result


def main():
    print_menu()

    valid_users_selection = get_valid_users_selection()

    select_valid_menu_option(valid_users_selection)


def new_game():
    global result

    result = "new"


def print_menu():
    print(f"\n{GAMES_NAME}\n")
    print("1. Continue last game")
    print("2. New game")
    print("3. Quit\n")


def select_valid_menu_option(valid_users_selection):
    menu_options[valid_users_selection]()


def set_globals(games_name, saves_path):
    global GAMES_NAME, SAVES_PATH

    GAMES_NAME = games_name
    SAVES_PATH = saves_path


def validate_users_selection(users_selection):
    validated_users_selection = None
    is_users_selection_valid = False

    try:
        users_selection_int = int(users_selection)
    except ValueError:
        print("Invalid input! Try entering a number instead\n")
    else:
        if users_selection_int not in menu_options:
            print("Invalid selection! Possible selections between 1 to 3!\n")
        else:
            validated_users_selection = users_selection_int
            is_users_selection_valid = True

    return is_users_selection_valid, validated_users_selection


def quit_launcher():
    print(f"\nQuiting launcher...")
    sys.exit(0)


menu_options = {1: continue_last_game,
                2: new_game,
                3: quit_launcher,
                }
