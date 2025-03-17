import pickle

class Catalog:
    def __init__(self, name):
        self.name = name
        self._items = []

    def add_items(self, items):
        for item in items:
            if item not in self._items:
                self._items.append(item)

    def remove_items(self, items):
        for item in items:
            if item in self._items:
                self._items.remove(item)

    def search_items(self, query, item_type=None):
        results = []
        for item in self._items:
            if item_type and not isinstance(item, item_type):
                continue
            if any(query.lower() in str(getattr(item, attr)).lower() for attr in vars(item)):
                results.append(item)
        return results
    
    def save_as_pickle(self):
        with open("catalog.pkl", "wb") as f :
            pickle.dump(self._items, f)

    def load_from_pickle(self):
        with open("catalog.pkl", "rb") as f:
            self._items = pickle.load(f)



