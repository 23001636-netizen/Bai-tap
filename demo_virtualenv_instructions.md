# Demo tạo và sử dụng môi trường ảo Python với virtualenv

## 1. Tạo Virtual Environment
Mở terminal trong thư mục dự án (ví dụ `c:/Users/ACER/Desktop/Bai tap`)

Chạy lệnh:

```
python -m virtualenv venv
```

Lệnh này tạo một folder `venv` chứa môi trường ảo.


## 2. Kích hoạt Virtual Environment

- **Windows (PowerShell):**

```
.\venv\Scripts\Activate.ps1
```

- **Windows (Command Prompt):**

```
.\venv\Scripts\activate.bat
```

- **Linux/macOS:**

```
source venv/bin/activate
```


## 3. Cài đặt thư viện bên trong Virtual Environment

Khi môi trường ảo đã active (biến môi trường thay đổi), chạy lệnh:

```
pip install mysql-connector-python
```

hoặc các package khác.


## 4. Chạy file demo MySQL

Chạy file Python đã tạo `demo_mysql.py`:

```
python demo_mysql.py
```


## 5. Tắt môi trường ảo khi xong

```
deactivate
```


---

Bạn có thể dùng file `.md` này làm tài liệu làm demo môi trường ảo cho bài tập của bạn.