import random

import launcher
from common import cards


class Game:
    def __init__(self, num_of_players):
        self.deck = cards.generate_cards()
        self.game_ended = False
        self.num_of_players = num_of_players
        self.players = []
        self.round_index = 0
        self.table = []

        # generate players (class instances) for number of players entered
        for num in range(1, self.num_of_players + 1):
            self.players.append(Player(num))

        # for each player, draw 5 initial cards to hand
        for player in self.players:
            player.draw_initial_hand(self.deck)

        correct_table = False
        while not correct_table:
            drawn_card = self.deck.pop(random.randint(0, len(self.deck) - 1))
            if drawn_card.rank in ("Ace", "King", "Queen", "Jack", "Four", "Three", "Two"):
                self.deck.append(drawn_card)
            else:
                self.table.append(drawn_card)
                correct_table = True

        # start the game
        self._main()

    def _main(self):
        def print_current_game_status(self, player):
            print(f"\nRound #{self.round_index}: Player #{player.players_id}")
            print(f"\nCard on table:")
            print(f"{self.table[len(self.table) - 1]}\n")
            print("Cards on you hand:")

            for card_index, card in enumerate(player.hand, start=1):
                print(f"{card_index}. {repr(card)}")

        while not self.game_ended:
            self.round_index += 1
            for player in self.players:
                control.check_skip(player)
                print_current_game_status(self, player)
                users_selection_is_valid = False
                is_compliant_with_rules = False
                while not (users_selection_is_valid and is_compliant_with_rules):
                    print('\nQ - Quit\n')
                    users_selection = input("\nChoose a card to be put on table or draw card press 'D': ")
                    if not users_selection.isdigit():
                        self.control(users_selection, player, self.deck)
                        break
                    else:
                        try:
                            users_selection_int = int(users_selection)
                        except ValueError:
                            print("Invalid input! Try entering a number instead")
                        else:
                            if users_selection_int not in range(1, len(player.hand) + 1):
                                print("Invalid selection! Selected number out of range!")
                    is_compliant_with_rules = validate_card(self.table[len(self.table) - 1],
                                                            player.hand[users_selection_int - 1])
                    if is_compliant_with_rules:
                        self.table.append(player.hand.pop(users_selection_int - 1))
                        users_selection_is_valid = True
                    else:
                        print("You cannot use this card due to macao rules!")

    def get_valid_users_selection(self):
        pass

    def validate_users_selection(self):
        pass

    def control(self, users_selection, player, deck):
        control_switches = {
            'Q': launcher.quit_program,
            'D': player.draw_card,
        }
        control_switches[users_selection.upper()](deck)

    def show_draw_card(self):
        print(player.hand[-1])
        pass

class control():
    @staticmethod
    def check_skip(player):
        if player.skip == 0:
            player.is_skip = False

class Player:
    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id
        self.is_skip = False
        self.skip = 0

    def draw_initial_hand(self, deck):
        for card in range(5):
            self.hand.append(deck.pop(random.randint(0, len(deck) - 1)))
        return self.hand

    def draw_card(self, deck):
        self.hand.append(deck.pop(random.randint(0, len(deck) - 1)))

    def lay_out_card(self, cards_index, player, table):
        table.append(player.hand.pop(cards_index - 1))


def validate_card(table_card, player_card):
    return any(
        (table_card.rank == "Queen",
         player_card.rank == "Queen",
         table_card.rank == player_card.rank,
         table_card.suit == player_card.suit,
         )
    )
