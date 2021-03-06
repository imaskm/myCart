from mycart.scripts import init


def get_active_cart_id_for_user(username):

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT id FROM carts WHERE username=? AND is_active=1;'
        cursor.execute(sql_cmd, (username,))
        result = cursor.fetchone()
        return result[0] if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def get_cartdetails_from_id(cart_id):

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT * FROM cartdetails WHERE cart_id=?;'
        cursor.execute(sql_cmd, (cart_id,))
        result = cursor.fetchall()
        return result if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def remove_product_from_cart(cart_id, product_id,is_only_item_in_cart):

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        cursor.execute("BEGIN")
        sql_cmd = 'DELETE FROM cartdetails WHERE cart_id=? and product_id=?;'
        cursor.execute(sql_cmd, (cart_id,product_id))
        if cursor.rowcount != 0:
            if is_only_item_in_cart:
                sql_cmd="UPDATE carts SET is_active=0 WHERE id=?"
                cursor.execute(sql_cmd, (cart_id,))

            cursor.execute("COMMIT")
            return True
    except:
        cursor.execute("ROLLBACK")
        return
    finally:
        if db_conn:
            db_conn.close()