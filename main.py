# filepath: /home/iturbo/Desktop/Python-project-1-/main.py
from project_management.list_project import search_projects_by_date, view_project

from registration import register_user

from login import login_user


from project_management.create_project import create_project



def main():
    while True:
        print("\nCrowdfunding Consle App")
        print("1. Register  ")
        print("2. Login")
        print("3. Exit")
        option = input("Choose an otion: ")

        if option == "1":
            register_user()

        elif option == "2":
            email = login_user()

            if email:

                while True:
                    print("\nCrowdfunding Consle App")
                    print("1. Create Project")
                    print("2. View Projects")
                    print("3. Search Projects by Date")
                    print("4. Logout")
                    option = input("Choose an otion: ")

                    if option == "1":
                        create_project(email)

                    elif option == "2":
                        view_project()

                    elif option == "3": 
                        search_projects_by_date()

                    elif option == "4":
                        break

                    else:
                        print("Invalid option")

        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
