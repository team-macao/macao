import macao

GAME_NAME = "Macao"
SAVES_PATH = "saved_games/"


class MainMenu:
    def main(self):
        self._print_menu()
        users_selection = users_selection_validation()
        self.select_valid_game_options(users_selection)

    def _print_menu(self):
        print(f"\n{GAME_NAME}\n")
        print("1. Continue last game")
        print("2. New game")
        print("3. Saved games")
        print("4. Exit game")

    def select_valid_game_options(self, users_selection):
        if users_selection <= 0 or users_selection >= 5:
            self.invalid_selection()
        elif users_selection == 1:
            self.continue_the_last_game()
        elif users_selection == 2:
            self.new_game()
        elif users_selection == 3:
            self.saved_games()
        elif users_selection == 4:
            self.quit_game()

    def invalid_selection(self):
        print("\nInvalid selection!")
        self.main()

    def continue_the_last_game(self):
        pass

    def new_game(self):
        macao.Game().start_game()

    def saved_games(self):
        SavesMenu().main()

    def quit_game(self):
        print(f"\nQuiting {GAME_NAME}...")


def users_selection_validation():
    while True:
        try:
            users_selection = int(input("\nYour selection: "))
        except ValueError:
            print("You must input a number!")
        else:
            return users_selection


if __name__ == '__main__':
    MainMenu().main()
