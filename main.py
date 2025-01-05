from project_management.create_project import create_project
from project_management.list_project import search_projects_by_date, view_project, delete_project, update_project
from project_management.fileoperations import read_projects
from registration import register_user
from login import login_user

def main():
    read_projects()
    while True:
        print("\nCrowdfunding Console App")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            register_user()

        elif option == "2":
            email = login_user()

            if email:
                while True:
                    print("\nCrowdfunding Console App")
                    print("1. Create Project")
                    print("2. View Projects")
                    print("3. Search Projects by Date")
                    print("4. Update Project")
                    print("5. Delete Project")
                    print("6. Logout")
                    option = input("Choose an option: ")

                    if option == "1":
                        create_project(email)
                    elif option == "2":
                        view_project()
                    elif option == "3":
                        search_projects_by_date()
                    elif option == "4":
                        update_project(email)
                    elif option == "5":
                        delete_project(email)
                    elif option == "6":
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
