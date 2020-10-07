import sys
from src.operations import users_operations, category_operations, products_operations, cart_operations, admin_operations
from src.classes import users, categories, products
from tabulate import tabulate


def welcome():
    return "Welcome to My Cart"


def home(user: users.User = None):
    if not user:

        while True:
            try:
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
            except EOFError:
                print("Exiting from application...")
                sys.exit(0)
            except KeyboardInterrupt:
                home()
            except ValueError:
                print("Invalid Input!!")
                continue

    else:

        if user.is_admin:

            while True:
                try:

                    print("\nSelect one of the options (press ctrl+d to exit): \n")
                    print("1. Add Category")
                    print("2. View Categories")
                    print("3. Add Product")
                    print("4. View All Products")
                    print("5. Check Cart of User")
                    print("6. See bills of a User")
                    print("7. Logout")

                    user_input = int(input())
                    if user_input == 1:
                        category = input("Enter New Category to Add: ").lower()
                        if admin_operations.add_category(user, category):
                            print("\n Category Added!!\n")
                        else:
                            print("\nCategory already exists!!\n")
                        continue
                    elif user_input == 2:
                        all_categories = category_operations.show_all_categories()
                        if all_categories:
                            print(tabulate(all_categories))
                        else:
                            print("\nNo Category Found!!\n")
                        continue

                    elif user_input == 3:
                        result = admin_operations.add_product(user)
                        if result is None:
                            print("\nProduct already exists!!\n")
                        elif not result:
                            continue
                        else:
                            print("\nProduct added!!\n")
                        continue
                    elif user_input == 4:
                        all_products = products_operations.show_all_products()
                        if all_products:
                            print(tabulate(all_products, products.Product.headers(), 'github'))
                        else:
                            print("\nNo Products Found!!!\n")

                    elif user_input == 5:
                        username = input("Enter username: ")
                        result = admin_operations.get_user_cart(username)

                        if result is None:
                            print("\nNo data found in cart for this user!!\n")
                        elif result:
                            print(tabulate(result, "keys", "github"))
                        continue

                    elif user_input == 6:
                        username = input("Enter username: ")
                        result = admin_operations.get_user_bills(username)
                        if result is None:
                            print("\nFailed to get the bills!!\n")
                        elif result:
                            print(tabulate(result, ["Bill ID", "username", "Total Amount", "Discount"], "github"))
                        continue

                    elif user_input == 7:
                        users_operations.logout(user)
                        home()

                    else:
                        print("\nInvalid Input!!\n")
                        continue

                except ValueError:
                    print("\nInvalid Input!!\n")
                    continue
                except EOFError:
                    sys.exit("Exiting...")
                except KeyboardInterrupt:
                    home(user)

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
                    print("7. Remove product from cart")
                    print("8. Logout")

                    user_input = int(input())

                    if user_input == 1:
                        all_categories = category_operations.show_all_categories()
                        if all_categories:
                            print(tabulate(all_categories))
                        else:
                            print("\nNo Category Found!!\n")
                        continue
                    elif user_input == 2:
                        all_products = products_operations.show_all_products()
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
                        cart_data = cart_operations.get_cart_data_to_print(user.username)
                        if not cart_data:
                            print("\nYour cart is empty!! \n")
                            continue
                        else:
                            print(tabulate(cart_data, "keys", "github"))
                            continue
                    elif user_input == 6:
                        all_bill_data = cart_operations.checkout_cart(user)
                        if all_bill_data:
                            print("\nHere is your bill for last transaction\n")
                            print(tabulate(all_bill_data, "keys", "github"))
                            continue
                        else:
                            print("Unable to checkout cart")

                    elif user_input == 7:
                        product_id = int(input("Enter product id: "))
                        if cart_operations.remove_product_from_cart(user, product_id):
                            print("\nRemoved Item from cart\n")
                        else:
                            print("\nFailed to remove item from cart\n")

                    elif user_input == 8:
                        users_operations.logout(user)
                        home()

                    else:
                        print("Invalid Input!!!")
                        continue
                except ValueError:
                    print("\nInvalid Input, Try again!!\n")
                    continue
                except EOFError:
                    print("Exiting from application...")
                    sys.exit(0)
                except KeyboardInterrupt:
                    home(user)


if __name__ == "__main__":
    try:
        welcome()
        home()
    except Exception as e:
        print(e)
        sys.exit(0)
