
from registration import users


def login_user():

    print("Login:")
    email = input("Email: ")
    password = input("Password: ")

    user = users.get(email)
    
    if user and user["password"] == password:
        print(f"Welcome back, {user['first_name']}!")
        return email
    else:
        print("Invalid email or password!")
        return None
