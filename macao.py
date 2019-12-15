import random

import launcher
from common import cards


class Game:
    def __init__(self, num_of_players):
        self.deck = cards.generate_cards()
        self.is_action_underway = False
        self.is_game_over = False
        self.num_of_players = num_of_players
        self.other_selections = ["D", "Q", "S"]
        self.players = []
        self.table = []

        for id in range(1, self.num_of_players + 1):
            self.players.append(Player(id))

        for player in self.players:
            player.draw_initial_hand(self.deck)

        is_first_card_correct = False
        while not is_first_card_correct:
            random_card = self.deck.pop(random.randint(0, len(self.deck) - 1))
            if random_card.rank in cards.INACTIVE_CARDS:
                is_first_card_correct = True
                self.table.append(random_card)

        self._main()

    def _main(self):
        round_index = 0
        while not self.is_game_over:
            round_index += 1
            for player in self.players:
                print(f"\nRound #{round_index}: Player #{player.players_id}")
                print(f"\nCard on table:")
                print(f"{self.table[- 1]}\n")
                print("Cards on you hand:")
                for card_index, card in enumerate(player.hand):
                    print(f"{card_index + 1}. {repr(card)}")
                is_players_move_valid = False
                while not is_players_move_valid:
                    users_selection = get_users_selection()
                    valid_selection = validate_users_selection(users_selection, player.hand, self.other_selections)
                    is_players_move_valid = validate_players_move(player.hand, valid_selection, self.table)
                    if is_players_move_valid:
                        self.table.append(player.hand.pop(valid_selection - 1))
                    else:
                        print("Not possible to lay out this card due to Macao rules!")

class Player:
    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id

    def draw_initial_hand(self, deck):
        for card in range(5):
            self.hand.append(deck.pop(random.randint(0, len(deck) - 1)))
        return self.hand

    def draw_card(self):
        pass

    def lay_out_card(self, cards_index, player, table):
        table.append(player.hand.pop(cards_index - 1))


def get_users_selection():
    print("\n\"D\" - Draw, \"Q\" - Quit, \"S\" - Save")
    users_selection = input("Enter your selection: ")
    return users_selection


def validate_users_selection(users_selection, players_hand, other_selections):
    is_users_selection_valid = False
    while not is_users_selection_valid:
        try:
            int_users_selection = int(users_selection)
        except ValueError:
            if users_selection in other_selections:
                is_users_selection_valid = True
            else:
                print("Invalid input!")
        else:
            if int_users_selection not in range(1, len(players_hand) + 2):
                print("Invalid selection! Selected number out of range!")
            else:
                return int_users_selection


def validate_players_move(players_hand, users_selection, table):
    results = []
    results.append(table[-1].rank == players_hand[users_selection - 1].rank)
    results.append(table[-1].suit == players_hand[users_selection - 1].suit)
    results.append(table[-1].rank == "Queen")
    results.append(players_hand[users_selection - 1].rank == "Queen")
    return any(results)
