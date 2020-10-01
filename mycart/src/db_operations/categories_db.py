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
        sql_cmd = 'SELECT name FROM category as c WHERE c.id IN' \
                  '(SELECT category_id FROM productcategory WHERE product_id=?);'
        cursor.execute(sql_cmd, (product_id,))
        result = cursor.fetchall()
        return tuple(result) if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()