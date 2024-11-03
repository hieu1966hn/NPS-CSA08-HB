Buổi 12: Trực quan hóa dữ liệu với MATPLOTLIB
- Thư viện Matplotlib
- Các hàm hỗ trợ thông dụng (bảng hàm và công dụng)
- Giới thiệu về các biểu đồ thông dụng

Thư viện Matplotlib: Là một thư viện để vẽ đồ thị trong Python, thường được sử dụng kết hợp các thư viện NumPy và Pandas.

Cài đặt thư viện Matplotlib


2. Ví dụ với biểu đồ đường
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()

Giải thích: 
- x: là dữ liệu trục hoành và y là dữ liệu trục tung.
- plt.plot(x, y) sẽ vẽ một biểu đồ đường kết nối các điểm (1,10), (2, 20), ..

3. Hàm legend(), label()
- Công dụng: label() đặt tên trục và dữ liệu, trong khi legend() hiển thị chú thích cho biểu đồ, giúp người xem dễ hiểu dữ liệu.
- Cú pháp: 
plt.plot(x, y, label='Dữ liệu mẫu')
plt.legend()

4. Hàm show()
- Công dụng: hiển thị biểu đồ sau khi đã được thiết lập các thuộc tính.
- Cú pháp: plt.show()


5. Hàm title()
- Công dụng: Đặt tiêu đề cho biểu đồ
- Cú pháp: plt.title('Tiêu đề biểu đồ')

6. Hàm figure()
- Công dụng: tạo khung hình mới cho biểu đồ, cho phép bạn thiết lập kích thước và các thuộc tính khác.
- Cú pháp: 
plt.figure(figsize=(width, height))
- Ví dụ: 

7. Tạo tên cột x, y cho graph
- Công dụng: Đặt tên cho các cột trong biểu đồ giúp người dùng hiểu rõ hơn về dữ liệu
- Cú pháp: 
plt.xlabel('Tên trục x')
plt.ylabel('Tên trục y')
- Ví dụ: Đã ví dụ ở những mục 1, 2..

8. Vẽ biểu đồ hình cột với hàm hist()
- Công dụng: tạo biểu đồ cột (histogram), biểu diễn tần suất dữ liệu
- Cú pháp: 
plt.hist(data, bins=n)
- Ví dụ: 
- Giải thích: 
+ data: là tập dữ liệu
+ bins=4: chia thành 4 cột dựa trên tần suất của các giá trị từ 1 đến 4

9. Vẽ biểu đồ tròn với hàm pie()
- Công dụng: pie() tạo biểu đồ tròn (pia chart), biểu diễn tỉ lệ từng phần trong tổng thể
- Cú pháp: 
plt.pie(sizes, labels=labels)
- Ví dụ: 
- Giải thích: 
+ sizes: tỉ lệ các phần
+ labels: tên từng phần trong biểu đồ tròn

10. Export biểu đồ
- Công dụng: Lưu biểu đồ thành file hình ảnh để sử dụng hoặc chia sẻ
- Cú pháp: 
plt.savefig('tên_file.png')
- Ví dụ: 



Đề bài thực hành: 
Bài tập 1: Vẽ biểu đồ đường cơ bản
Mô tả: Tạo biểu đồ đường thể hiện nhiệt độ trung bình trong tuần.
Yêu cầu:
- Sử dụng plot() để vẽ biểu đồ đường.
- Đặt nhãn cho trục x (Ngày) và trục y (Nhiệt độ).
- Đặt tiêu đề cho biểu đồ và hiển thị chú thích (legend).

Dữ liệu mẫu:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperatures = [25, 27, 26, 28, 29, 30, 31]



Bài tập 2: Vẽ biểu đồ cột và biểu đồ tròn
- Mô tả: Vẽ biểu đồ thể hiện số lượng học sinh thích các môn học khác nhau.
- Yêu cầu:
+ Vẽ biểu đồ cột với dữ liệu số lượng học sinh thích từng môn học.
+ Tạo biểu đồ tròn từ cùng dữ liệu để so sánh tỉ lệ.
+ Thêm nhãn cho các trục, tiêu đề và lưu biểu đồ thành file hình ảnh.

Dữ liệu mẫu:
subjects = ["Math", "Science", "History", "Art", "PE"]
students = [15, 20, 10, 5, 25]


Bài tập 3: Vẽ biểu đồ Histogram
- Mô tả: Tạo biểu đồ histogram thể hiện phân phối điểm số của 100 học sinh trong một kỳ thi.
- Yêu cầu:
+ Sử dụng hist() để vẽ biểu đồ histogram với các khoảng điểm (bins) chia từ 0 đến 100, mỗi khoảng cách nhau 10 điểm.
+ Đặt tiêu đề và nhãn cho các trục.
+ Thêm chú thích giải thích ý nghĩa biểu đồ.

Dữ liệu mẫu:
import numpy as np
scores = np.random.randint(0, 101, 100)  # Tạo ngẫu nhiên điểm số từ 0 đến 100 cho 100 học sinh
  
