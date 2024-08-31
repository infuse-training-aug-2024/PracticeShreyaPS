import re

class PasswordValdation:
    def __init__(self):
        self.valid_password_list = []
        self.pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$]).{6,12}$'

    try:
        def isPassword_valid(self, password_list):
            for password in password_list:
                if re.match(self.pattern, password):
                    self.append_valid_password(password)
            return self 
    except ValueError :
        print("enter comma seperated list of passwords")

    def append_valid_password(self, password):
        self.valid_password_list.append(password)

try:
        
    input_string = input("Enter list of passwords separated by commas: ")
    if not input_string:
        raise ValueError("no input given")
    password_list = input_string.split(',')


    obj = PasswordValdation().isPassword_valid(password_list)

    # Print the valid passwords
    print("Valid passwords:", obj.valid_password_list)

except ValueError as ve:
    print("value error occured:",ve)
except Exception as e:
    print("error occured:",e)