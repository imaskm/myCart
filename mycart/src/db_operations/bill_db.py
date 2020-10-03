from mycart.scripts import init
from src.classes import bills
from src.operations import cart_operations, products_operations
from src.classes import users


def create_new_bill(bill: bills.Bill, product_ids_and_quantities):
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()

        cursor.execute("BEGIN")

        for product in product_ids_and_quantities:
            sql_cmd = "UPDATE products SET quantity = quantity - ? WHERE id=?;"
            cursor.execute(sql_cmd,(int(product[1]),product[0]))

        sql_cmd = 'INSERT INTO bills(total_amount,discount,cart_id,username) VALUES(?,?,?,?);'
        cursor.execute(sql_cmd, (bill.total_amount, bill.discount, bill.cart_id, bill.username))
        result = cursor.lastrowid
        if result:
            sql_cmd = 'UPDATE carts SET is_active=0 where id=?'
            cursor.execute(sql_cmd, (bill.cart_id,))

            if cursor.rowcount != 0:
                cursor.execute("COMMIT")
                bill.id = result
                return True
    except:
        cursor.execute("ROLLBACK")
        return None
    finally:
        if db_conn:
            db_conn.close()


def get_bill_data_for_user(username):

    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT * FROM bills WHERE username=?;'
        cursor.execute(sql_cmd, (username,))
        result = cursor.fetchall()
        return result if result else None

    except:
        return
    finally:
        if db_conn:
            db_conn.close()

    return None