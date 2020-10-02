from src.db_operations import products_db, categories_db
from src.classes import products
from typing import List


def show_all_products():
    products_without_categories = products_db.get_all_products()

    if not products_without_categories:
        print("\nNo Products Found!!\n")
        return None

    categories_with_products = categories_db.get_category_names_for_all_product()
    all_products: List[products.Product] = []

    for p in products_without_categories:
        product_obj = products.Product(*p)
        all_products.append(product_obj)
        categories_for_product = []
        for product_id_and_category in categories_with_products:
            if product_obj.get_id() == product_id_and_category[0]:
                categories_for_product.append(product_id_and_category[1])

        product_obj.categories = tuple(categories_for_product)

    return all_products


def get_products_by_category(category_name):

    products_in_category = products_db.get_products_in_category(category_name)

    if not products_in_category:
        return None

    all_products: List[products.Product] = []

    for p in products_in_category:
        product_obj = products.Product(*p)
        product_obj.categories = (category_name,)
        all_products.append(product_obj)

    return all_products


def get_products_by_ids(product_ids):
    result_products = products_db.get_products_details(product_ids)

    if not result_products:
        return None

    all_products: List[products.Product] = []

    for product in result_products:
        product_obj = products.Product(*product)
        all_products.append(product_obj)

    return all_products
