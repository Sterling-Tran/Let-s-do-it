# Let's do it - Ứng dụng thiết lập hoàn thành Mục tiêu, lấy cảm hừng từ [Go fucking do it](https://gofuckingdoit.com/?ref=access)  

Goals là một ứng dụng web được xây dựng bằng Django giúp người dùng quản lý và theo dõi các mục tiêu cá nhân của mình. Ứng dụng cung cấp các công cụ để tạo, theo dõi và quản lý mục tiêu, cũng như thiết lập kế hoạch để đạt được các mục tiêu đó.

## Các tính năng chính
- **Tạo mục tiêu**: Tạo mục tiêu.
- **Theo dõi tiến độ**: Theo dõi tiến độ đạt được mục tiêu theo thời gian qua email.
- **Nhắc nhở**: Nhắc nhở hoàn thành mục tiêu khi tới hạn.
- **Chia sẻ mục tiêu**: Chia sẻ mục tiêu với người khác qua email.

## Công nghệ sử dụng

- **Django**: Phiên bản 5.x
- **Bootstrap 5**: Giao diện người dùng
- **HTML, CSS, JavaScript**: Frontend
- **SQL Lite**: database 

## Cài đặt

1. **Clone repository**

   ```bash
   git clone https://github.com/Sterling-Tran/Let-s-do-it.git
   
2. **Chuyển đến thư mục dự án**
    ```bash
    cd letdoit
3. **Tạo và kích hoạt môi trường ảo**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows: venv\Scripts\activate
4. **Cài đặt các phụ thuộc**
    ```bash
    pip install -r requirements.txt

5. **Thực hiện các migration**
    ```bash
    python manage.py migrate
6. **Khởi chạy ứng dụng**
    ```bash
    python manage.py runserver
7. **Truy cập ứng dụng tại**
    ```bash
    http://localhost:8000
8. **Truy cập admin panel**
    ```bash
    http://localhost:8000/admin
