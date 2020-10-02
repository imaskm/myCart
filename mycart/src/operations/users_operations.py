import getpass
from src.classes import users, products
from src.custom_exceptions import users_exceptions
from src.db_operations import users_db, products_db


def register():
    while True:
        try:
            username: str = input("Enter username:  ")
            password: str = getpass.getpass("Enter password: ")
            confirm_password: str = getpass.getpass("Confirm password: ")
            name: str = input("Enter your full name:  ")

            user = users.User(username, password, name)

            if password != confirm_password:
                print("passwords are not same, please enter again")
                continue

            if users_db.check_if_username_exists(username):
                print("This username is already taken, try different one")
                continue
            users_db.create_user(user)
            return user
        except users_exceptions.InvalidUsernameException:
            print("Invalid Username (must be alphanumeric, start with alphabet and of length (4-8))")
        except users_exceptions.InvalidPasswordException:
            print("Invalid Password (must be of length 4 to 30)")
        except users_exceptions.InvalidNameException:
            print("Invalid Name, must be of length 2 to 30")


def login():
    while True:

        username = input("Enter your username: ")
        password = getpass.getpass("Enter your password: ")

        user = users_db.get_user_from_username_and_password(username,password)
        if not user:
            print("Invalid credentials, try again!")
            continue
        return user


def add_product_to_users_cart(user, product_id, quantity=1):

    product_details = products_db.get_product_details(product_id)

    if not product_details:
        print("\nCouldn't add product to cart, try again\n")
        return None

    product_details = products.Product(*product_details)

    if product_details.quantity == 0:
        print("\nProduct is out of stock!!")
        return

    if product_details.quantity < quantity:
        print(f"Only {product_details.quantity} items of this product available \n")
        return

    return users_db.update_users_active_cart(user, product_details, quantity)


def logout(user):
    if user:
        del user
    return

