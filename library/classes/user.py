import json
import sys
data_location = "library/data/users.json"
test_data_location = "tests/data/users.json"


class User():
    def __init__(self, username) -> None:
        self.username = username
        self.is_authenticated = False
        self.data_location = data_location
        if 'unittest' in sys.modules:
            self.data_location = test_data_location

    def create(self,password):
        # convert password to hash
        # store username and passwordhash to json file
        pass

    def login(self, password):
        # retreive user info from json file by username
        # hash the inputted password
        # compare the hashed inputted password to the passwordhash from the file
        # if they match, then set self.is_authenticated = True and return False, otherwise return False
        pass

