"""
Library Catalog Management Application

This script provides a command-line interface for managing a library catalog.
Users can:
- Search for items
- View the entire catalog
- Add new items (books, CDs, video games)
- Remove items
- Save and load the catalog using pickle serialization

The application supports three types of library items:
- Books
- CDs
- Video Games

Each item can be searched, added, and removed from the catalog.
"""

from catalog import Catalog
from SubClasses import Books, CDs, Video_Games

def print_menu():
    print("Library Catalog Menu")
    print("1. Search catalog")
    print("2. Print the entire catalog")
    print("3. Add item to catalog")
    print("4. Remove item from catalog")
    print("5. Open catalog from file")
    print("6. Save catalog to file")
    print("7. Exit")
    print("Choose an option: ", end="")

def main():
    catalog = Catalog(name="My Library Catalog")

    while True:
        print_menu()
        choice = input().strip()

        if choice == '1':
            search_term = input("Enter the search term: ").strip()
            results = catalog.search_items(search_term)
            if results:
                for item in results:
                    print(item)
            else:
                print("No items found.")

        elif choice == '2':
            items = catalog._items
            for item in items:
                print(item)

        elif choice == '3':
            item_type = input("Enter the type of item (book/cd/game): ").strip().lower()
            name = input("Enter the name: ").strip()
            isbn = input("Enter the ISBN: ").strip()
            tags = input("Enter the tags (comma separated): ").strip().split(',')

            if item_type == 'book':
                author = input("Enter the author: ").strip()
                genre = input("Enter the genre: ").strip()
                page_numbers = input("Enter the number of pages: ").strip()
                new_item = Books(name, isbn, tags, author, genre, page_numbers)
            elif item_type == 'cd':
                artist = input("Enter the artist: ").strip()
                cd_length = input("Enter the length of the CD: ").strip()
                new_item = CDs(name, isbn, tags, cd_length, artist)
            elif item_type == 'game':
                genre = input("Enter the genre: ").strip()
                studio = input("Enter the studio: ").strip()
                console = input("Enter the console: ").strip()
                new_item = Video_Games(name, isbn, tags, genre, studio, console)
            else:
                print("Invalid item type.")
                continue

            catalog.add_items([new_item])
            print("Item added to catalog.")

        elif choice == '4':
            name = input("Enter the name of the item to remove: ").strip()
            item_to_remove = None
            for item in catalog._items:
                if item.name.lower() == name.lower():
                    item_to_remove = item
                    break
            if item_to_remove:
                catalog.remove_items([item_to_remove])
                print("Item removed from catalog.")
            else:
                print("Item not found in catalog.")
        elif choice == '5':
            print("Saving current catalog to file")
            catalog.save_as_pickle()
        elif choice == '6':
            print("Loading save from file")
            catalog.load_from_pickle()
        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
