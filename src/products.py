import mysql.connector

mysql = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567890",
    database="tienda_proyecto"
)
def get_products():
    mysql_cursor = mysql.cursor(dictionary=True)
    mysql_cursor.execute("SELECT * FROM informatica")
    products = mysql_cursor.fetchall()
    mysql_cursor.close()
    mysql.close()
    return products

products = get_products()