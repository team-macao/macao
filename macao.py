import random
import sys

from launcher import launcher
from common import cards
from common.errors import *

GAMES_NAME = "Macao"
SAVES_PATH = "saved_games/"


class GameData:
    def __init__(self, **kwargs):
        try:
            loaded_game_data = kwargs["loaded_game_data"]
        except KeyError:
            self._new_game_init()
        else:
            self._loaded_game_init(loaded_game_data)

    def _loaded_game_init(self, loaded_game_data):
        self.game_ended = loaded_game_data["game_ended"]
        self.deck = loaded_game_data["game_ended"]
        self.num_of_players = loaded_game_data["num_of_players"]
        self.round_index = loaded_game_data["round_index"]
        self.players = loaded_game_data["players"]
        self.table = loaded_game_data["table"]

    def _new_game_init(self):
        self.game_ended = False
        self.deck = cards.generate_cards()
        self.round_index = 0

        self.get_num_of_players()
        self.set_up_list_of_instances_of_players()
        self.set_up_table()

    def check_if_not_empty_deck(self):
        if len(self.table) == 0:
            self.rebuild_deck()

    def get_num_of_players(self):
        while True:
            try:
                num_of_players = int(input("\nEnter number of players for this game: "))
            except ValueError:
                print("Invalid input! Try entering a number instead!\n")
            else:
                if num_of_players not in range(2, 5):
                    print("Invalid selection! Number of players must be between 2 to 4 players!")
                else:
                    break

        self.num_of_players = num_of_players

    def rebuild_deck(self):
        for card in range(len(self.table) - 1):
            self.deck.append(self.table.pop(card))

    def set_up_table(self):
        correct_card_found = False

        self.table = []

        while not correct_card_found:
            found_card_index = random.randint(0, len(self.deck) - 1)
            if self.deck[found_card_index].rank in cards.RANKS[4:-4]:
                self.table.append(self.deck.pop(found_card_index))
                correct_card_found = True
            else:
                pass

    def set_up_list_of_instances_of_players(self):
        list_of_players = []

        for number in range(self.num_of_players):
            list_of_players.append(Player(number + 1))

        for player in list_of_players:
            player.draw_initial_hand(self.deck)

        self.players = list_of_players


class Player:
    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id
        self.is_skip = False
        self.skip = 0

    def check_if_possible_to_play(self):
        print("ok")
        if self.is_skip == True:
            print_information_about_being_skipped()
            self.change_players_skip()
            return False
        elif self.is_skip == False:
            return True
        else:
            raise Exception

    def decide_if_to_lay_out_drawn_card(self):
        users_decision = input(f"Drawn card: {self.hand[-1]}\n"
                               f"put this card on the table? Y/N:").upper()
        if users_decision == "Y":
            self.lay_out_card(-1)
        elif users_decision == "N":
            pass
        else:
            raise Exception

    def draw_initial_hand(self, deck):
        for card in range(5):
            self.hand.append(deck.pop(random.randint(0, len(deck) - 1)))
        return self.hand

    def draw_card(self):
        self.hand.append(game_data.deck.pop(random.randint(0, len(game_data.deck) - 1)))

    def lay_out_card(self, index_of_card):
        game_data.table.append(self.hand.pop(index_of_card - 1))

    @property
    def length_of_hand(self):

        length_of_hand = len(self.hand)

        return length_of_hand

    @property
    def enumerated_hand(self):
        return enumerate(self.hand, start=1)

    def change_players_skip(self):
        if self.skip == 1:
            self.skip -= 1
            self.is_skip = False
        elif self.skip > 1:
            self.skip -= 1
        else:
            raise Exception


def check_if_compliant_with_rules(users_selection):
    return True


def check_if_users_selection_is_valid(users_selection):
    possible_valid_selections = check_possible_valid_selections()
    if users_selection not in possible_valid_selections:
        is_players_selection_valid = False
    else:
        is_players_selection_valid = True

    return is_players_selection_valid


def check_possible_valid_selections():
    result = []

    for card_index in range(1, current_player.length_of_hand + 1):
        result.append(f"{card_index}")
    for selection in static_selections:
        result.append(selection)

    return result


def get_users_selection():
    while True:
        users_selection = input("Enter a valid number or letter for selected action: ").upper()
        is_users_selection_valid = check_if_users_selection_is_valid(users_selection)
        is_users_selection_compliant_with_rules = check_if_compliant_with_rules(users_selection)
        if not is_users_selection_valid:
            print("Invalid input!\n")
        elif is_users_selection_valid:
            if not is_users_selection_compliant_with_rules:
                print("Selected action is not compliant with the game rules!")
            elif is_users_selection_compliant_with_rules:
                break
            else:
                raise Exception
        else:
            raise Exception

    return users_selection


def give_player_card():
    current_player.draw_card()


def lay_out_card(index_of_selected_card):
    game_data.table.append(current_player.hand.pop(index_of_selected_card - 1))


def main():
    launched_type_of_game = launcher.launch(games_name=GAMES_NAME, saves_path=SAVES_PATH)
    global game_data

    if launched_type_of_game == "new":
        game_data = GameData()
        start_game()
    elif launched_type_of_game == "continue":
        pass
    else:
        raise LaucherError


def play(users_selection):
    pass


def print_current_game_status():
    print(f"\nRound #{game_data.round_index}: Player #{current_player.players_id}")
    print(f"\nCard on table:")
    print(f"{game_data.table[len(game_data.table) - 1]}\n")
    print("Cards on you hand:")

    for card_index, card in current_player.enumerated_hand:
        print(f"{card_index}. {repr(card)}")

    print('\nQuit - \"Q\", Draw - \"D\"\n')


def print_information_about_being_skipped():
    input("You cannot make a move during this round. Press enter to continue.")


def start_game():
    while not game_data.game_ended:
        start_round()


def start_players_move():
    can_play = current_player.check_if_possible_to_play()

    if can_play:
        print_current_game_status()
        users_selection = get_users_selection()
        try:
            users_selection_int = int(users_selection)
        except ValueError:
            if users_selection in static_selections:
                static_selections[users_selection]()
            else:
                raise Exception
        else:
            current_player.lay_out_card(users_selection_int)


def start_round():
    game_data.round_index += 1

    global current_player

    for current_player in game_data.players:
        game_data.check_if_not_empty_deck()
        start_players_move()


def quit_program():
    print(f"\nQuiting {GAMES_NAME}...")
    sys.exit(0)


static_selections = {"D": give_player_card,
                     "Q": quit_program,
                     }

if __name__ == '__main__':
    main()
