from library.classes.book import Book

def add_book():
    book = Book("The Three-Body Problem")
    print(book.year)
    book.year = 2016
    
    was_book_saved, message = book.save()
    print(was_book_saved, message)
    

if __name__ == '__main__':
    add_book()