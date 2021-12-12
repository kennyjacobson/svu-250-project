import json
import sys
data_location = "library/data/authors.json"
test_data_location = "tests/data/authors.json"

class Author():
    def __init__(self, full_name):
        self.full_name = full_name
        self.birth_year = 0
        #TODO: parse out full_name into corresponding first_name and last_name
        self.first_name = full_name.split()[0]
        self.last_name = full_name.split()[1]
        self.author_list = []
        self.data_location = data_location

        if 'unittest' in sys.modules:
            self.data_location = test_data_location

        with open(self.data_location) as authors:
            self.author_list = json.load(authors)

        author = self._get_author_in_list()
        if(author):
            self.full_name = author["full_name"]
            self.birth_year = author["birth_year"]
            self.first_name = author["first_name"]
            self.last_name = author["last_name"]
    
    def _get_author_in_list(self):
        for author in self.author_list:
            if self.full_name == author["full_name"]:
                return author
        return None
    
    
    
    def update_author_birth_year(self, updatedYear):
        '''If author does not already exist in database, it will be saved.'''
        self.birth_year = updatedYear
        if self._get_author_in_list():
            self.remove()
            self.save()

    def parse_author_name(self):
        '''Parse the full name of the author to be first name and last name'''
        for author in self.author_list:
            if self.first_name == author["first_name"]:
                return author.split()[0]
            if self.last_name == author["last_name"]:
                return author.split()[1]    
        return None

    #TODO: save() 
    # see book.py save() for guidance
    def save(self):

        '''Saves the author to the database. 
        Returns was_author_saved (bool) and message.
        If the author already exists, the author will not save.'''

        if(self._get_author_in_list()):
            return False, "Book already exists."

        author = {
            "full_name" : self.full_name,
            "birth_year" : self.birth_year,
            "first_name" : self.first_name,
            "last_name"  : self.last_name
         }
        self.author_list.append(author)
        with open(self.data_location, "w") as authors:
            json.dump(self.author_list, authors)
        return True, "Success."

       


    #TODO: remove() 
    # see book.py remove() for guidance
    def remove(self):
        for author in self.author_list:
            if self.full_name == author["full_name"]:
                self.author_list.remove(author)
                with open(self.data_location, "w") as authors:
                    json.dump(self.author_list, authors)
                return True, "Successfully removed."
        return False, "Not found."
    #TODO: get_author_age()
    # subract author's birth_year from current year
    # return the value

    #TODO: search()
    #  return a list of authors whose last_name starts with whatever the user used to create the author object
    #  example:
    #   author_A = Author("A")
    #   list_A = author_A.search()
    #   list_A contains all the authors whose last name start with "A" like "Douglas Adams", "Chinua Achebe", etc.