class Catalog:
    def __init__(self,name):
        self.name = name
        self.items = []

    def add_library_item (self, item_added):
        self.items.append(item_added)
    
    def remove_library_item (self, item_removed):
        try:
            self.items.pop(self, item_removed)
        except:
            print("Item not in catalog")
    
    def search ():
        pass