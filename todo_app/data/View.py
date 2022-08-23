class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items
    
    @property
    def doing_items(self):
        self.d_items = []
        for i in self._items['allcards']:
            if i.status == "Doing":
                self.d_items.append(i)
        return self.d_items
    
    @property
    def done_items(self):
        self.d_items = []
        for i in self._items['allcards']:
            if i.status == "Done":
                self.d_items.append(i)
        return self.d_items

    @property
    def todo_items(self):
        self.d_items = []
        for i in self._items['allcards']:
            if i.status == "To Do":
                self.d_items.append(i)
        return self.d_items