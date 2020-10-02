import sys
from src.operations import users_operations,category_operations, products_operations, cart_operations
from src.classes import users, categories, products
from tabulate import tabulate

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
        while True:
            try:
                print("\nSelect one of the options (press ctrl+d to exit): \n")
                print("1. View Categories")
                print("2. View All Products")
                print("3. View Products in a category")
                print("4. Add Product in Cart")
                print("5. View Cart")
                print("6. Checkout Cart")
                print("7. Logout")

                user_input = int(input())

                if user_input == 1:
                    all_categories = category_operations.show_all_categories()
                    if all_categories:
                        print(tabulate(all_categories))
                    else:
                        print("\nNo Category Found!!\n")
                    continue
                elif user_input == 2:
                    all_products =  products_operations.show_all_products()
                    if all_products:
                        print(tabulate(all_products, products.Product.headers(), 'github'))
                    else:
                        print("\nNo Products Found!!!\n")
                    continue
                elif user_input == 3:

                    category_input = input("Enter Category:  ").lower()
                    products_in_category = products_operations.get_products_by_category(category_input)
                    if not products_in_category:
                        print("\n No Products Found in this category!! \n")
                    else:
                        print(tabulate(products_in_category, products.Product.headers(), 'github'))
                    continue
                elif user_input == 4:
                    product_id = input("Enter Product ID:  ")
                    product_quantity = int(input("Enter quantities (1 to 3):  "))
                    if product_quantity < 0 or product_quantity > 3:
                        print("\n Invalid Quantity!! \n")

                    if not users_operations.add_product_to_users_cart(user, product_id, product_quantity):
                        print("Failed to add the product in cart!! Try again\n")
                    else:
                        print("\nProduct has been added to cart!!\n")
                elif user_input == 5:
                    cart_data = cart_operations.show_cart(user)
                    if not cart_data:
                        print("\nYour cart is empty!! \n")
                        continue
                    else:
                        print(tabulate(cart_data, "keys", "github"))
                        continue

                elif user_input == 6:
                    all_bill_data = cart_operations.checkout_cart(user)
                    if not all_bill_data:
                        print("\nFailed to generate bill!! \n")
                        continue
                    print("\nHere is your bill for last transaction\n")
                    print(tabulate(all_bill_data,"keys","github"))
                    continue

                elif user_input == 7:
                    users_operations.logout(user)
                    home()

                else:
                    print("Invalid Input!!!")
                    continue
            except ValueError:
                print("\nInvalid Input, Try again!!\n")
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
