import pickle

class Catalog:
    """
    Represents a catalog system for managing library items.
    Provides methods to add, remove, search, and persist library items using pickle serialization.
    """
    def __init__(self, name):
        """
        Initialize a new Catalog instance.
        Args:
            name (str): The name of the catalog
        Attributes:
            name (str): The catalog's name
            _items (list): A private list to store library items
        """
        self.name = name
        self._items = []
    
    def add_items(self, items):
        """
        Add multiple items to the catalog, avoiding duplicates.
        Args:
            items (list): A list of items to be added to the catalog
        Items that already exist in the catalog will be skipped
        """
        for item in items:
            if item not in self._items:
                self._items.append(item)
    
    def remove_items(self, items):
        """
        Remove multiple items from the catalog.
        Args:
            items (list): A list of items to be removed from the catalog
        Only items present in the catalog will be removed
        """
        for item in items:
            if item in self._items:
                self._items.remove(item)
    
    def search_items(self, query, item_type=None):
        """
        Search for items in the catalog based on a query and optional type filter.
        Args:
            query (str): The search term to match against item attributes
            item_type (type, optional): A specific item type to filter results 
        Returns:
            list: A list of items matching the search criteria
        Searches across all attributes of items using case-insensitive matching
        """
        results = []
        for item in self._items:
            if item_type and not isinstance(item, item_type):
                continue
            if any(query.lower() in str(getattr(item, attr)).lower() for attr in vars(item)):
                results.append(item)
        return results
    
    def save_as_pickle(self):
        """
        Save the catalog items to a pickle file.
        Serializes the catalog's items list to 'catalog.pkl' using pickle.
        Overwrites the existing 'catalog.pkl' file if it exists
        """
        with open("catalog.pkl", "wb") as f:
            pickle.dump(self._items, f)
    
    def load_from_pickle(self):
        """
        Load catalog items from a pickle file.
        Deserializes items from 'catalog.pkl' and replaces the current catalog's items.
        Assumes 'catalog.pkl' exists and contains a valid pickled list of items
        """
        with open("catalog.pkl", "rb") as f:
            self._items = pickle.load(f)
