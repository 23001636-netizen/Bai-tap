# Hướng dẫn chạy project demo_mysql

## Bước 1: Tạo và kích hoạt môi trường ảo

Mở terminal ở thư mục dự án ("Bai tap") và chạy:

```bash
python -m virtualenv venv
```

Sau đó kích hoạt môi trường ảo:
- Trên Windows cmd:

```bash
venv\Scripts\activate.bat
```

- Trên PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```


## Bước 2: Cài đặt dependencies

Chạy lệnh:

```bash
pip install mysql-connector-python
```

## Bước 3: Chạy demo

Chạy file demo

```bash
python demo_mysql.py
```

## Ghi chú
- Yêu cầu Python 3.11 trở lên
- MySQL server phải đang chạy và có cấu hình phù hợp
- Đảm bảo file `demo_mysql.py` có trong thư mục

Chúc bạn thành công!