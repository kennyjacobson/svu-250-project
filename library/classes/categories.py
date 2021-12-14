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

    def _get_category_in_list(self,name):
        for category in self.category_list:
            if name == category["name"]:
                return name
        return None
    
    def add_category(self,name,keyword):
        if(self._get_category_in_list(name)):
            return False, "Category already exists."
        category = {
            "name" : name,
            "keyword" : keyword
        } 
        self.category_list.append(category)
        with open(self.data_location, "w") as categories:
            json.dump(self.category_list, categories)
        return True, "Success."  

      
        

    #def add_category(name,keyword):
        # check to see if the category exists, if so return false, "category already exists."
        # else
        # create a dictionary for the name and the keyword
        # add the dictionary as an element to the category_list 
        # write the newly updated category_list to the data_location
      #  pass

    #def categorize(book):
        # loop through the category_list to see if any keyword exists in the book title, if so, return True, category
        # else return False, None
    #    pass

    
