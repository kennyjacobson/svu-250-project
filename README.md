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

### Categorizing a Book

```python
from library.classes.categories import Categories
from library.classes.book import Book
name = "Spy Novels"
keyword = "Spy"
title = "The Spy Who Loved Me"
new_book = Book(title)
new_category = Categories()
does_exist, _ = new_category.categorize(new_book)
print(does_exist, message)
```




### Creating a user

```python
from library.classes.user import User
username = "Username"
password = "password123"
the_user = user(username)
username.create(password)

```

### Logging in

```python
from library.classes.user import User
username = "Username"
password = "password123"
the_user = user(username)
successful_login = the_user.login(password)
if successful_login:
    print("Login successful.")
else:
    print("Login unsuccessful.")
    
```

### Creating an author

```python
from library.classes.author import Author
author = Author("Melanie Jacobson")
author.birth_year = 1974
was_author_saved, message = book.save()
print(was_author_saved, message)
```

### Parse an author's name

```python
from library.classes.author import Author
author = Author("Emily Dickinson")
author_first_name = ("Emily")
author_last_name = ("Dickinson")
parse_first_name, pasrse_last_name = author.save()
print(parse_first_name, parse_last_name, message)
```

### Search for a keyword in book's title

```python
from library.classes.book import Book
keyword = Book("Pirate")
keyword.search()
```

### Update a book's year

```python
#If book already exists in database:
from library.classes.book import Book
book = Book("Peter and the Starcatchers")
book.save()
book.update_year(2004)

#if book doesn't already exist in database:
from library.classes.book import Book
book = Book("Ender's Game")
book.year = 1945
book.update_year(1985)

