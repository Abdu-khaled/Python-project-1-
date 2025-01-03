

from  registration import register


def main():
    while True:
        print("\nCrowdfunding Consle App")
        print("1. Register  ")
        print("2. Login")
        print("3. Exit")
        option = input("Choose an otion: ")

        if option == "1":
            register()

        elif option == "2":
            email = login()

            if email:

                while True:
                    print("\nCrowdfunding Consle App")
                    print("1. Create Project")
                    print("2. View Projects")
                    print("3. Logout")
                    option = input("Choose an otion: ")

                    if option == "1":
                        create_project(email)

                    elif option == "2":
                        view_projects()

                    elif option == "3":
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
