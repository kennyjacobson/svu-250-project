import unittest
import json
from library.classes import author
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

    def test_update_author_birth_year(self):
        new_author = Author("Stephen King")
        new_author.birth_year = 2000
        new_author.save()

        new_author2 = Author("Stephen King")
        self.assertEqual(new_author.birth_year, new_author2.birth_year)

        updated_birth_year = 1947
        new_author.update_author_birth_year(updated_birth_year)
        self.assertEqual(updated_birth_year, new_author.birth_year)

    def test_parse_author_name(self):
        author_name = "Jules Varne"
        parse_first_name = "Jules"
        parse_last_name = "Varne"
        author = Author(author_name)
        author.first_name = parse_first_name
        author.last_name = parse_last_name
        success, message = author.save()
        self.assertTrue(success)

    def test_remove(self):
        title = "Lord Tennyson"

        new_author = Author(title)
        new_author.birth_year = 1947
        was_saved, _ = new_author.save()
        self.assertTrue(was_saved)

        was_removed, _ = new_author.remove()
        self.assertTrue(was_removed)

        was_removed, _ = new_author.remove()
        self.assertFalse(was_removed)

        author_check = Author(title)
        self.assertFalse(author_check._get_author_in_list())

# Start of added test by Aaron
    def test_get_author_age(self):
        author1 = Author("Brandon Mull")
        author1.full_name = "Brandon Mull"
        author1.birth_year = 1997
        author1.save()
        new_Author = Author("Brandon Mull")
        age = new_Author.get_author_age()
        self.assertEqual(24, age)

    def test_search(self):
        author1 = Author("Brandon Mull")
        author1.full_name = "Brandon Mull"
        author1.save()

        last_name = "Mull"
        new_Author = Author("Brandon Mull")
        authorList = new_Author.search()
        self.assertEqual("Mull", authorList[0]["last_name"])

# End of added tests by Aaron
