import sqlite3

# Fungsi koneksi database
def create_connection(db_file):
    conn = sqlite3.connect(db_file)
    return conn

# Query untuk membuat tabel (minimal 5 tabel)
def create_tables(conn):
    drop_queries = [
        "DROP TABLE IF EXISTS order_items",
        "DROP TABLE IF EXISTS orders",
        "DROP TABLE IF EXISTS products",
        "DROP TABLE IF EXISTS categories",
        "DROP TABLE IF EXISTS users"
    ]
    create_queries = [
        "CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE, age INTEGER)",
        "CREATE TABLE categories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT)",
        "CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL, category_id INTEGER, FOREIGN KEY (category_id) REFERENCES categories (id))",
        "CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, order_date TEXT, total REAL, FOREIGN KEY (user_id) REFERENCES users (id))",
        "CREATE TABLE order_items (id INTEGER PRIMARY KEY AUTOINCREMENT, order_id INTEGER, product_id INTEGER, quantity INTEGER, FOREIGN KEY (order_id) REFERENCES orders (id), FOREIGN KEY (product_id) REFERENCES products (id))"
    ]
    cursor = conn.cursor()
    for query in drop_queries:
        cursor.execute(query)
    for query in create_queries:
        cursor.execute(query)
    conn.commit()
    print("Tabel berhasil dibuat.")

# Query untuk insert data
def insert_data(conn):
    cursor = conn.cursor()
    # Insert users
    cursor.execute("INSERT INTO users (name, email, age) VALUES ('John Doe', 'john@example.com', 30)")
    cursor.execute("INSERT INTO users (name, email, age) VALUES ('Jane Smith', 'jane@example.com', 25)")
    # Insert categories
    cursor.execute("INSERT INTO categories (name, description) VALUES ('Electronics', 'Electronic gadgets')")
    cursor.execute("INSERT INTO categories (name, description) VALUES ('Books', 'Various books')")
    # Insert products
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES ('Laptop', 1000.00, 1)")
    cursor.execute("INSERT INTO products (name, price, category_id) VALUES ('Python Book', 20.00, 2)")
    # Insert orders
    cursor.execute("INSERT INTO orders (user_id, order_date, total) VALUES (1, '2023-10-01', 1020.00)")
    # Insert order_items
    cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 1, 1)")
    cursor.execute("INSERT INTO order_items (order_id, product_id, quantity) VALUES (1, 2, 1)")
    conn.commit()
    print("Data berhasil disisipkan.")

# Query untuk select data (dengan join)
def select_data(conn):
    query = """
    SELECT u.name AS user, p.name AS product, oi.quantity, o.total
    FROM order_items oi
    JOIN orders o ON oi.order_id = o.id
    JOIN users u ON o.user_id = u.id
    JOIN products p ON oi.product_id = p.id
    """
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    print("Hasil Query Gabungan:")
    for row in rows:
        print(f"User: {row[0]}, Product: {row[1]}, Quantity: {row[2]}, Total: {row[3]}")

# Program utama
def main():
    database = "new_database.db"
    conn = create_connection(database)
    create_tables(conn)
    insert_data(conn)
    select_data(conn)
    conn.close()
    print("Program selesai.")

if __name__ == "__main__":
    main()
