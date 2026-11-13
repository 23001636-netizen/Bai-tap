import mysql.connector
from mysql.connector import Error

try:
    # Kết nối tới MySQL
    connection = mysql.connector.connect(
        host='localhost',
        user='root',  # bạn đổi user nếu cần
        password='Minhtu2005'  # nhập mật khẩu bạn đặt cho root trong cài MySQL
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Tạo database demo nếu chưa có
        cursor.execute("CREATE DATABASE IF NOT EXISTS demo_db")
        cursor.execute("USE demo_db")

        # Tạo bảng users
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                age INT
            )
        """)

        # Chèn dữ liệu
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 30))
        connection.commit()

        # Lấy dữ liệu
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        print("Users in database:")
        for row in rows:
            print(row)

except Error as e:
    print("Error while connecting MySQL", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
