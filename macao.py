import random

from common import cards


class Deck:
    def __init__(self):
        self.pool = cards.generate_all_cards()
        self.table = []


class Game:
    def __init__(self):
        self.game_ended = False
        self.main_deck = Deck()
        self.deck = Deck()
        self.players = []

    def start_game(self):
        def get_num_of_players():
            while True:
                try:
                    num_of_players = int(input("Input the number of players for this game: "))
                except ValueError:
                    print("You must input a number!")
                else:
                    return num_of_players

        def put_first_card_from_pool_on_table(pool, table):
            table.append(pool.pop(random.randint(0, len(pool) - 1)))

        num_of_players = get_num_of_players()
        for num in range(1, num_of_players + 1):
            self.players.append(Player(num))
        for player in self.players:
            player.draw_hand(self.deck)


        # putting first card on table:
        put_first_card_from_pool_on_table(self.deck.pool, self.deck.table)

        self._current_game(self.deck)

    def put_card_from_user_to_table(player, card_index, table):
        table.append(player.hand.pop(card_index - 1))

    def _current_game(self, deck):
        while not self.game_ended:
            for player in self.players:
                print(f"\nPlayer #{player.players_id}\n")
                print(f"\nCard on table:")
                print(f"{self.deck.table[len(self.deck.table) - 1]}\n")
                print("Cards on you hand:")
                count = 1
                for card in player.hand:
                    print(f"{count}. {repr(card)}")
                    count += 1
                users_selection = int(input("\nChoose a card to be put on the table: "))
                self.deck.table.append(player.hand.pop(users_selection-1))


class Player:
    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id

    def draw_hand(self, deck):
        for card in range(5):
            self.hand.append(deck.pool.pop(random.randint(0, len(deck.pool)-1)))
        return self.hand
