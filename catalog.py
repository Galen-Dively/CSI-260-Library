import LibraryItem

class Catalog:
    def __init__(self,name):
        self.name = name
        self.items = []

    def add_library_item (self, item_added: LibraryItem):
        self.items.append(item_added)
    
    def remove_library_item (self, item_removed: LibraryItem):
        try:
            self.items.pop(self, item_removed)
        except:
            print("Item not in catalog")
    
    def search (self,name,isbn,tag):
        temp_results =[]
        for i in self.items:
            if i.name == name:
                temp_results.append(i)
            elif i.isbn == isbn:
                temp_results.append(i)
            elif i.tags == tag:
                temp_results.append(i)
        if len(temp_results) == 0:
            return("No items found with these filters")
        else:
            return(f"{len(temp_results)} Items found:\n{[str(i) for i in temp_results]}")