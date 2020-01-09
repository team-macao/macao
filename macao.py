import random

from launcher import launcher
from common import cards
from common.errors import *


# class Control():
#     @staticmethod
#     def check_skip(player):
#         if player.skip == 0:
#             player.is_skip = False


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
        self.num_of_player = loaded_game_data["num_of_players"]
        self.round_index = loaded_game_data["round_index"]
        self.players = loaded_game_data["players"]
        self.table = loaded_game_data["table"]

    def _new_game_init(self):
        self.game_ended = False
        self.deck = cards.generate_cards()
        self.num_of_players = self.get_num_of_players()
        self.players = []
        self.round_index = 0
        self.table = []

        self.set_up_list_of_instances_of_players()
        self.set_up_table()

    def check_if_not_empty_deck(self):
        if len(self.table) == 0:
            self.rebuild_deck()

    @staticmethod
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

    def increase_number_of_round(self, increase_value=1):
        self.round_index += increase_value

    @staticmethod
    def get_users_selection():
        is_users_selection_valid = False
        is_users_selection_compliant_with_rules = False

        while True:
            users_selection = None
            users_selection = input("Enter a valid number or letter for selected action: ")
            is_users_selection_valid = check_if_users_selection_is_valid(users_selection)
            is_users_selection_compliant_with_rules = check_if_compliant_with_rules(users_selection)
            if not is_users_selection_valid:
                continue
            elif is_users_selection_valid:
                if not is_users_selection_compliant_with_rules:
                    continue
                elif is_users_selection_compliant_with_rules:
                    return users_selection
                else:
                    raise Exception
            else:
                raise Exception

    def rebuild_deck(self):
        for card in range(len(self.table) - 1):
            self.deck.append(self.table.pop(card))

    def set_up_table(self):
        correct_card_found = False

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
            list_of_players.append(Player(number))

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
        if self.is_skip == True:
            print_information_about_being_skipped()
            self.lower_players_skip()
            return False
        elif self.is_skip == False:
            return True
        else:
            raise Exception

    def decide_if_to_lay_out_drawn_card(self):
        users_decision = input(f"Drawn card: {self.hand[-1]}\n"
                               f"put this card on the table? Y/N:").upper()
        if users_decision == "Y":
            game_data.table.append(self.hand.pop(-1))
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

    def lay_out_card(self, cards_index, table):
        table.append(self.hand.pop(cards_index - 1))

    def lower_players_skip(self):
        if self.skip == 1:
            self.skip -= 1
            self.remove_players_skip()
        elif self.skip > 1:
            self.skip -= 1
        else:
            raise Exception

    def remove_players_skip(self):
        self.is_skip = False


def main():
    launched_type_of_game = launcher.launch()
    global game_data

    if launched_type_of_game == "new":
        game_data = GameData()
        start_game()
    elif launched_type_of_game == "continue":
        pass
    else:
        raise LaucherError


def check_if_compliant_with_rules(users_selection):
    return True


def check_if_users_selection_is_valid(users_selection):
    possible_valid_selections = check_possible_valid_selections()
    if users_selection not in range(1, len(current_player.hand) + 1):
        print("Invalid selection! Selected number out of range!")
    else:
        return True


def check_possible_valid_selections():
    pass


def play(users_selection):
    pass


def print_current_game_status():
    print(f"\nRound #{game_data.round_index}: Player #{current_player.players_id}")
    print(f"\nCard on table:")
    print(f"{game_data.table[len(game_data.table) - 1]}\n")
    print("Cards on you hand:")

    for card_index, card in enumerate(current_player.hand, start=1):
        print(f"{card_index}. {repr(card)}")

    print('\nQuit - \"Q\", Draw - \"D\"\n')


def print_information_about_being_skipped():
    pass


def start_game():
    while not game_data.game_ended:
        start_round()


def start_players_move():
    can_play = current_player.check_if_possible_to_play()
    if can_play:
        print_current_game_status()
        users_selection = game_data.get_users_selection()
        try:
            users_selection_int = int(users_selection)
        except ValueError:
            pass
        else:
            play(users_selection_int)


def start_round():
    game_data.increase_number_of_round()

    global current_player

    for current_player in game_data.players:
        game_data.check_if_not_empty_deck()
        start_players_move()


def validate_card(player_card):
    results_of_validation = (player_card.rank == "Queen",
                             game_data.table[-1].rank == "Queen",
                             game_data.table[-1].rank == player_card.rank,
                             game_data.table[-1].suit == player_card.suit,
                             )

    return any(results_of_validation)


if __name__ == '__main__':
    main()
