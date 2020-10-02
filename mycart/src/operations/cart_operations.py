from src.db_operations import cart_db,bill_db
from typing import List
from src.classes import cartdetails,products, bills
from src.operations import products_operations
from src.utility import settings


def show_cart(user):

    cart_details_objects,all_products = get_cart_and_product_details(user)

    if not all_products:
        return

    cart_data_to_print = []
    total_amount_of_cart = 0
    for i in range(len(all_products)):
        cart_data=dict()
        cart_data["Product Name"] = all_products[i].name
        cart_data["Price"] = all_products[i].price
        cart_data["Quantities"] = cart_details_objects[i].quantity
        cart_data["Total Amount"] = cart_data["Price"] * cart_data["Quantities"]
        total_amount_of_cart+=cart_data["Total Amount"]
        cart_data_to_print.append(cart_data)

    if cart_data_to_print:
        cart_data=dict()

        if total_amount_of_cart > settings.MINIMUM_AMOUNT_FOR_DISCOUNT:
            cart_data["Discount"] = settings.DISCOUNT_TO_BE_PROVIDED
        else:
            cart_data["Discount"] = 0

        cart_data["Total Amount"] = total_amount_of_cart - cart_data["Discount"]

        cart_data_to_print.append(cart_data)

    return cart_data_to_print


def get_cart_and_product_details(user):

    cart_id = cart_db.get_active_cart_id_for_user(user.username)

    if not cart_id:
        return None, None

    cart_details = cart_db.get_cartdetails_from_id(cart_id)

    if not cart_details:
        return None,None

    cart_details_objects: List[cartdetails.CartDetails] = []

    for cart_data in cart_details:
        cart_details_objects.append(cartdetails.CartDetails(*cart_data))

    product_ids = []

    for cart_data in cart_details_objects:
        product_ids.append(cart_data.product_id)

    all_products = products_operations.get_products_by_ids(product_ids)

    if not all_products:
        return None,None

    return cart_details_objects,all_products


def checkout_cart(user):

    cart_id = cart_db.get_active_cart_id_for_user(user.username)

    all_cart_data = show_cart(user)

    total_amount = all_cart_data[-1]["Total Amount"]
    discount = all_cart_data[-1]["Discount"]
    #actual_amount = total_amount - discount

    new_bill = bills.Bill(total_amount, discount, cart_id, user.username )

    if not bill_db.create_new_bill(new_bill):
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



