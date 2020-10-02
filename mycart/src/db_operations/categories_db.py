from mycart.scripts import init


def get_all_categories():
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT id,name from categories;'
        cursor.execute(sql_cmd)
        result = cursor.fetchall()
        return result if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def get_category_names_for_product(product_id):

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT name FROM categories as c WHERE c.id IN' \
                  '(SELECT category_id FROM productcategories WHERE product_id=?);'
        cursor.execute(sql_cmd, (product_id,))
        result = cursor.fetchall()
        return result if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def get_category_id_from_name(category_name):
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT id FROM categories WHERE name=?;'
        cursor.execute(sql_cmd, (category_name,))
        result = cursor.fetchone()
        return result[0] if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def get_category_names_for_all_product():

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT pc.product_id,name FROM categories as c INNER JOIN productcategories as pc ON ' \
                  'c.id=pc.category_id;'
        cursor.execute(sql_cmd)
        result = cursor.fetchall()
        return result if result else None

    except:
        return
    finally:
        if db_conn:
            db_conn.close()