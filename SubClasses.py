from LibraryItem import *

'''
adding the three sub classes for the project being: Books,  CDs, and Magazines for the parent class LibraryItem 
'''

class Books(AbstractLibraryItem):
    def __init__(self, name, isbn, tags, author, genre, page_numbers):
        super().__init__(name, isbn, tags)
        self.author = author
        self.genre = genre
        self.page_numbers = page_numbers

    def match(self, keyword):
        return keyword.lower() in self.name.lower() or keyword.lower() in self.author.lower() or any(keyword.lower() in tag.lower() for tag in self.tags)

    def __str__(self):
        return f"Book: {self.name}, Author: {self.author}, Genre: {self.genre}, Pages: {self.page_numbers}, ISBN: {self.isbn}, Tags: {self.tags}"

    def to_short_string(self):
        return f"Book: {self.name} by {self.author}"

class CDs(AbstractLibraryItem):
    def __init__(self, name, isbn, tags, cd_length, artist):
        super().__init__(name, isbn, tags)
        self.cd_length = cd_length
        self.artist = artist

    def match(self, keyword):
        return keyword.lower() in self.name.lower() or keyword.lower() in self.artist.lower() or any(keyword.lower() in tag.lower() for tag in self.tags)
        
    def __str__(self):
        return f"CD: {self.name}, Artist: {self.artist}, Length: {self.cd_length}, ISBN: {self.isbn}, Tags: {self.tags}"
    
    def to_short_string(self):
        return f"CD: {self.name} by {self.artist}"

class Video_Games(AbstractLibraryItem):
    def __init__(self, name, isbn, tags, genre, studio, console):
        super().__init__(name, isbn, tags)
        self.genre = genre
        self.studio = studio
        self.console = console
    
    def match(self, keyword):
        return keyword.lower() in self.name.lower() or keyword.lower() in self.studio.lower() or keyword.lower() in self.console.lower() or keyword.lower() in self.genre.lower() or any(keyword.lower() in tag.lower() for tag in self.tags)
    
    def __str__(self):
        return f"Game: {self.name}, Genre: {self.genre}, Studio: {self.studio}, Console: {self.console} ISBN: {self.isbn}, Tags: {self.tags}"
    
    def to_short_string(self):
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
