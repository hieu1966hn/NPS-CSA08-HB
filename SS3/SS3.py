#### Xây dựng lớp Phân số (Fraction)
class PhanSo:
    ## Hàm khởi tạo
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso

    ## Hàm hiển thị phân số ra màn hình terminal
    def __str__(self):
        return f"{self.tuso}/{self.mauso}"
    

    ## Hàm tìm UCLN
    def find_UCLN(self, a, b):
        smaller = min(abs(a), abs(b)) ## 3/ 6
        ucln = 1 ## mặc định là 1
        for i in range(1, smaller + 1):
            if a % i ==0 and b %i ==0:
                ucln = i ## 1, 3, 
        return ucln
        

    ### Hàm rút gọn phân số: 3/6 => 1/2
    def rutGonPhanSo(self):
        ucln = self.find_UCLN(self.tuso, self.mauso)
        self.tuso = self.tuso // ucln
        self.mauso = self.mauso // ucln
        return PhanSo(self.tuso, self.mauso)


    ### Hàm cộng 2 phân số
    def add(self, other):
        new_tuso = self.tuso * other.mauso + other.tuso * self.mauso
        new_mauso = self.mauso * other.mauso
        result = PhanSo(new_tuso, new_mauso)
        return result

    ### Hàm trừ 2 phân số
    def subtract(self, other):
        new_tuso = self.tuso * other.mauso - other.tuso * self.mauso
        new_mauso = self.mauso * other.mauso
        result = PhanSo(new_tuso, new_mauso)
        return result

    ## Hàm nhân 2 phân số
    def multiply(self, other):
        new_tuso = self.tuso * other.tuso
        new_mauso = self.mauso * other.mauso
        result = PhanSo(new_tuso, new_mauso)
        return result
    
    ## Hàm nhân chia phân số
    def divide(self, other):
        new_tuso = self.tuso * other.mauso
        new_mauso = self.mauso * other.tuso
        result = PhanSo(new_tuso, new_mauso)
        return result


PhanSo1 = PhanSo(3, 2)
PhanSo2 = PhanSo(7, 5)
PhanSo3 = PhanSo(3, 6)

## Rút gọn phân số 3
print(f"Phân số 3 được rút gọn lại là {PhanSo3.rutGonPhanSo()}")

# ### Cộng hai phân số
# print(f"Cộng 2 phân số: {PhanSo1.add(PhanSo2)}")  ### Output:
# ### Trừ hai phân số
# print(f"Trừ 2 phân số: {PhanSo1.subtract(PhanSo2)}")  ### Output:
# ### Nhân hai phân số
# print(f"Nhân 2 phân số: {PhanSo1.multiply(PhanSo2)}")  ### Output:
# ### Chia hai phân số
# print(f"Chia 2 phân số: {PhanSo1.divide(PhanSo2)}")  ### Output:
