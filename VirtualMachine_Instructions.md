# Hướng dẫn cài đặt và tạo máy ảo với Oracle VirtualBox

## 1. Tải và cài đặt Oracle VirtualBox
- Truy cập trang chủ Oracle VirtualBox: https://www.virtualbox.org/wiki/Downloads
- Chọn bản cài đặt phù hợp cho Windows và tải về.
- Mở file cài, làm theo hướng dẫn để cài đặt VirtualBox.

## 2. Tải file ISO cài đặt Ubuntu
- Truy cập https://ubuntu.com/download/desktop
- Tải file ISO bản mới nhất.

## 3. Tạo máy ảo mới
- Mở Oracle VirtualBox.
- Nhấn nút "New" để tạo máy ảo.
- Đặt tên máy ảo, chọn loại "Linux", phiên bản "Ubuntu (64-bit)".
- Cấu hình RAM (1-2GB là đủ cho demo).
- Tạo một ổ đĩa ảo mới (VD: 20GB, VDI, dynamically allocated).

## 4. Cài Ubuntu trên máy ảo
- Bật máy ảo mới tạo.
- Chọn file ISO Ubuntu đã tải khi máy ảo hỏi ổ đĩa cài.
- Thực hiện theo hướng dẫn cài đặt Ubuntu.

## 5. Cài thêm phần mềm cần thiết trên Ubuntu máy ảo
- Cập nhật hệ thống:
  ```bash
  sudo apt update && sudo apt upgrade
  ```
- Cài Python, MySQL server hoặc các phần mềm demo cần thiết.

## 6. Demo và ghi chú
- Thực hành demo Python kết nối MySQL trong máy ảo.
- Ghi chú các bước bạn làm.
- Chụp ảnh hoặc quay video nếu cần.

---

Bạn muốn thêm hướng dẫn cụ thể các lệnh cài Python, MySQL hoặc viết script demo trên máy ảo Ubuntu không?