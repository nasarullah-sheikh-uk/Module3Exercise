# Tests to check the item list
import pytest
from todo_app.data.View import ViewModel
from todo_app.data.trello_items import Card, get_cards, add_card, update_card

Cards = []

ids = range(5)
for id in ids:
    Cards.append(Card(id, "Card_"+str(id), 1, "Doing"))

items = { 'allcards': Cards } # because the main code returns a Dict of all cards and all lists
item_view_model=ViewModel(items)

def test_check_doing():
    for s in item_view_model.doing_items:
        print (s.name, s.status)
        assert s.status == "Doing"
