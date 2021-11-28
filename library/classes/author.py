import json
import sys
data_location = "library/data/authors.json"
test_data_location = "tests/data/authors.json"

class Author():
    def __init__(self, full_name):
        self.full_name = full_name
        self.birth_year = 0
        #TODO: parse out full_name into corresponding first_name and last_name
        self.author_list = []
        self.data_location = data_location

        if 'unittest' in sys.modules:
            self.data_location = test_data_location

        with open(self.data_location) as authors:
            self.author_list = json.load(authors)

        author = self._get_author_in_list()
        if(author):
            self.full_name = author["full_name"]
            
    
    def _get_author_in_list(self):
        for author in self.author_list:
            if self.full_name == author["full_name"]:
                return author
        return None

    #TODO: save() 
    # see book.py save() for guidance

    #TODO: remove() 
    # see book.py remove() for guidance

    #TODO: get_author_age()
    # subract author's birth_year from current year
    # return the value

    #TODO: search()
    #  return a list of authors whose last_name starts with whatever the user used to create the author object
    #  example:
    #   author_A = Author("A")
    #   list_A = author_A.search()
    #   list_A contains all the authors whose last name start with "A" like "Douglas Adams", "Chinua Achebe", etc.