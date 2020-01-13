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
            self._loaded_game_init(kwargs["loaded_game_data"])
        except KeyError:
            self._new_game_init()

    def _loaded_game_init(self, loaded_game_data):
        self.current_player = loaded_game_data["current_player"]
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
        self.build_list_of_instances_of_players()
        self.set_up_table()

    def build_list_of_instances_of_players(self):
        list_of_players = []

        for number in range(self.num_of_players):
            list_of_players.append(Player(number + 1))

        for player in list_of_players:
            player.draw_initial_hand(self.deck)

        self.players = list_of_players

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

    def set_current_player(self, players_instance):
        self.current_player = players_instance


class Player:
    def change_players_skip(self):
        if self.skip == 1:
            self.skip -= 1
            self.is_skip = False
        elif self.skip > 1:
            self.skip -= 1
        else:
            raise Exception

    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id
        self.is_skip = False
        self.skip = 0

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

    @property
    def enumerated_hand(self):
        return enumerate(self.hand, start=1)

    def lay_out_card(self, index_of_card):
        game_data.table.append(self.hand.pop(index_of_card - 1))

    @property
    def length_of_hand(self):

        length_of_hand = len(self.hand)

        return length_of_hand

    def play(self, players_selection):
        if players_selection.isdigit():
            self.lay_out_card(int(players_selection))
        elif players_selection in static_selections:
            static_selections[players_selection]()
        else:
            raise Exception


def check_if_compliant_with_rules(players_selection):
    if players_selection.isdigit():
        selected_card = game_data.current_player.hand[int(players_selection) - 1]
        card_on_table = game_data.table[-1]

        return any(
            (selected_card.rank == "Queen",
             card_on_table.rank == "Queen",
             card_on_table.rank == selected_card.rank,
             card_on_table.suit == selected_card.suit,
             )
        )
    else:
        return True


def check_if_not_empty_deck():
    if len(game_data.table) == 0:
        game_data.rebuild_deck()


def check_if_player_can_play(current_player):
    if current_player.is_skip == True:
        print_information_about_being_skipped()
        current_player.change_players_skip()
        return False
    elif current_player.is_skip == False:
        return True
    else:
        raise Exception


def check_if_players_selection_is_valid(players_selection):
    possible_valid_selections = check_possible_valid_selections()
    if players_selection not in possible_valid_selections:
        is_players_selection_valid = False
    else:
        is_players_selection_valid = True

    return is_players_selection_valid


def check_possible_valid_selections():
    result = []

    for card_index in range(1, game_data.current_player.length_of_hand + 1):
        result.append(f"{card_index}")
    for selection in static_selections:
        result.append(selection)

    return result


def give_card():
    game_data.current_player.draw_card()


def get_valid_players_selection():
    is_players_selection_valid = False
    is_players_selection_compliant_with_rules = False
    players_selection = None

    while not is_players_selection_valid or not is_players_selection_compliant_with_rules:
        players_selection = input("Enter a valid number or letter for selected action: ").upper()

        is_players_selection_valid = check_if_players_selection_is_valid(players_selection)
        if not is_players_selection_valid:
            print("\nInvalid input!\n")
            continue
        else:
            pass

        is_players_selection_compliant_with_rules = check_if_compliant_with_rules(players_selection)
        if not is_players_selection_compliant_with_rules:
            print("\nSelected action is not compliant with the game rules!\n")
            continue
        else:
            pass

    return players_selection


def main():
    type_of_launched_game = launcher.launch(games_name=GAMES_NAME, saves_path=SAVES_PATH)

    if type_of_launched_game == "new":
        set_up_globals()
        start_game()
    elif type_of_launched_game == "continue":
        print("\nNOT YET IMPLEMENTED")
        quit_game()
    else:
        raise LaucherError


def print_current_game_status():
    print(f"\nRound #{game_data.round_index}: Player #{game_data.current_player.players_id}")
    print(f"\nCard on table:")
    print(f"{game_data.table[len(game_data.table) - 1]}\n")
    print("Cards on you hand:")

    for card_index, card in game_data.current_player.enumerated_hand:
        print(f"{card_index}. {repr(card)}")

    print('\nQuit - \"Q\", Draw - \"D\"\n')


def print_information_about_being_skipped():
    input("You cannot make a move during this round. Press enter to continue:")


def set_up_globals(**kwargs):
    global game_data

    game_data = GameData(**kwargs)


def start_game():
    while not game_data.game_ended:
        game_data.round_index += 1

        for player in game_data.players:
            check_if_not_empty_deck()
            game_data.set_current_player(player)

            if check_if_player_can_play(player):
                print_current_game_status()
                players_selection = get_valid_players_selection()
                game_data.current_player.play(players_selection)


def quit_game():
    print(f"\nQuiting {GAMES_NAME}...")
    sys.exit(0)


static_selections = {"D": give_card,
                     "Q": quit_game,
                     }

if __name__ == '__main__':
    main()
