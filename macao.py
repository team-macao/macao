import random

from common import cards


class Deck:
    def __init__(self):
        self.pool = cards.generate_all_cards()


class Game:
    def __init__(self, num_of_players):
        self.deck = Deck()
        self.game_ended = False
        self.num_of_players = num_of_players
        self.players = []
        self.table = []

        # generate players (class instances) for number of players inputted
        for num in range(1, self.num_of_players + 1):
            self.players.append(Player(num))

        # for each player, draw 5 inital cards to hand
        for player in self.players:
            player.draw_initial_hand(self.deck)

        # lay out the first card on the table
        self.table.append(self.deck.pool.pop(random.randint(0, len(self.deck.pool) - 1)))

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
                # set flag "users_selection_valid" to False
                users_selection_valid = False
                # iterate until got a valid user's selection
                while not users_selection_valid:
                    # get user's selection
                    users_selection = input("\nChoose a card to be put on the table: ")
                    # check if user entered a number
                    try:
                        users_selection_int = int(users_selection)
                    # if unsuccessful, inform user to enter a number instead
                    except ValueError:
                        # inform user to input a number
                        print("Invalid input! Try entering a number instead")
                    # check if selected card index is correct
                    else:
                        # if user selected a "out-of-range" index
                        if users_selection_int not in range(1, card_index + 1):
                            # inform user to input a valid number
                            print("Invalid selection! Selected number out of range!")
                        # if user selected correctly
                        else:
                            # lay out selected card from user's hand on the table
                            self.table.append(player.hand.pop(users_selection_int - 1))
                            # set flag "users_selection_valid" to True
                            users_selection_valid = True


class Player:
    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id

    def draw_initial_hand(self, deck):
        for card in range(5):
            self.hand.append(deck.pool.pop(random.randint(0, len(deck.pool) - 1)))
        return self.hand

    def draw_a_card(self):
        pass

    def lay_out_card(self, cards_index, player, table):
        table.append(player.hand.pop(cards_index - 1))
