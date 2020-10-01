DB_PATH = "/home/ashwani/work/MyCart/mycart.db"

USERS_TABLE = """ CREATE TABLE IF NOT EXISTS users (
                                        username text PRIMARY KEY,
                                        password text NOT NULL,
                                        name text NOT NULL,
                                        is_admin integer DEFAULT 0
                                    ); """

CATEGORY_TABLE = """ CREATE TABLE IF NOT EXISTS categories(
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL UNIQUE
                                    ); """

PRODUCT_TABLE = """ CREATE TABLE IF NOT EXISTS products (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        name text NOT NULL,
                                        price real NOT NULL
                                        ); """

PRODUCT_CATEGORY_TABLE = """ CREATE TABLE IF NOT EXISTS productcategories(
                                        product_id integer NOT NULL,
                                        category_id integer NOT NULL,
                                        FOREIGN KEY (product_id) REFERENCES products(id),
                                        FOREIGN KEY (category_id) REFERENCES categories(id)
                                        );"""

CART_TABLE = """ CREATE TABLE IF NOT EXISTS carts (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        username text NOT NULL UNIQUE,
                                        FOREIGN KEY (username) REFERENCES users(username)
                                    );  """

CART_DETAILS_TABLE = """ CREATE TABLE IF NOT EXISTS cartdetails (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        cart_id integer NOT NULL,
                                        product_id integer NOT NULL,
                                        quantity integer NOT NULL,
                                        FOREIGN KEY (cart_id) REFERENCES carts(id),
                                        FOREIGN KEY (product_id) REFERENCES products(id)                  
                                    );  """

BILL_TABLE = """ CREATE TABLE IF NOT EXISTS bills (
                                        id integer PRIMARY KEY AUTOINCREMENT,
                                        total_amount real NOT NULL,
                                        discount real NOT NULL,
                                        cart_details_id integer NOT NULL,
                                        username text NOT NULL UNIQUE,
                                        FOREIGN KEY (cart_details_id) REFERENCES cartdetails(id)
                                    );  """

ALL_TABLES = (USERS_TABLE,CATEGORY_TABLE,PRODUCT_TABLE,PRODUCT_CATEGORY_TABLE,CART_TABLE,CART_DETAILS_TABLE,BILL_TABLE)

