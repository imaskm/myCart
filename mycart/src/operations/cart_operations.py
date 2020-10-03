from src.db_operations import cart_db, bill_db
from typing import List
from src.classes import cartdetails, products, bills
from src.operations import products_operations, bill_operations
from src.utility import settings


def get_cart_data_to_print(username):
    cart_details_objects, all_products = get_cart_and_product_details(username)

    if not all_products:
        return

    cart_data_to_print = []
    total_amount_of_cart = 0
    for i in range(len(all_products)):
        cart_data = dict()
        cart_data["Product Name"] = all_products[i].name
        cart_data["Price"] = all_products[i].price
        cart_data["Quantities"] = cart_details_objects[i].quantity
        cart_data["Total Amount"] = cart_data["Price"] * cart_data["Quantities"]
        total_amount_of_cart += cart_data["Total Amount"]
        cart_data_to_print.append(cart_data)

    if cart_data_to_print:
        cart_data = dict()

        if total_amount_of_cart > settings.MINIMUM_AMOUNT_FOR_DISCOUNT:
            cart_data["Discount"] = settings.DISCOUNT_TO_BE_PROVIDED
        else:
            cart_data["Discount"] = 0

        cart_data["Total Amount"] = total_amount_of_cart - cart_data["Discount"]

        cart_data_to_print.append(cart_data)

    return cart_data_to_print


def get_cart_and_product_details(username):
    cart_id = cart_db.get_active_cart_id_for_user(username)

    if not cart_id:
        return None, None

    cart_details = cart_db.get_cartdetails_from_id(cart_id)

    if not cart_details:
        return None, None

    cart_details_objects: List[cartdetails.CartDetails] = []

    for cart_data in cart_details:
        cart_details_objects.append(cartdetails.CartDetails(*cart_data))

    product_ids = []

    for cart_data in cart_details_objects:
        product_ids.append(cart_data.product_id)

    all_products = products_operations.get_products_by_ids(product_ids)

    if not all_products:
        return None, None

    return cart_details_objects, all_products


def checkout_cart(user):
    cart_id = cart_db.get_active_cart_id_for_user(user.username)

    if not cart_id:
        print("Your cart is empty!!")
        return

    all_cart_data = get_cart_data_to_print(user.username)

    total_amount = all_cart_data[-1]["Total Amount"]
    discount = all_cart_data[-1]["Discount"]

    cart_details_objects, all_products = get_cart_and_product_details(user)

    if not all_products:
        return

    new_bill = bills.Bill(total_amount, discount, cart_id, user.username)

    product_ids_and_quantity = bill_operations.get_id_and_quantity_if_products_can_be_billed_in_cart_of_user(user)

    if not product_ids_and_quantity:
        return

    if not bill_db.create_new_bill(new_bill, product_ids_and_quantity):
        return

    data = dict()
    data["Product Name"] = "Customer Name"
    data["Price"] = user.name
    all_cart_data.append(data)

    data = dict()
    data["Product Name"] = "Bill Number"
    data["Price"] = new_bill.id

    all_cart_data.append(data)

    data = dict()
    data["Product Name"] = "Company Name"
    data["Price"] = "ScaleReal"

    all_cart_data.append(data)

    return all_cart_data


def remove_product_from_cart(user, product_id):

    cart_id = cart_db.get_active_cart_id_for_user(user.username)

    if not cart_id:
        print("Your cart is empty!!")
        return

    cart_details = cart_db.get_cartdetails_from_id(cart_id)

    is_only_item_in_cart = False

    if len(cart_details) == 1:
        is_only_item_in_cart=True

    for cart_data in cart_details:
        cart_details_object = cartdetails.CartDetails(*cart_data)

        if product_id == cart_details_object.product_id:
            if cart_db.remove_product_from_cart(cart_id,product_id, is_only_item_in_cart):
                return True
            else:
                return False
    return False


def get_data_from_cart_ids(cart_ids):

    cart_details = []
    for cart_id in cart_ids:
        cart_details.extend(cart_db.get_cartdetails_from_id(cart_id))

    if not cart_details:
        return

    cart_details_objects: List[cartdetails.CartDetails] = []

    for cart_data in cart_details:
        cart_details_objects.append(cartdetails.CartDetails(*cart_data))

    return cart_details_objects

