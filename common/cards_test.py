from common.cards import Card


def test_create_obj_card():
    obj = Card("Hearts", "Ace")
    assert obj.__str__() == "Ace of Hearts"


