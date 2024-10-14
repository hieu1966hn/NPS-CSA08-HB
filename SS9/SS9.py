# Kiểm tra thử xem có Pandas chưa nhé?
import pandas as pd ## Viết tắt lại tên thư viện để dễ dùng hơn.

## Ví dụ 1 series trong pandas
# csa09 = [
#     ['STT', "Mhv", "Name", "Age"],
#     [1, "P_Long", "Long", 18],
#     [2, "D_Anh", "Đức Anh", 16],
#     [3, "V_Khang", "Khang", 14],
#     [4, "T_Hung", "Thái Hùng", 17],
# ]

# Mhv = [["P_Long"], ["D_Anh"], ["V_Khang"], ["T_Hung"]]

# csa09 = {
#     'Mhv': [["P_Long"], ["D_Anh"], ["V_Khang"], ["T_Hung"]],
# }


#### Ví dụ => Series là cấu trúc một chiều.
# STT = pd.Series([1,2,3,4])
# print(STT)

### Ví dụ với DataFrame: DF là cấu trúc hai chiều (rows và columns)
# data = {
#     'Name': ['Long', "Hùng", 'Khang', "Đức Anh"],
#     "Age": [18, 17, 14, 16]
# }

# df = pd.DataFrame(data)
# print(df)


#### Tạo Data bằng hàm Series() và DataFrame(): Ví dụ bên trên đã đầy đủ
# df.to_csv('csa09.csv', index=False) ### Xuất DF ra file CSV


#### Chữa bài thực hành
data = {
    'Name': ['Long', "Hùng", 'Khang', "Đức Anh"],
    "Age": [18, 17, 14, 16],
    "Point": [8.5, 7.0, 10, 9],
}

## Tạo DF từ dữ liệu trên
df_Students = pd.DataFrame(data)
## Hiển thị DF
# print(df_Students)

### Yêu cầu 2: 
## Đọc dữ liệu từ file CSV
df_from_csv = pd.read_csv('./SS9/csa09.csv')

## Hiển thị DF đã đọc  từ file CSV
# print(df_from_csv.head()) # Xem trước 5 dòng dữ liệu đầu tiên

### Yêu cầu 3: 
## Kiểm tra KDL với dtypes: Kiểm tra KDL từng cột
# print(df_from_csv.dtypes)

## Xem thông tin chung về DataFrame với info()
# print(df_from_csv.info())


### Yêu cầu 4: Xuất dữ liệu ra File CSV
df_Students.to_csv('./SS9/output_students.csv', index=False)
print("Dữ liệu đã được xuất ra file output_students.csv")