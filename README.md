# svu-250-project

## Examples of How To Use

### Creating a book

```python
from library.classes.book import Book
book = Book("The Three-Body Problem")
book.year = 2014
was_book_saved, message = book.save()
print(was_book_saved, message)
```

### Removing a book

```python
from library.classes.book import Book
book = Book("The Three-Body Problem")
was_book_saved, message = book.remove()
print(was_book_saved, message)
```

### Creating an author

```python
from library.classes.author import Author
author = Author("Melanie Jacobson")
author.birth_year = 1974
was_author_saved, message = book.save()
print(was_author_saved, message)
```
