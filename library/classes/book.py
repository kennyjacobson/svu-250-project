import json
import sys
data_location = "library/data/books.json"
test_data_location = "tests/data/books.json"

class Book():
    def __init__(self, title):
        self.title = title
        self.year = 0
        self.book_list = []
        self.data_location = data_location

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

    #TODO: update_year()
    # update the year field and save

    #TODO: add_author()
    # make sure the author exists
    # update the author property and save

    #TODO: add_category()
    # make sure the category exists
    # update the category property and save

    #TODO: get_book_age()
    # subract book's year from current year
    # return the value

    #TODO: search()
    #  return a list of books whose title starts with whatever the user used to create the book object
    #  example:
    #   book_A = Book("A")
    #   list_A = book_A.search()
    #   list_A contains all the books that start with "A" like "A Swiftly Tilting Planet", "Absalom, Absalom!", etc.

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
            "year" : self.year
        }
        self.book_list.append(book)
        with open(self.data_location, "w") as books:
            json.dump(self.book_list, books)
        return True, "Success."
    
        
