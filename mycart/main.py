import sys
from src.operations import users_operations,category_operations, products_operations
from src.classes import users

def welcome():
    return "Welcome to My Cart"


def home(user: users.User = None):
    if not user:
        try:
            while True:
                print("Select one of the options (press ctrl+d to exit): \n")
                print("1. Register")
                print("2. Login")

                user_input = int(input())

                if user_input == 1:
                    user = users_operations.register()
                    print(f"{user.name} , you are successfully registered. you can now login")
                    del user
                    continue
                elif user_input == 2:
                    user: users.User = users_operations.login()
                    home(user)
                else:
                    print("Invalid Input!!!")
                    continue
        except KeyboardInterrupt:
            print("Exiting from application...")
            sys.exit(0)
        except KeyError:
            print("Exiting application....")
            sys.exit(0)

    else:

        try:
            while True:
                print("\nSelect one of the options (press ctrl+d to exit): \n")
                print("1. View Categories")
                print("2. View All Products")
                print("3. View Products in a category")
                print("4. View Cart")
                print("5. Logout")

                user_input = int(input())

                if user_input == 1:
                    category_operations.show_all_categories()
                    continue
                elif user_input == 2:
                    products_operations.show_all_products()
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
