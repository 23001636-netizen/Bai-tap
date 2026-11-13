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

## Bước 4: Chạy MySQL trong Docker container (nếu dùng Docker)

- Đảm bảo Docker Desktop đang chạy (xem biểu tượng Docker đang xanh)
- Kéo image MySQL chính thức:
	```bash
	docker pull mysql:latest
	```
- Chạy container MySQL với cấu hình:
	```bash
	docker run --name mysql-demo -e MYSQL_ROOT_PASSWORD=Minhtu2005 -d -p 3306:3306 mysql:latest
	```
- Kiểm tra container đang chạy:
	```bash
	docker ps
	```
## Ghi chú chung
- Port mặc định MySQL là 3306. Nếu bị trùng cổng với MySQL cài đặt trên máy, có thể dùng cổng khác như 3307:3307:3306
- Kết nối MySQL trong Python dùng host localhost, port 3306 (hoặc cổng bạn ánh xạ), user root, password là mật khẩu bạn chọn khi chạy container.
