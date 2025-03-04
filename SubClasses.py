from LibraryItem import *

'''
adding the three sub classes for the project being: Books,  CDs, and Magazines for the parent class LibraryItem 
'''

class Books(LibraryItem):
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

class CDs(LibraryItem):
    def __init__(self, name, isbn, tags, cd_length, artist):
        super().__init__(name, isbn, tags)
        self.cd_length = cd_length
        self.artist = artist

    def match(self, keyword):
        return keyword.lower() in self.name.lower() or keyword.lower() in self.artist.lower() or any(keyword.lower() in tag.lower() for tag in self.tags)
        
    def __str__(self):
        return f"CD: {self.name}, Artist: {self.artist}, Length: {self.cd_length}, ISBN: {self.isbn}, Tags: {self.tags}"
    
    def make_a_da_short_string(self):
        return f"CD: {self.name} by {self.artist}"

class Magazines(LibraryItem):
    pass

# Testing the Books class
'''
x = Books("Harry Potter", "123456", ["fantasy", "magic"], "J.K. Rowling", "Fantasy", 300)
print(x)
print(x.match("Harry"))
print(x.match("Rowling"))
print(x.match("magic"))
print(x.match("fantasy"))
'''