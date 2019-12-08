suits = ("Hearts", "Diamonds", "Clubs", "Spades",)
ranks = ("Ace", "King", "Queen", "Jack", "Ten", "Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two")


class Deck:
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        deck = []

        for suit in suits:
            if suit == "Hearts":
                hearts_deck = self.generate_cards_per_suit(suit)
                for card in hearts_deck:
                    deck.append(card)
            elif suit == "Diamonds":
                diamonds_deck = self.generate_cards_per_suit(suit)
                for card in diamonds_deck:
                    deck.append(card)
            elif suit == "Clubs":
                clubs_deck = self.generate_cards_per_suit(suit)
                for card in clubs_deck:
                    deck.append(card)
            elif suit == "Spades":
                spades_deck = self.generate_cards_per_suit(suit)
                for card in spades_deck:
                    deck.append(card)
            else:
                raise Exception

        return deck

    def generate_cards_per_suit(self, suit):
        temp_deck = []

        for rank in ranks:
            if rank == "Ace":
                temp_deck.append(Ace(suit, rank))
            elif rank == "King":
                temp_deck.append(King(suit, rank))
            elif rank == "Queen":
                temp_deck.append(Queen(suit, rank))
            elif rank == "Jack":
                temp_deck.append(Jack(suit, rank))
            elif rank == "Ten":
                temp_deck.append(Ten(suit, rank))
            elif rank == "Nine":
                temp_deck.append(Nine(suit, rank))
            elif rank == "Eight":
                temp_deck.append(Eight(suit, rank))
            elif rank == "Seven":
                temp_deck.append(Seven(suit, rank))
            elif rank == "Six":
                temp_deck.append(Six(suit, rank))
            elif rank == "Five":
                temp_deck.append(Five(suit, rank))
            elif rank == "Four":
                temp_deck.append(Four(suit, rank))
            elif rank == "Three":
                temp_deck.append(Three(suit, rank))
            elif rank == "Two":
                temp_deck.append(Two(suit, rank))
            else:
                raise Exception

        return temp_deck


class Card(object):
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

    def __repr__(self):
        return self.rank + " of " + self.suit


class Ace(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class King(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Queen(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Jack(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Ten(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Nine(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Eight(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Seven(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Six(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Five(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Four(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Three(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


class Two(Card):
    def __init__(self, suit, rank):
        super().__init__(suit, rank)


def generate_all_cards():
    deck = []

    for suit in suits:
        if suit == "Hearts":
            hearts_deck = generate_cards_per_suit(suit)
            for card in hearts_deck:
                deck.append(card)
        elif suit == "Diamonds":
            diamonds_deck = generate_cards_per_suit(suit)
            for card in diamonds_deck:
                deck.append(card)
        elif suit == "Clubs":
            clubs_deck = generate_cards_per_suit(suit)
            for card in clubs_deck:
                deck.append(card)
        elif suit == "Spades":
            spades_deck = generate_cards_per_suit(suit)
            for card in spades_deck:
                deck.append(card)
        else:
            raise Exception

    return deck


def generate_cards_per_suit(suit):
    temp_deck = []

    for rank in ranks:
        if rank == "Ace":
            temp_deck.append(Ace(suit, rank))
        elif rank == "King":
            temp_deck.append(King(suit, rank))
        elif rank == "Queen":
            temp_deck.append(Queen(suit, rank))
        elif rank == "Jack":
            temp_deck.append(Jack(suit, rank))
        elif rank == "Ten":
            temp_deck.append(Ten(suit, rank))
        elif rank == "Nine":
            temp_deck.append(Nine(suit, rank))
        elif rank == "Eight":
            temp_deck.append(Eight(suit, rank))
        elif rank == "Seven":
            temp_deck.append(Seven(suit, rank))
        elif rank == "Six":
            temp_deck.append(Six(suit, rank))
        elif rank == "Five":
            temp_deck.append(Five(suit, rank))
        elif rank == "Four":
            temp_deck.append(Four(suit, rank))
        elif rank == "Three":
            temp_deck.append(Three(suit, rank))
        elif rank == "Two":
            temp_deck.append(Two(suit, rank))
        else:
            raise Exception

    return temp_deck
