import unittest
import json
from library.classes.categories import Categories

test_data_location = "tests/data/categories.json"

class Test_categories(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        with open(test_data_location, "w") as books:
                    json.dump([], books)