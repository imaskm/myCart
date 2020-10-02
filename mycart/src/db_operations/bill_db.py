from mycart.scripts import init
from src.classes import bills


def create_new_bill(bill: bills.Bill):
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        #decrease product quantity
        sql_cmd =


        sql_cmd = 'INSERT INTO bills(total_amount,discount,cart_id,username) VALUES(?,?,?,?);'
        cursor.execute(sql_cmd, (bill.total_amount, bill.discount, bill.cart_id, bill.username))
        result = cursor.lastrowid
        if result:
            sql_cmd = 'UPDATE carts SET is_active=0 where id=?'
            cursor.execute(sql_cmd, (bill.cart_id,))

            if cursor.rowcount != 0:
                db_conn.commit()
                bill.id = result
                return True
    except:
        return None
    finally:
        if db_conn:
            db_conn.close()
