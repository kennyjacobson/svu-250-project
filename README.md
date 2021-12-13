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

