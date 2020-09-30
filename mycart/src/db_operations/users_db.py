from pip._vendor.pyparsing import _ustr

from mycart.scripts import init
import sys
from src.classes import users

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
        print("ERROR: Failed to fetch records!!")
        sys.exit(0)
    finally:
        if db_conn:
            db_conn.close()