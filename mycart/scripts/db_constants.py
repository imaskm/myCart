DB_PATH = "/home/ashwani/work/MyCart/mycart.db"

USERS_TABLE = """ CREATE TABLE IF NOT EXISTS users (
                                        username text PRIMARY KEY,
                                        password text NOT NULL,
                                        name text NOT NULL,
                                        is_admin integer DEFAULT 0
                                    ); """

CATEGORY_TABLE = """ CREATE TABLE IF NOT EXISTS categories(
                                        id text PRIMARY KEY,
                                        name text NOT NULL UNIQUE
                                    ); """

PRODUCT_TABLE = """ CREATE TABLE IF NOT EXISTS products (
                                        id text PRIMARY KEY,
                                        name text NOT NULL,
                                        price real NOT NULL,
                                        category_id text NOT NULL,
                                        FOREIGN KEY (category_id) REFERENCES categories(category_id)
                                        );  """

CART_TABLE = """ CREATE TABLE IF NOT EXISTS carts (
                                        id text PRIMARY KEY,
                                        username text NOT NULL UNIQUE,
                                        FOREIGN KEY (username) REFERENCES users(username)
                                    );  """

CART_DETAILS_TABLE = """ CREATE TABLE IF NOT EXISTS cartdetails (
                                        id text PRIMARY KEY,
                                        cart_id text NOT NULL,
                                        product_id text NOT NULL,
                                        quantity integer NOT NULL,
                                        FOREIGN KEY (cart_id) REFERENCES carts(id),
                                        FOREIGN KEY (product_id) REFERENCES products(id)                  
                                    );  """

BILL_TABLE = """ CREATE TABLE IF NOT EXISTS bills (
                                        id text PRIMARY KEY,
                                        total_amount real NOT NULL,
                                        discount real NOT NULL,
                                        cart_details_id NOT NULL,
                                        username text NOT NULL UNIQUE,
                                        FOREIGN KEY (cart_details_id) REFERENCES cartdetails(cart_id)
                                    );  """

ALL_TABLES = (USERS_TABLE,CATEGORY_TABLE,PRODUCT_TABLE,CATEGORY_TABLE,CART_DETAILS_TABLE,BILL_TABLE)

