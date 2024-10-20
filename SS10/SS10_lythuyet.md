Buổi 10: Truy xuất dữ liệu với Pandas

- tail(n) -> Trả về n hàng cuối cùng
- var_name['colmn_name'] -> Trả về tất cả dữ liệu ở cột column_name 
- var_name['column_name'][i] -> Trả về giá trị ở vị trí thứ i của cột column_name 


1. Truy xuất dữ liệu trong DF (tương tự List và Dictionary)
- Truy xuất một cột: 
+ Cú pháp: var_name['colmn_name'] -> Trả về tất cả dữ liệu ở cột column_name trong DF

- Truy xuất bằng chỉ số (index):
+ Cú pháp: var_name[index]
+ Công dụng: Truy xuất các giá trị dựa trên chỉ số hàng


2. Truy xuất nhiều cột
- Cú pháp: var_name[['column_name_1', 'column_name_2']]
- Công dụng: Truy xuất nhiều cột từ DF cùng một lúc.

3. Truy xuất một giá trị cụ thể trong cột
- Cú pháp: var_name['tên_cột'][index]
- Công dụng: Truy xuất một giá trị cụ thể từ một cột dựa trên chỉ số hàng (index)

4. Boolean Indexing
- Cú pháp: var_name[var_name['tên_cột] == giá_trị]
- Công dụng: Truy xất các hàng thỏa mãn điều kiện cho trước. Boolean Indexing trả về một DF hoặc Series chỉ chứa các hàng có giá trị thỏa mãn điều kiện.

5. Hàm loc[] & iloc[]
- loc[]
+ Cú pháp: var_name.loc[row_label, col_label]
+ Công dụng: Truy xuất dữ liệu dựa trên nhãn hàng và cột. loc[] sử dụng nhãn để xác định hàng và cột.

- iloc[]
+ Cú pháp: var_name.iloc[row_index, col_index]
+ Công dụng: Truy xuất dữ liệu dựa trên chỉ số hàng và cột. iloc[] sử dụng chỉ số (index) thay vì nhãn.

=>> 
Loc: Dùng khi biết giá trị cụ thể. 
Iloc: Dùng khi biết vị trí cụ thể.






DF: Dữ liệu tỉnh và thành phố trực thuộc Trung ương ở Việt Nam
- col_list: Một danh sách chữa các string là danh sách tên các cột
- province_list: Một ds chữa các tuple là thông tin trên từng dòng

Yêu cầu: từ 2 biến trên, hãy sử dụng thư viện pandas để khởi tạo Data Frame (df) chứa đầy đủ dữ liệu đã cho.


#### Bài 1: Từ DF df đã tạo, dựa vào các thuộc tính và phương thức trên DF để tìm:
- Số dòng và số cột trong df
- Kích thước lưu trữ của df trong bộ nhớ
- Kiểu dữ liệu của từng cột trong df


#### Bài 2
- Lưu dữ liệu trong df đã tạo vào file provinces.csv theo định dạng csv
Ghi chú: Nhớ truyền tham số index = False vào phương thức to_csv() trên DF
- Đọc dữ liệu từ file provinces.csv đã lưu vào biến province_df. Dữ liệu trong province_df cần khớp hoàn toàn với df.




### Bài 3: Trích xuất tên các tỉnh và thành phố trong df để in ra màn hình theo định dạng sau: 

list of provinces and cities: Thành phố Hà Nội, Tỉnh Hà Giang, ...