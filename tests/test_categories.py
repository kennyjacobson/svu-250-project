import unittest
import json
from library.classes.categories import Categories
from library.classes.book import Book

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
    
    def test_categorize(self):
        title = "The spy Who Loved Me"
        keyword = "Spy"
        name = "Spy novels"
        new_book = Book(title)
        was_saved, _ = new_book.save()
        print(was_saved)
        new_category = Categories()
        new_category.add_category(name, keyword)
        does_exist, category = new_category.categorize(new_book)
        self.assertTrue(does_exist)
        self.assertEquals(category, name)

        title = "Ninjas running through the forest"
        new_book_2 = Book(title)
        no_exist, _ = new_category.categorize(new_book_2)
        self.assertFalse(no_exist)