from LibraryItem import *

'''
adding the three sub classes for the project being: Books,  CDs, and Magazines for the parent class LibraryItem 
'''

class Books(AbstractLibraryItem):
    """
    Represents a book item in a library catalog. 
    Inherits from AbstractLibraryItem and adds book-specific attributes.
    """
    def __init__(self, name, isbn, tags, author, genre, page_numbers):
        """
        Initialize a new Book instance.
        Args:
            name (str): The title of the book
            isbn (str): The International Standard Book Number
            tags (list): List of tags associated with the book
            author (str): The author of the book
            genre (str): The genre of the book
            page_numbers (int): Total number of pages in the book
        """
        super().__init__(name, isbn, tags)
        self.author = author
        self.genre = genre
        self.page_numbers = page_numbers
    
    def match(self, keyword):
        """
        Check if the keyword matches the book's attributes.
        Args:
            keyword (str): The search term to match against
        Returns:
            bool: True if keyword is found in name, author, or tags, False otherwise
        """
        return keyword.lower() in self.name.lower() or \
               keyword.lower() in self.author.lower() or \
               any(keyword.lower() in tag.lower() for tag in self.tags)
    
    def __str__(self):
        """
        Generate a detailed string representation of the book.
        Returns:
            str: Formatted string with book details
        """
        return f"Book: {self.name}, Author: {self.author}, Genre: {self.genre}, Pages: {self.page_numbers}, ISBN: {self.isbn}, Tags: {self.tags}"
    
    def to_short_string(self):
        """
        Generate a concise string representation of the book.
        Returns:
            str: Abbreviated book description with name and author
        """
        return f"Book: {self.name} by {self.author}"

class CDs(AbstractLibraryItem):
    """
    Represents a CD item in a library catalog. 
    Inherits from AbstractLibraryItem and adds CD-specific attributes.
    """
    def __init__(self, name, isbn, tags, cd_length, artist):
        """
        Initialize a new CD instance.
        Args:
            name (str): The title of the CD
            isbn (str): The International Standard Book Number
            tags (list): List of tags associated with the CD
            cd_length (str): The total length of the CD (e.g., '45:30')
            artist (str): The artist or band of the CD
        """
        super().__init__(name, isbn, tags)
        self.cd_length = cd_length
        self.artist = artist
    
    def match(self, keyword):
        """
        Check if the keyword matches the CD's attributes.
        
        Args:
            keyword (str): The search term to match against
        Returns:
            bool: True if keyword is found in name, artist, or tags, False otherwise
        """
        return keyword.lower() in self.name.lower() or \
               keyword.lower() in self.artist.lower() or \
               any(keyword.lower() in tag.lower() for tag in self.tags)
    
    def __str__(self):
        """
        Generate a detailed string representation of the CD.
        Returns:
            str: Formatted string with CD details
        """
        return f"CD: {self.name}, Artist: {self.artist}, Length: {self.cd_length}, ISBN: {self.isbn}, Tags: {self.tags}"
    
    def to_short_string(self):
        """
        Generate a concise string representation of the CD.
        Returns:
            str: Abbreviated CD description with name and artist
        """
        return f"CD: {self.name} by {self.artist}"

class Video_Games(AbstractLibraryItem):
    """
    Represents a video game item in a library catalog.
    Inherits from AbstractLibraryItem and adds video game-specific attributes.
    """
    def __init__(self, name, isbn, tags, genre, studio, console):
        """
        Initialize a new Video Game instance.
        Args:
            name (str): The title of the video game
            isbn (str): The International Standard Book Number
            tags (list): List of tags associated with the video game
            genre (str): The genre of the video game
            studio (str): The game development studio
            console (str): The gaming platform or console
        """
        super().__init__(name, isbn, tags)
        self.genre = genre
        self.studio = studio
        self.console = console
    
    def match(self, keyword):
        """
        Check if the keyword matches the video game's attributes.
        Args:
            keyword (str): The search term to match against
        Returns:
            bool: True if keyword is found in name, studio, console, genre, or tags, False otherwise
        """
        return keyword.lower() in self.name.lower() or \
               keyword.lower() in self.studio.lower() or \
               keyword.lower() in self.console.lower() or \
               keyword.lower() in self.genre.lower() or \
               any(keyword.lower() in tag.lower() for tag in self.tags)
    
    def __str__(self):
        """
        Generate a detailed string representation of the video game.
        Returns:
            str: Formatted string with video game details
        """
        return f"Game: {self.name}, Genre: {self.genre}, Studio: {self.studio}, Console: {self.console} ISBN: {self.isbn}, Tags: {self.tags}"
    
    def to_short_string(self):
        """
        Generate a concise string representation of the video game.
        Returns:
            str: Abbreviated video game description with name and studio
        """
        return f"Game: {self.name} by {self.studio}"

# Testing the Video_Games class
'''
x = Video_Games("Minecraft", "132546", ["fun!", "adventure!"], "Sandbox Survival", "Mojang", "Xbox")
print(x)
print(x.match("Minecraft"))
print(x.match("Mojang"))
print(x.match("Xbox"))
print(x.match("sandbox"))
'''

# Testing the CDs class (the length is in minutes)
'''
x = CDs("Goodbye Yellow Brick Road", "123457", ["classic rock", "rock"], 72, "Elton John")
print(x)
print(x.match("Yellow"))
print(x.match("Elton"))
'''
