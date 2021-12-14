import json
import sys
import hashlib
data_location = "library/data/users.json"
test_data_location = "tests/data/users.json"


class User():
    def __init__(self, username) -> None:
        self.username = username
        self.passwordhash = ""
        self.user_list = []
        self.is_authenticated = False
        self.data_location = data_location
        if 'unittest' in sys.modules:
            self.data_location = test_data_location

        with open(self.data_location, "r") as users:
            self.user_list = json.load(users)

    def get_user_in_list(self):
        for user in self.user_list:
            if self.username == user["username"]:
                return User
        return None

        # List of dictionaries? My minddddd

    def create(self,password):
        if(self.get_user_in_list()):
            return False

        hashedPass = hashlib.sha256(password.encode("utf-8")).hexdigest()
        user_dict = {
            "username" : self.username,
            "passwordhash" : hashedPass
        }
        self.user_list.append(user_dict)

        with open(self.data_location, "w") as users:
            json.dump(self.user_list, users)

        return True

    def login(self, password):
        with open(self.data_location, "r") as users:
            self.user_list = json.load(users)
        
        foundUser = {}
        for user in self.user_list:
            if user["username"] == self.username:
                foundUser = user

        hashedPass = hashlib.sha256(password.encode("utf-8")).hexdigest()
        try:
            if foundUser["passwordhash"] == hashedPass:
                self.is_authenticated = True
                return True
        except KeyError:
            return False
        return False

