from src.classes import users, bills
from src.operations import products_operations, cart_operations
from src.db_operations import bill_db,cart_db
from typing import List

def get_id_and_quantity_if_products_can_be_billed_in_cart_of_user(user: users.User):
    cart_details, product_details = cart_operations.get_cart_and_product_details(user)

    product_ids_and_quantity=[]

    if product_details:
        for i in range(len(product_details)):
            if not products_operations.get_product_details_if_can_be_added(product_details[i].get_id(),
                                                                           cart_details[i].quantity):
                print("Some products are not available anymore, please remove those items from cart")
                return
            product_ids_and_quantity.append((product_details[i].get_id(),cart_details[i].quantity))
        return product_ids_and_quantity
    else:
        return


def get_bill_for_user(username):

    results_bills = bill_db.get_bill_data_for_user(username)
    if not results_bills:
        return None

    # active_cart_id = cart_db.get_active_cart_id_for_user(username)

    bill_objects: List[bills.Bill] = []

    for bill in results_bills:
        bill_id = bill[0]
        bill = bill[1:]
        bill_object = bills.Bill(*bill)
        bill_object.id = bill_id
        # skipping active cart
        # if bill_object.cart_id == active_cart_id:
        #     continue
        bill_objects.append(bill_object)
        # cart_ids.append(bill_object.cart_id)
        # bill_data_to_print.append([bill_object.id, bill_object.cart_id])

    if not bill_objects:
        return

    bill_data_to_print= []

    for bill_object in bill_objects:
        bill_data_to_print.append([bill_object.id, bill_object.username,
                                   bill_object.total_amount, bill_object.discount])

    return bill_data_to_print

    # cart_details_objects = cart_operations.get_data_from_cart_ids(cart_ids)
    #
    # cart_details_objects = sorted(cart_details_objects, key= lambda x: x.cart_id)
    #
    # product_ids = []
    #
    # for cart_data in cart_details_objects:
    #     product_ids.append(cart_data.product_id)
    #
    # all_products = products_operations.get_products_by_ids(product_ids)
    #
    # for bill_data in bill_data_to_print:
