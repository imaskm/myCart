from mycart.scripts import init


def get_all_products():
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT id, name, price from products;'
        cursor.execute(sql_cmd)
        result = cursor.fetchall()
        return result if result else None
    except:
        #print("Failed to fetch records! Try again")
        return
    finally:
        if db_conn:
            db_conn.close()