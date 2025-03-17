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
        with open("catalog.pkl", "w") as f :
            f.write(pickle.dumps(self._items))

    def load_from_pickle(self):
        with open("catalog.pkl", "r") as f:
            self._items = 



# """"Why are we calling the base class?"""
# # class LibraryItem:
# #     def __init__(self, title, author):
# #         self.title = title
# #         self.author = author

# class Book(AbstractLibraryItem):
#     def __init__(self, title, author, isbn):
#         super().__init__(title, author)
#         self.isbn = isbn

# class DVD(AbstractLibraryItem):
#     def __init__(self, title, director, duration):
#         super().__init__(title, director)
#         self.duration = duration
