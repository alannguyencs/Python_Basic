import psycopg2
"""
1. Connect to a database
2. Create a cursor object
3. Write an SQL query
4. Commit changes
5. Close database connection
"""

def create_table():
    conn = psycopg2.connect("dbname = 'sample_db' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()

def insert(item, quantity, price):
    conn = psycopg2.connect(
        "dbname = 'sample_db' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))
    conn.commit()
    conn.close()

# insert('Coffee cup', 1, 50)

def view():
    conn = psycopg2.connect(
        "dbname = 'sample_db' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

# print (view())
def delete(item):
    conn = psycopg2.connect(
        "dbname = 'sample_db' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    conn.commit()
    conn.close()


# delete('Wine Blass')
# print (view())

def update(quantity, price, item):
    conn = psycopg2.connect(
        "dbname = 'sample_db' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432' ")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    conn.commit()
    conn.close()


create_table()
# insert("Apple", 1, 2)
# insert("Orange", 2, 3)
update(3,5,'Apple')
print (view())
# update(11, 6, 'Water Glass')
# print (view())