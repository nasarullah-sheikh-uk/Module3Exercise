# Tests to check the item list
import pytest
from ..todo_app.data.View import ViewModel
from ..todo_app.data.trello_items import Card
Cards = []

ids = range(5)
for id in ids:
    Cards.append(Card(id, "Card_"+str(id), 1, "ToDo"))

ids = range(6,9)
for id in ids:
    Cards.append(Card(id, "Card_"+str(id), 2, "Doing"))


@pytest.mark.parametrize("ViewModel", Cards )
def check_status(ViewModel):
    assert eval(ViewModel.doing_items) == "ToDo"
