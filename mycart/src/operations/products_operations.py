from src.db_operations import products_db, categories_db
from src.classes import products
from typing import List
from tabulate import tabulate

def show_all_products():

    products_without_categories = products_db.get_all_products()

    all_products : List[products.Product] = []
    import pdb
    pdb.set_trace()
    for p in products_without_categories:
        product_obj = products.Product(*p)
        all_products.append(product_obj)

        product_obj.categories = categories_db.get_category_names_for_product(product_obj.get_id())

    print(tabulate( all_products, products.Product.headers(), 'github' ))
