import unittest
import json
import hashlib
from library.classes.user import User

test_data_location = "tests/data/users.json"

class Test_user(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName=methodName)
        with open(test_data_location, "w") as user:
                    json.dump([], user)
    def test_create(self):
        #Validation testing
        passing_username = "letmepass"
        passing_user = User(passing_username)
        passing_pass = "biguserpassword123"
        pass_hash = hashlib.sha256(passing_pass.encode("utf-8")).hexdigest()

        self.assertTrue(passing_user.create(passing_pass))
        with open(test_data_location, "r") as read_file_1:
            data_pass = json.load(read_file_1)
        
        pulledUser = ""
        foundUserFirst = False
        for user in data_pass:
            if user["username"] == passing_username:
                pulledUser = user
                foundUserFirst = True
        
        self.assertTrue(foundUserFirst)
        self.assertEqual(pulledUser["passwordhash"], pass_hash)

        #Defect testing 1, bad
        failing_username = "Somebodystopme"
        failing_user = User(failing_username)
        failing_pass = "thishashshouldfail"
        fail_hash = hashlib.sha256("pneumonoultramicroscopicsilicovolcanoconiosis".encode("utf-8")).hexdigest()
        failing_user.create(failing_pass)
        with open(test_data_location, "r") as read_file_2:
            data_fail = json.load(read_file_2)

        pulledUserFail = ""
        foundUserSecond = False
        for user in data_fail:
            if user["username"] == failing_username:
                pulledUserFail = user
                foundUserSecond = True

        self.assertTrue(foundUserSecond)
        self.assertNotEqual(fail_hash, pulledUserFail["passwordhash"])
        

        #Defect testing 2, mal
        nonexistant_username = "IDoNotExist"
        with open(test_data_location, "r") as read_file_3:
            data_nonexistant = json.load(read_file_3)
        foundUserThird = False
        
        for user in data_nonexistant:
            if user["username"] == nonexistant_username:
                foundUserThird = True

        self.assertFalse(foundUserThird)

        #Defect testing 3, exists
        existing_user = User(passing_username)
        self.assertFalse(existing_user.create("anypass"))


    def test_login(self):
        # Validation testing
        username1 = "spotmeinbrah"
        passingUser = User(username1)
        passingPassword = "iamthekeymasterareyouthegatekeeper"
        passingUser.create(passingPassword)
        self.assertTrue(passingUser.login(passingPassword))
        self.assertTrue(passingUser.is_authenticated)

        # Defect testing 1, bad
        username2 = "imthebadguy"
        failingUser = User(username2) 
        # I coded this while rewatching star wars.
        # the end of episode 4 is still one of the best sequences in all of cinema.
        correctPassword = "iamyourfather"
        failingUser.create(correctPassword)
        badPassword = "nooooooooooooooooooooooooooooooooooo"
        self.assertFalse(failingUser.login(badPassword))
        self.assertFalse(failingUser.is_authenticated)

        # defect testing 2, mal
        # attempt to login without having created an account
        username3 = "thisUserDoesNotExist"
        missingUser = User(username3)
        missingPassword = "nopassword"
        self.assertFalse(missingUser.login(missingPassword))
        self.assertFalse(missingUser.is_authenticated)