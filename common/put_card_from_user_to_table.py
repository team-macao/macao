
def put_card_from_user_to_table(player, card_index, table):
    table.append(player.hand.pop(card_index-1))
