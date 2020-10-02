from mycart.scripts import init
from src.db_operations import categories_db, cart_db
from src.classes import users, products

def get_all_products():
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT * from products;'
        cursor.execute(sql_cmd)
        result = cursor.fetchall()
        return result if result else None
    except:
        # print("Failed to fetch records! Try again")
        return
    finally:
        if db_conn:
            db_conn.close()


def get_products_in_category(category_name):

    category_id = categories_db.get_category_id_from_name(category_name)
    if not category_id:
        return None

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT id, name, price from products AS p WHERE p.id IN ( SELECT product_id from ' \
                  'productcategories WHERE category_id=?);'
        cursor.execute(sql_cmd, (category_id,))
        result = cursor.fetchall()
        return result if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def get_product_details(product_id):

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT id, name, price, quantity from products WHERE id=?;'
        cursor.execute(sql_cmd, (product_id,))
        result = cursor.fetchone()
        return result if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def get_products_details(product_ids):

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = f"SELECT id, name, price, quantity from products WHERE id IN ({','.join(['?']*len(product_ids))});"
        cursor.execute(sql_cmd, product_ids)
        result = cursor.fetchall()
        return result if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()
