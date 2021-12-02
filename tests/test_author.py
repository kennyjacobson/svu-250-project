import unittest
import json
from library.classes.author import Author

test_data_location = "tests/data/authors.json"

class Test_author(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        with open(test_data_location, "w") as books:
                    json.dump([], books)

    def test_get_author_in_list(self):
        non_existing_name = "Fred Dostoevsky"

        nonexisting_book = Author(non_existing_name)
        self.assertFalse(nonexisting_book._get_author_in_list())

    def test_save(self):
        author_name = "Brandon Sanderson"
        birth_year = 1975
        author = Author(author_name)
        author.birth_year = birth_year
        success, message = author.save()
        self.assertTrue(success)

        author2 = Author(author_name)
        self.assertEqual(author2.birth_year, birth_year)
        success2, message2 = author2.save()

        self.assertFalse(success2)


