Buổi 7: Các hàm có sẵn trong SQL
- Kiến thức buổi 6: 
+ Read: select, from, where, limit, offset

- Kiến thức buổi 7: 
+ CREATE DATABASE: Tạo cơ sở dữ liệu (DATABASE)
+ USE ten_database: Sau khi tạo => chọn cơ sở dữ liệu để sử dụng
+ CREATE TABLE ten_bang (...): Tạo bảng mới trong cơ sở dữ liệu
+ INSERT INTO ten_bang(cot1, cot2, ...) VALUES (gia_tri1, gia_tri2, ...); Thêm dữ liệu vào bảng
+ SELECT cot1, cot2, .. FROM ten_bang; Để lấy dữ liệu từ bảng
+ UPDATE ten_bang SET cot1 = gia_tri_moi WHERE dieu_kien; Cập nhật dữ liệu trong bảng
+ DELETE FROM ten_bang WHERE dieu_kien; 
+ ALTER TABLE ten_bang ADD cot_moi kieu_du_lieu; Thêm cột vào bảng
+ ALTER TABLE ten_bang DROP COLUMN cot; Xóa cột khỏi bảng
+ DROP TABLE ten_bang; Xóa bảng
+ DROP DATABASE ten_database; Xóa cơ sở dữ liệu
+ BETWEEN xx AND xx;

+ COUNT(): Đếm số lượng bản ghi hoặc giá trị không trống
SELECT COUNT(*) FROM ten_bang;

+ GROUP BY: Để gom nhóm các bản ghi có cùng giá trị trong một hoặc nhiều cột, thường kết hợp với các hàm như COUNT(), SUM(), AVG(), MAX(), MIN().


+ AVG(): Sử dụng để tính giá trị trung bình của một cột chứa dữ liệu số(như số lượng, giá cả, điểm số, ...)
SELECT AVG(ten_cot) FROM ten_bang 

+ DISTINCT: Sử dụng để loại bỏ các giá trị trùng lặp trong kết quả truy vấn, chỉ lấy các giá trị duy nhất từ một hoặc nhiều cột.
SELECT DISTINCT ten_cot FROM ten_bang;
