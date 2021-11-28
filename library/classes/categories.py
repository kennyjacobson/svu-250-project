import json
import sys
data_location = "library/data/categories.json"
test_data_location = "tests/data/categories.json"


class Categories():
    def __init__(self) -> None:
        self.data_location = data_location
        self.category_list = []
        if 'unittest' in sys.modules:
            self.data_location = test_data_location

        with open(self.data_location) as categories:
            self.category_list = json.load(categories)


    def add_category(name,keyword):
        # check to see if the category exists, if so return false, "category already exists."
        # else
        # create a dictionary for the name and the keyword
        # add the dictionary as an element to the category_list 
        # write the newly updated category_list to the data_location
        pass

    def categorize(book):
        # loop through the category_list to see if any keyword exists in the book title, if so, return True, category
        # else return False, None
        pass
