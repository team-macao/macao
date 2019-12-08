import copy
import random

from common import cards

main_deck = cards.generate_deck()


def main(num_of_players):
    game_ended = False

    # players_decks - lista list kart każdego z graczy
    # pcs_deck - lista kart komputera
    # used_cards_ids - lista indeksów kart wyjętych z głównej talii
    players_decks, pcs_deck, used_cards_ids, = draw_decks_per_the_num_of_players(num_of_players)

    while not game_ended:
        print(f"\nCard on table: {repr(main_deck[used_cards_ids[-1]])}")
        for player_id in range(num_of_players):
            print(f"\nPlayer #{player_id+1}")
            print("Cards on you hand:")
            try:
                cards_id = 0
                for card in players_decks[player_id]:
                    cards_id += 1
                    print(f"{cards_id}. {repr(card)}")
            except Exception:
                pass

            try:
                players_move = input("\nPlease select which card to be put on the table: ")
            except Exception:
                pass


def draw_decks_per_the_num_of_players(num_of_players):
    used_cards_ids = []
    players_decks = []
    for num in range(num_of_players):
        temp_players_deck, used_cards_ids = draw_deck(used_cards_ids)
        players_decks.append(temp_players_deck)
    pcs_deck, used_cards_ids = draw_deck(used_cards_ids)

    return players_decks, pcs_deck, used_cards_ids


def draw_deck(used_cards_ids):
    players_deck = []
    counter = 0

    temp_used_cards_ids = used_cards_ids

    while counter < 5:
        cards_id = random.randint(0, 51)
        if cards_id not in temp_used_cards_ids:
            counter += 1
            temp_used_cards_ids.append(cards_id)
            players_deck.append(main_deck[cards_id])
        else:
            continue

    return players_deck, temp_used_cards_ids
