from library.classes.book import Book
from library.classes.author import Author
def add_book():
    author = Author("Tennison Schmidt")
    author.save()
    book = Book("The Three-Body Problem")
    print(book.year)
    book.year = 2016
    was_updated, message = book.add_author("Tennison Schmidt")
    #was_book_saved, message = book.save()
    print(was_updated, message)
    

if __name__ == '__main__':
    add_book()