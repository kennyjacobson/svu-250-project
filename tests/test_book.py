import unittest
import json
from library.classes.book import Book

test_data_location = "tests/data/books.json"

class Test_book(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        with open(test_data_location, "w") as books:
                    json.dump([], books)


    def test_get_book_in_list(self):
        title = "The Three-Body Problem"
        year = 2016

        non_existing_title = "The Brothers K"

        new_book = Book(title)
        new_book.year = year
        was_saved, _ = new_book.save()
        self.assertTrue(was_saved)
        
        existing_book = Book(title)
        self.assertTrue(existing_book._get_book_in_list())

        nonexisting_book = Book(non_existing_title)
        self.assertFalse(nonexisting_book._get_book_in_list())

    

    def test_save(self):
        title = "Pet Sematary"
        year = 1983

        new_book = Book(title)
        new_book.year = year

        #First time, it should save.
        was_saved, _ = new_book.save()
        self.assertTrue(was_saved)

        #Let's see if it's in the database.
        book_check = Book(title)
        self.assertTrue(book_check._get_book_in_list())

        #Second time, it should not.
        was_saved, _ = new_book.save()
        self.assertFalse(was_saved)

    def test_update_year(self):
        new_book = Book("The Hunchback of Notre Dame")
        new_book.year = 2021
        new_book.save()

        new_book2 = Book("The Hunchback of Notre Dame")
        self.assertEqual(new_book.year, new_book2.year)

        updated_year = 1831
        new_book.update_year(updated_year)
        self.assertEqual(updated_year, new_book.year)


    def test_search(self):
        initialBook = Book("Ender's Game")
        initialBook.save()

        title = "Ender"
        new_book = Book(title)
        foundBooks = new_book.search()
        self.assertEqual("Ender's Game", foundBooks[0]["title"])
        # for each book in database that starts with given letter,
        # if there is a book in the database that is not also in the returned list or in the list but not also in the database, fail.


    def test_remove(self):
        title = "Don Quijote"
        year = 1615

        new_book = Book(title)
        new_book.year = year
        was_saved, _ = new_book.save()
        self.assertTrue(was_saved)

        #Remove the book, it should remove w/o problem.
        was_removed, _ = new_book.remove()
        self.assertTrue(was_removed)

        #Try again to remove the book, it should fail.
        was_removed, _ = new_book.remove()
        self.assertFalse(was_removed)

        book_check = Book(title)
        self.assertFalse(book_check._get_book_in_list())

    def test_add_author(self):
        author_name = "Gabriel Garcia-Marquez"
        book = Book("One Hundred Years of solitude")
        book.save()
        book.add_author(author_name)
        self.assertTrue(author_name == book.author_name)

