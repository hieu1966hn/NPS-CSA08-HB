Buổi 9: Tìm hiểu về thư viện Pandas
1. Cài đặt pip3 và pandas (done)
2. Sử dụng thư viện pandas với import (done)
3. Giới thiệu: dataframe và series 
4. Giới thiệu các hàm đọc file của pandas();
5. Các phương thức cơ bản của Pandas


So sánh:
- Series: Một cột (1 chiều)
- DataFrame: Nhiều cột (2 chiều), tương tự như một dictionary với key là tên cột và value là series.


Tạo Data bằng hàm Series() và DataFrame(): Đã có ví dụ


Giới thiệu các hàm đọc file của Pandas.
- read_csv(): Đọc dữ liệu từ file CSV.
df = pd.read_csv('ten_file.csv')
print(df.head())

Chú ý: head() để xem trước vài dòng đầu tiên của dữ liệu.

- read_excel(): Đọc dữ liệu từ file Excel
df = pd.read_excel('ten_file.xlsx')
print(df.info())

- head(): Xem 5 dòng đầu tiên của DF

- info(): Xem thông tin chung về DF, bao gồm số lượng dòng, cột và kiểu dữ liệu.

- dtypes: Xem kiểu dữ liệu của từng cột trong DF


Export Data bằng Pandas
1. Xuất ra file CSV với to_csv()
Ví dụ: Xuất DataFrame thành file CSV
df.to_csv('output.csv', index = False)

Giải thích: Tham số index = False sẽ loại bỏ cột chỉ mục khi xuất ra file.



Đề bài thực hành: 
1. Tạo một DataFrame chứa thông tin về tên, tuổi, điểm số của từng học viên lớp mình.
2. Đọc dữ liệu từ 1 file CSV hoặc excel có sẵn (Đọc file: output.csv)
3. Thực hiện thao tác xem trước dữ liệu với head(), xem kiểu dữ liệu với dtypes, và kiểm tra thông tin chung với info().
4. Xuất dữ liệu ra file csv (bài 1).

Nâng cao hơn