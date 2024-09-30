Buổi 5: Giới thiệu về cơ sở dữ liệu
- Tầm quan trọng của dữ liệu
- Tại sao phải lưu trữ dữ liệu
- Cơ sở dữ liệu có quan hệ
- Làm quen với SQL


Dữ liệu: Từ dữ liệu mà chúng ta có thể phân tích được các xu hướng...
- Dữ liệu quan hệ: 
- Dữ liệu không quan hệ: json, graph, hash,... 

Hệ thống quản lý dữ liệu (DBMS): nơi tương tác giữa người dùng và dữ liệu.

Dữ liệu + Hệ thống quản lý dữ liệu => cơ sở dữ liệu



CSDL quan hệ: 
- Dữ liệu được biểu diễn thành các bảng có cột và dòng (hàng). Giống như bảng trong Excel, có các cột và dòng.
+ Mỗi dòng (một bộ/ tuple) đại diện cho một đối tượng (mục thông tin). VD: Mỗi dòng có thể đại diện cho một học sinh trong lớp.
+ Mỗi cột là một thuộc tính của đối tượng

- Tập hợp các bảng thì được gọi là: một cơ sở dữ liệu quan hệ. Nhiều bảng kết nối với nhau qua các mối quan hệ, chúng ta gọi nó là cơ sở dữ liệu quan hệ.
- Lược đồ quan hệ: Là cách mà các bảng trong CSDL được tổ chức và kết nối với nhau.
+ Khóa quan hệ: Là một thuộc tính hoặc nhóm thuộc tính giúp xác định duy nhất các dòng trong bảng.
    * Khóa chính (Primary Key): Là cột hoặc nhóm cột giúp phân biệt mỗi dòng trong bảng. Ví dụ, trong bảng học sinh, "Mã học sinh" có thể là chìa khóa chính vì mỗi học sinh có một mã riêng.
    * Khóa ngoại (Foreign Key): Là cột kết nối 2 bảng lại với nhau. Nó thường là khóa chính từ bảng khác. Ví dụ, "Mã lớp" trong bảng học sinh có thể là khóa ngoại kết nối với bảng "Lớp học".

+ one - many relationship: Quan hệ một - nhiều => Một đối tượng trong bảng này có thể liên quan đến nhiều đối tượng trong bảng khác. Ví dụ, một lớp có nhiều học sinh.
+ many- many relationship: Quan hệ nhiều - nhiều: Một đối tượng trong bảng này có thể liên quan đến nhiều đối tượng trong bảng khác, và ngược lại. Ví dụ, một học sinh có thể tham gia nhiều CLB và một CLB có thể có nhiều học sinh.
+ one - one relationship: Quan hệ một - một: Một đối tượng trong bảng này chỉ liên quan đến một đối tượng duy nhất trong bảng khác. Ví dụ, mỗi học sinh chỉ có một học bạ.




SQL: 
- Cài đặt MySQL
- Cài đặt MySQL workbench
- Cách tạo table: create table
+ Giới thiệu các kiểu dữ liệu:  INT, VARCHAR, BINARY, DATE, TIMESTAMP, ...
+ Thêm, xóa hàng vào table: insert, delete, alter