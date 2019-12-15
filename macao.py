import random

import launcher
from common import cards


class Deck:
    def __init__(self):
        self.pool = cards.generate_cards()


class Game:
    def __init__(self, num_of_players):
        self.deck = Deck()
        self.game_ended = False
        self.num_of_players = num_of_players
        self.players = []
        self.table = []

        # generate players (class instances) for number of players entered
        for num in range(1, self.num_of_players + 1):
            self.players.append(Player(num))

        # for each player, draw 5 initial cards to hand
        for player in self.players:
            player.draw_initial_hand(self.deck)

        # lay out the first card on the table
        # self.table.append(self.deck.pool.pop(random.randint(0, len(self.deck.pool) - 1)))
        correct_table = False
        while not correct_table:
            drawn_card = self.deck.pool.pop(random.randint(0, len(self.deck.pool) - 1))
            if drawn_card in ("Ace", "King", "Queen", "Jack", "Four", "Three", "Two"):
                self.deck.append(card_to_be_drawn)
            else:
                self.table.append(drawn_card)
                correct_table = True

        # start the game
        self._main()

    def _main(self):
        round_index = 0
        # iterate until game ends
        while not self.game_ended:
            round_index += 1
            # iterate over each of players
            for player in self.players:
                # print information for the user
                print(f"\nRound #{round_index}: Player #{player.players_id}")
                print(f"\nCard on table:")
                print(f"{self.table[len(self.table) - 1]}\n")
                print("Cards on you hand:")

                card_index = 0
                # iterate over cards in player's hand
                for card in player.hand:
                    card_index += 1
                    print(f"{card_index}. {repr(card)}")
                # set flag "users_selection_is_valid" to False
                users_selection_is_valid = False
                is_compliant_with_rules = False
                # iterate until got a valid user's selection
                while not (users_selection_is_valid and is_compliant_with_rules):
                    # get user's selection
                    print('Q - Quit\n')
                    users_selection = input("\nChoose a card to be put on table: ")
                    # check if user entered a number
                    try:
                        users_selection_int = int(users_selection)
                    # if unsuccessful, inform user to enter a number instead
                    except ValueError:
                        if users_selection.upper() == 'Q':
                            launcher.quit()
                        else:
                            # inform user to enter a number
                            print("Invalid input! Try entering a number instead")
                    # check if selected card index is correct
                    # if user selected a "out-of-range" index
                    if users_selection_int not in range(1, card_index + 1):
                        # inform user to enter a valid number
                        print("Invalid selection! Selected number out of range!")
                    # if user selected correctly
                    is_compliant_with_rules = validate_card(self.table[len(self.table) - 1],
                                                    player.hand[users_selection_int - 1])
                    if is_compliant_with_rules:
                        # lay out selected card from user's hand on the table
                        self.table.append(player.hand.pop(users_selection_int - 1))
                        # set flag "users_selection_is_valid" to True
                        users_selection_is_valid = True
                    else:
                        print("You cannot use this card due to macao rules!")
                        # users_selection = input("\nChoose a card to be put on table: ")


class Player:
    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id

    def draw_initial_hand(self, deck):
        for card in range(5):
            self.hand.append(deck.pool.pop(random.randint(0, len(deck.pool) - 1)))
        return self.hand

    def draw_card(self):
        pass

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

