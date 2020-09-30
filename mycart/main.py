import sys
from src.operations import users_operations


def welcome():
    return "Welcome to My Cart"


def home(username=None):
    if not username:
        try:
            while True:
                print("Select one of the options (press ctrl+d to exit): \n")
                print("1. Register")
                print("2. Login")

                user_input = int(input())

                if user_input == 1:
                    users_operations.register()
                    sys.exit(0)
                elif user_input == 2:
                    users_operations.login()
                else:
                    print("Invalid Input!!!")
                    continue
        except KeyboardInterrupt:
            print("Exiting from application...")
            sys.exit(0)

    else:

        try:
            while True:
                print("Select one of the options (press ctrl+d to exit): \n")
                print("1. View Categories")
                print("2. View All Products")
                print("3. View Products in a category")
                print("4. View Cart")

                print("2. Login")

                user_input = int(input())

                if user_input == 1:
                    pass
                elif user_input == 2:
                    pass
                else:
                    print("Invalid Input!!!")
                    continue
        except KeyboardInterrupt:
            print("Exiting from application...")
            sys.exit(0)


if __name__ == "__main__":
    try:
        welcome()
        home()
    except Exception as e:
        print(e)
        sys.exit(0)
