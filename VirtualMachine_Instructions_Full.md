sudong hợp hướng dẫn cài đặt và demo máy ảo Ubuntu với Python và MySQL

## 1. Cài đặt Oracle VirtualBox và tạo máy ảo
- Tải Oracle VirtualBox từ trang chủ.
- Tạo máy ảo mới với loại Linux, phiên bản Ubuntu 64-bit.
- Cấu hình RAM 1-2GB, ổ đĩa VDI 20GB.
- Cài Ubuntu bằng file ISO.

## 2. Cài đặt phần mềm cần thiết trong Ubuntu máy ảo
- Mở Terminal máy ảo.
- Chạy lệnh cập nhật hệ thống:
  ```bash
  sudo apt update && sudo apt upgrade
  ```
- Cài Python3 venv nếu chưa có:
  ```bash
  sudo apt install python3-venv
  ```

## 3. Tạo và kích hoạt môi trường ảo Python
- Tạo môi trường ảo:
  ```bash
  python3 -m venv myenv
  ```
- Kích hoạt môi trường ảo:
  ```bash
  source myenv/bin/activate
  ```

## 4. Cài thư viện mysql-connector-python trong môi trường ảo
- Sau khi kích hoạt môi trường ảo, cài thư viện:
  ```bash
  pip install mysql-connector-python
  ```

## 5. Cài đặt MySQL Server trên máy ảo (nếu chưa cài)
- Cài MySQL Server:
  ```bash
  sudo apt install mysql-server
  ```
- Bảo mật MySQL:
  ```bash
  sudo mysql_secure_installation
  ```

## 6. Tạo database, user và bảng dữ liệu demo trong MySQL
- Đăng nhập MySQL:
  ```bash
  sudo mysql -u root -p
  ```
- Tạo database và user:
  ```sql
  CREATE DATABASE demo_db;
  CREATE USER 'demo_user'@'localhost' IDENTIFIED BY 'password123';
  GRANT ALL PRIVILEGES ON demo_db.* TO 'demo_user'@'localhost';
  FLUSH PRIVILEGES;
  ```
- Tạo bảng và thêm dữ liệu:
  ```sql
  USE demo_db;
  CREATE TABLE test_table (
      id INT PRIMARY KEY AUTO_INCREMENT,
      name VARCHAR(50)
  );
  INSERT INTO test_table (name) VALUES ('Test name');
  ```

## 7. Viết và chạy script Python kết nối MySQL
- File `mysql_demo.py` demo:
  ```python
  import mysql.connector

  conn = mysql.connector.connect(
      host="localhost",
      user="demo_user",
      password="password123",
      database="demo_db"
  )

  cursor = conn.cursor()
  cursor.execute("SELECT * FROM test_table")
  rows = cursor.fetchall()

  for row in rows:
      print(row)

  conn.close()
  ```
- Chạy lệnh trong terminal đang kích hoạt môi trường ảo:
  ```bash
  python mysql_demo.py
  ```

---

Nếu cần tau hướng dẫn chi tiết đoạn nào hoặc tạo file script giúp, báo tôi nhé.