from mycart.scripts import init
import sys
from src.db_operations import cart_db
from src.classes import users, products


def check_if_username_exists(username: str):
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT 1 FROM users where username=?;'
        cursor.execute(sql_cmd, (username,))

        if cursor.fetchone():
            return True
        else:
            return False

    except:
        print("ERROR: Failed to fetch records!!")
        sys.exit(0)

    finally:
        if db_conn:
            db_conn.close()


def create_user(user: users.User):
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'INSERT INTO users(username,password,name) VALUES(?,?,?);'
        cursor.execute(sql_cmd, (user.username, user.password, user.name))

        if cursor.rowcount > 0:
            db_conn.commit()
            return True
        else:
            return False
    except:
        return None
    finally:
        if db_conn:
            db_conn.close()


def get_user_from_username_and_password(username: str, password: str):
    try:
        db_conn = None
        db_conn = init.create_connection()
        cursor = db_conn.cursor()
        sql_cmd = 'SELECT username,password,name,is_admin from users where username=? and password=?;'
        cursor.execute(sql_cmd, (username, password))
        result = cursor.fetchone()
        return users.User(*result) if result else None
    except:
        return
    finally:
        if db_conn:
            db_conn.close()


def update_users_active_cart(user: users.User, product_details: products.Product, quantity):

    active_cart_id = cart_db.get_active_cart_id_for_user(user.username)
    try:
        db_conn = init.create_connection()
        cursor = db_conn.cursor()

        if not active_cart_id:
            sql_cmd = 'INSERT INTO carts(username,is_active) VALUES(?,?)'
            cursor.execute(sql_cmd, (user.username, 1))
            result = cursor.lastrowid
            if not result:
                return None
            active_cart_id = result

        sql_cmd = 'INSERT OR REPLACE INTO cartdetails(id, cart_id, product_id, quantity) VALUES( ' \
                  '(SELECT id from cartdetails where cart_id=? AND product_id=?),?,?,?);'
        cursor.execute(sql_cmd, (active_cart_id, product_details.get_id(), active_cart_id, product_details.get_id(),
                                 quantity))

        if cursor.lastrowid:
            db_conn.commit()
            return True
    except:
        return
    finally:
        if db_conn:
            db_conn.close()
