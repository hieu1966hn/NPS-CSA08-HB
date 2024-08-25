Ôn tập kiến thức buổi 1:
- Tìm hiểu về OOP
- Khai báo Class
- Thuộc tính (attribute) và phương thức (method)
+ Giả sử tạo ra một class con người
+ attribute thể hiện những đặc điểm của con người: màu da, tay, chân, màu tóc, ...
+ method: đi, nói, cảm xúc, ...
- Tên thuộc tính: bắt đầu bằng _
- Hàm init: 
+ def __init__(self): hàm constructor: self ám chỉ instance của class



Buổi học số 2: Special Methods và kế thừa
- Kế thừa (Inheritance):là một trong bốn nguyên lý cơ bản của lập trình hướng đối tượng (OOP). Kế thừa cho phép bạn tạo ra một lớp mới (Gọi là lớp con hoặc subclass) dựa trên một lớp hiện có (gọi là lớp cha hoặc superclass). Lớp con thừa hưởng tất cả các thuộc tính và phương thức của lớp cha nhưng cũng có thể thêm hoặc ghi đè các thuộc tính và phương thức của riêng lớp con.

Cú pháp cơ bản của kế thừa:
class LớpCha:
    def __init__(self, thuộc_tính_cha):
        self.thuộc_tính_cha = thuộc_tính_cha
    
    def phương_thức_cha(self):
        print("Đây là phương thức của lớp cha")

class LớpCon(LớpCha):
    def __init__(self, thuộc_tính_cha, thuộc_tính_con):
        # Gọi hàm khởi tạo của lớp cha
        super().__init__(thuộc_tính_cha)
        self.thuộc_tính_com = thuộc_tính_con
    def phương_thức_con(self):
        print("Đây là phương thức của lớp con")



super(): Được sử dụng để gọi hàm khởi tạo của lớp cha (Animal). Điều này giúp bạn không cần phải viết lại toàn bộ mã liên quan đến việc khởi tạo các thuộc tính chung giữa các lớp con.


Đề bài thực hành: Có một lớp Animal (Động vật) và bạn muốn tạo các lớp con từ lớp này như: Dog, Cat. Cả 2 lớp này đều thừa hưởng các thuộc tính và phương thức từ lớp Animal.



Kế thừa nhiều lớp: PYthon cho phép kế thừa từ nhiều lớp cha. Ví dụ: 
class A:
    def method_a(self):
        print("A")
    
class B:
    def method_b(self):
        print("B")

class C(A,B):
    pass

c = c()
c.method_a() #A
c.method_b() #B