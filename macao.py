import random

from common import cards


class Deck:
    def __init__(self):
        self.cards = cards.generate_all_cards()


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

        num_of_players = get_num_of_players()
        for num in range(1, num_of_players + 1):
            self.players.append(Player(num))
        for player in self.players:
            player.draw_hand(self.deck)
        self._current_game(self.deck)

    def _current_game(self, deck):
        while not self.game_ended:
            print(f"\nCard on table: ")
            for player in self.players:
                print(f"\nPlayer #{player.players_id}\n")
                print("Cards on you hand:")
                for card in player.hand:
                    print(repr(card))
                users_selection = input("\nChoose a card to be put on the table: ")


class Player:
    def __init__(self, players_id):
        self.hand = []
        self.players_id = players_id

    def draw_hand(self, deck):
        for card in range(1, 5):
            self.hand.append(deck.cards[random.randint(0, len(deck.cards))])
        return self.hand
