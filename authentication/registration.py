import email
import re

users = {}   # dictionary to store user information

def register_user():

# Function to register a new user
    print("Registering New User")

    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")


    email = input("Enter your email address: ")

    # check if email is already registered
    if email in users:
        print("This email is already registered. Please try a different email or log in.")
        return
    
    # check if email is valid
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Invalid email format!")
        return
    
   
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    # check if password and confirm password match
    if password != confirm_password:
        return 'Passwords do not match'


    phone_number = input("Enter your phone number: ")
    # check if phone number is valid
    if not re.match(r"^01[0-2,5][0-9]{8}$", phone_number):
        print("Invalid Egyptian phone number format!")
        return
    

    users[email] = {"first_name": first_name, "last_name": last_name, "password": password, "phone": phone_number}
    print("Registration successful!")












