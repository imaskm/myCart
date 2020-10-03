import sqlite3
from mycart.scripts import db_constants

# CustomExceptions
class DatabaseConnectionError(BaseException):
    pass


class TableCreationError(BaseException):
    pass


# create a database connection to the SQLite database specified by db_file
def create_connection():
    try:
        conn = sqlite3.connect(db_constants.DB_PATH)
        return conn
    except:
        raise DatabaseConnectionError


def create_table(conn, table_query):
    try:
        cur = conn.cursor()
        cur.execute(table_query)
    except Exception as e:
        print(e)
        print(table_query)
        raise TableCreationError


def create_admin_user():
    try:
        conn = create_connection()
        cur = conn.cursor()
        sql_cmd = "INSERT INTO users(username,password,name,is_admin) VALUES('admin','admin','Admin',1);"
        cur.execute(sql_cmd)
        conn.commit()
    except Exception as e:
        # print(e)
        return
    finally:
        conn.close()


if __name__ == "__main__":
    try:
        conn = create_connection()

        for create_table_query in db_constants.ALL_TABLES:
            create_table(conn,create_table_query)

        create_admin_user()

    except DatabaseConnectionError:
        print("Failed to connect to the DB")
        exit()
    except TableCreationError:
        print("Failed to create the table")




