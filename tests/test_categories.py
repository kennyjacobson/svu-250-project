import unittest
import json
from library.classes.categories import Categories

test_data_location = "tests/data/categories.json"

class Test_categories(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        with open(test_data_location, "w") as categories:
                    json.dump([], categories)

    
    def test_add_category(self):
      name = "Fantasy"
      keyword = "Dragon"

      #added category
      new_category = Categories()
      was_added, _ = new_category.add_category(name, keyword)
      self.assertTrue(was_added)

      #category exists already
      new_category = Categories()
      was_added, _ = new_category.add_category(name,keyword)
      self.assertFalse(was_added)