import json
import sys
from library.classes.author import Author
data_location = "library/data/books.json"
test_data_location = "tests/data/books.json"

class Book():
    def __init__(self, title):
        self.title = title
        self.year = 0
        self.book_list = []
        self.data_location = data_location
        self.author_name = ""

        if 'unittest' in sys.modules:
            self.data_location = test_data_location

        with open(self.data_location) as books:
            self.book_list = json.load(books)

        book = self._get_book_in_list()
        if(book):
            self.title = book["title"]
            self.year = book["year"]
            
    
    def _get_book_in_list(self):
        for book in self.book_list:
            if self.title == book["title"]:
                return book
        return None

    def update_year(self, updatedYear):
        '''If book does not already exist in database, it will be saved.'''
        self.year = updatedYear
        if self._get_book_in_list():
            self.remove()
        self.save()

    #TODO: add_author()
    # make sure the author exists
    # update the author property and save
    # In book save, make sure to update variable name before db.
    def add_author(self,author_name):
        author = Author(author_name)
        if author._get_author_in_list():
            self.author_name = author_name
            self.remove()
            self.save()
            return True, "Success"
        return False, "Author doesn't exist"

    #TODO: add_category()
    # make sure the category exists
    # update the category property and save

    #TODO: get_book_age()
    # subract book's year from current year
    # return the value

    def search(self):
        foundBooks = []
        # startingLetter = self.title[0]
        for book in self.book_list:
            if self.title in book["title"]:
                foundBooks.append(book)
        return foundBooks

    def remove(self):
        for book in self.book_list:
            if self.title == book["title"]:
                self.book_list.remove(book)
                with open(self.data_location, "w") as books:
                    json.dump(self.book_list, books)
                return True, "Successfully removed."
        return False, "Not found."

    def save(self):
        '''Saves the book to the database. 
        Returns was_book_save (bool) and message.
        If the book already exists, the book will not save.'''

        #TODO: Don't save the book if the year is missing.

        if(self._get_book_in_list()):
            return False, "Book already exists."
        book = {
            "title" : self.title,
            "year" : self.year,
            "author name" : self.author_name
        }
        self.book_list.append(book)
        with open(self.data_location, "w") as books:
            json.dump(self.book_list, books)
        return True, "Success."
        
