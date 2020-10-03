from src.classes import users, products
from src.db_operations import categories_db, products_db, users_db
from src.operations import cart_operations, bill_operations


def add_category(user: users.User, category):
    new_category_id = categories_db.insert_new_category(category)

    return new_category_id


def add_product(user):
    try:
        product_name = input("Enter product's name: ")
        product_price = float(input("Enter product's price: "))
        product_quantity = int(input("Enter product's quantity: "))
        product_categories = tuple(
            input("Enter category names(comma-separated for multiple value): ").lower().split(","))

        category_ids = []
        for category_name in product_categories:
            category_id = categories_db.get_category_id_from_name(category_name)
            if category_id:
                category_ids.append(str(category_id))
            else:
                print(f"Invalid category {category_name}, not added to product, Try again with valid values ")
                return False

        product = products.Product(
            _id=None,
            name=product_name,
            price=product_price,
            quantity=product_quantity,
            categories=category_ids
        )
        product_id = products_db.insert_new_product(product)

        return product_id

    except ValueError:
        print("\nInvalid Input!!\n")
        return


def get_user_cart(username):
    if not users_db.check_if_username_exists(username):
        print("No such user exists!!")
        return False

    return cart_operations.get_cart_data_to_print(username)


def get_user_bills(username):
    if not users_db.check_if_username_exists(username):
        print("No such user exists!!")
        return False

    bill_data_to_print = bill_operations.get_bill_for_user(username)

    return bill_data_to_print
