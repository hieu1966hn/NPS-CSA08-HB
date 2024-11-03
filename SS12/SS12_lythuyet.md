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