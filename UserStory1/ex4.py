import re
input_string=input("enter list of passwords")
password_list=input_string.split(',')
valid_password_list=[]

def isPassword_valid(password):
    pattern=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$]).{6,12}$'
    if(re.match(pattern, password)!= None):
        return True
    else:
        return False



for i in password_list:
    if(isPassword_valid(i)):
        valid_password_list.append(i)
    
print(valid_password_list)