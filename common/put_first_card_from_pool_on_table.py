import random

def put_first_card_from_pool_on_table(pool, table):
    table.append(pool.pop(random.randint(0, len(pool)-1)))


