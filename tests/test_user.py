import unittest
import json
from library.classes.user import User

test_data_location = "tests/data/users.json"

class Test_user(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        with open(test_data_location, "w") as books:
                    json.dump([], books)