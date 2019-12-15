import sys

import macao

GAME_NAME = "Macao"
SAVES_PATH = "saved_games/"


class MainMenu:
    def __init__(self):
        self.menu_options = {1: continue_last_game,
                             2: new_game,
                             3: quit, }

    def main(self):
        self._print_menu()
        self.is_users_selection_valid = False
        while not self.is_users_selection_valid:
            self.users_selection = self.get_users_selection()
            self.is_users_selection_valid, self.valid_users_selection = self.validate_users_selection()
        self._select_valid_menu_option()

    def _print_menu(self):
        print(f"\n{GAME_NAME}\n")
        print("1. Continue last game")
        print("2. New game")
        print("3. Exit game\n")

    def _select_valid_menu_option(self):
        self.menu_options[self.valid_users_selection]()

    def get_users_selection(self):
        users_selection = input("Enter a valid number for your selection: ")
        return users_selection

    def validate_users_selection(self):
        try:
            users_selection_int = int(self.users_selection)
        except ValueError:
            print("\nInvalid input! Try entering a number instead")
            return False, None
        else:
            if users_selection_int not in range(1, 4):
                print("\nInvalid selection! Possible number of users playing between 2 to 4!")
                return False, None
            else:
                valid_users_selection = users_selection_int
                return True, valid_users_selection


def continue_last_game():
    pass


def new_game():
    def get_num_of_players():
        while True:
            try:
                num_of_players = int(input("\nEnter number of players for this game: "))
            except ValueError:
                print("\nInvalid input! Try entering a number instead")
            else:
                if num_of_players not in range(2, 5):
                    print("\nInvalid selection! Number of players must be between 2 to 4 players!")
                else:
                    return num_of_players

    num_of_players = get_num_of_players()

    macao.Game(num_of_players)


def quit():
    print(f"\nQuiting {GAME_NAME}...")
    sys.exit(0)


if __name__ == '__main__':
    MainMenu().main()
