Nội dung buổi học số 3
- Ôn tập về kiến thức OOP với bài luyện tập: Phân số
- Bước đầu setup và lập trình game: Snake => trò trơi cổ điển, người chơi điều khiển một con rắn di chuyển xung quanh màn hình để ăn thức ăn và trở nên dài hơn. Người chơi phải tránh đụng phải tường hoặc tự cắn đuôi của mình.

Giới thiệu thêm các game có thể lập trình với pygame: Breakout, tic-tac-toe, Flappy Bird, Maze, ... Hangman.





Đề bài thực hành: 
  
Đề bài 1: Quản lý hệ thống nhân sự
Yêu cầu: Viết một chương trình mô phỏng hệ thống quản lý nhân sự với các class sau:

Person: Chứa các thuộc tính chung cho mọi người như tên, tuổi, địa chỉ.
Employee: Kế thừa từ Person, có thêm thuộc tính job_title và salary.
Manager: Kế thừa từ Employee, có thêm thuộc tính department.
Company: Chứa danh sách các nhân viên và quản lý, có phương thức để thêm, xóa, và tìm kiếm nhân viên theo tên.

Kết quả mong đợi:
Hệ thống có thể quản lý nhân viên và quản lý, in ra thông tin từng người theo cấu trúc lớp.




Đề bài 2: Hệ thống ngân hàng
Yêu cầu: Xây dựng một hệ thống ngân hàng có các class:

Account: Chứa thông tin cơ bản về tài khoản như số dư, chủ tài khoản, và các phương thức như gửi tiền (deposit) và rút tiền (withdraw).
SavingsAccount và CheckingAccount: Kế thừa từ Account.
SavingsAccount có thêm lãi suất, phương thức tính lãi.
CheckingAccount có phí giao dịch và giới hạn số lần giao dịch.
Sử dụng tính đa hình để xử lý việc giao dịch cho cả hai loại tài khoản, tính toán lãi suất cho SavingsAccount và tính phí giao dịch cho CheckingAccount.

Kết quả mong đợi:
Mô phỏng hoạt động ngân hàng với các giao dịch khác nhau và in ra số dư sau mỗi giao dịch.




Đề bài 3: Đa kế thừa trong hệ thống giao thông
Yêu cầu: Xây dựng một hệ thống giao thông với đa kế thừa:

Vehicle: Là lớp cha cho mọi phương tiện, có thuộc tính tốc độ và phương thức di chuyển.
Car và Bicycle: Kế thừa từ Vehicle.
Car có thêm thuộc tính số ghế.
Bicycle có thêm thuộc tính số bánh xe.
HybridVehicle: Kế thừa từ cả Car và Bicycle, có thể chuyển đổi giữa chế độ chạy xe đạp và xe hơi.

Kết quả mong đợi:
Mô phỏng hệ thống phương tiện, cho phép phương tiện di chuyển và in ra thông tin từng loại phương tiện khi sử dụng đa kế thừa.