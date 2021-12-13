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
### Adding a Category

```python
from library.classes.categories import Categories
name = "Fantasy"
keyword = "Dragon"
new_category = Categories()
was_added, message = new_category.add_category(name, keyword)
print(was_added, message)
```