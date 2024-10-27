import pandas as pd

col_list = ['Name', 'Division', 'Region', 'Area', 'Population']
province_list = [
 ('Thành phố Hà Nội', 'Thành phố Trung ương', 'Đồng bằng sông Hồng', 3358.6, 8093.9),
 ('Tỉnh Hà Giang', 'Tỉnh', 'Đông Bắc Bộ', 7929.5, 858.1),
 ('Tỉnh Cao Bằng', 'Tỉnh', 'Đông Bắc Bộ', 6700.3, 530.9),
 ('Tỉnh Bắc Kạn', 'Tỉnh', 'Đông Bắc Bộ', 4860.0, 314.4),
 ('Tỉnh Tuyên Quang', 'Tỉnh', 'Đông Bắc Bộ', 5867.9, 786.3),
 ('Tỉnh Lào Cai', 'Tỉnh', 'Tây Bắc Bộ', 6364.0, 733.3),
 ('Tỉnh Điện Biên', 'Tỉnh', 'Tây Bắc Bộ', 9541.3, 601.7),
 ('Tỉnh Lai Châu', 'Tỉnh', 'Tây Bắc Bộ', 9068.8, 462.6),
 ('Tỉnh Sơn La', 'Tỉnh', 'Tây Bắc Bộ', 14123.5, 1252.7),
 ('Tỉnh Yên Bái', 'Tỉnh', 'Tây Bắc Bộ', 6887.5, 823.0),
 ('Tỉnh Hoà Bình', 'Tỉnh', 'Tây Bắc Bộ', 4590.6, 855.8),
 ('Tỉnh Thái Nguyên', 'Tỉnh', 'Đông Bắc Bộ', 3526.6, 1290.9),
 ('Tỉnh Lạng Sơn', 'Tỉnh', 'Đông Bắc Bộ', 8310.1, 782.8),
 ('Tỉnh Quảng Ninh', 'Tỉnh', 'Đông Bắc Bộ', 6178.2, 1324.8),
 ('Tỉnh Bắc Giang', 'Tỉnh', 'Đông Bắc Bộ', 3895.6, 1810.4),
 ('Tỉnh Phú Thọ', 'Tỉnh', 'Đông Bắc Bộ', 3534.6, 1466.4),
 ('Tỉnh Vĩnh Phúc', 'Tỉnh', 'Đồng bằng sông Hồng', 1235.9, 1154.8),
 ('Tỉnh Bắc Ninh', 'Tỉnh', 'Đồng bằng sông Hồng', 822.7, 1378.6),
 ('Tỉnh Hải Dương', 'Tỉnh', 'Đồng bằng sông Hồng', 1668.2, 1896.9),
 ('Thành phố Hải Phòng', 'Thành phố Trung ương', 'Đồng bằng sông Hồng', 1561.8, 2033.3),
 ('Tỉnh Hưng Yên', 'Tỉnh', 'Đồng bằng sông Hồng', 930.2, 1255.8),
 ('Tỉnh Thái Bình', 'Tỉnh', 'Đồng bằng sông Hồng', 1586.4, 1862.2),
 ('Tỉnh Hà Nam', 'Tỉnh', 'Đồng bằng sông Hồng', 861.9, 854.5),
 ('Tỉnh Nam Định', 'Tỉnh', 'Đồng bằng sông Hồng', 1668.6, 1780.9),
 ('Tỉnh Ninh Bình', 'Tỉnh', 'Đồng bằng sông Hồng', 1386.8, 984.5),
 ('Tỉnh Thanh Hóa', 'Tỉnh', 'Bắc Trung Bộ', 11114.6, 3645.8),
 ('Tỉnh Nghệ An', 'Tỉnh', 'Bắc Trung Bộ', 16481.4, 3337.2),
 ('Tỉnh Hà Tĩnh', 'Tỉnh', 'Bắc Trung Bộ', 5990.7, 1290.3),
 ('Tỉnh Quảng Bình', 'Tỉnh', 'Bắc Trung Bộ', 8000.0, 896.6),
 ('Tỉnh Quảng Trị', 'Tỉnh', 'Bắc Trung Bộ', 4621.7, 633.4),
 ('Tỉnh Thừa Thiên Huế', 'Tỉnh', 'Bắc Trung Bộ', 4902.4, 1129.5),
 ('Thành phố Đà Nẵng', 'Thành phố Trung ương', 'Nam Trung Bộ', 1284.9, 1141.1),
 ('Tỉnh Quảng Nam', 'Tỉnh', 'Nam Trung Bộ', 10574.7, 1497.5),
 ('Tỉnh Quảng Ngãi', 'Tỉnh', 'Nam Trung Bộ', 5155.8, 1231.9),
 ('Tỉnh Bình Định', 'Tỉnh', 'Nam Trung Bộ', 6066.2, 1487.8),
 ('Tỉnh Phú Yên', 'Tỉnh', 'Nam Trung Bộ', 5023.4, 873.2),
 ('Tỉnh Khánh Hòa', 'Tỉnh', 'Nam Trung Bộ', 5137.8, 1232.8),
 ('Tỉnh Ninh Thuận', 'Tỉnh', 'Nam Trung Bộ', 3355.3, 591.0),
 ('Tỉnh Bình Thuận', 'Tỉnh', 'Nam Trung Bộ', 7943.9, 1232.3),
 ('Tỉnh Kon Tum', 'Tỉnh', 'Tây Nguyên', 9674.2, 543.4),
 ('Tỉnh Gia Lai', 'Tỉnh', 'Tây Nguyên', 15511.0, 1520.2),
 ('Tỉnh Đắk Lắk', 'Tỉnh', 'Tây Nguyên', 13030.5, 1872.6),
 ('Tỉnh Đắk Nông', 'Tỉnh', 'Tây Nguyên', 6509.3, 625.8),
 ('Tỉnh Lâm Đồng', 'Tỉnh', 'Tây Nguyên', 9783.3, 1299.3),
 ('Tỉnh Bình Phước', 'Tỉnh', 'Đông Nam Bộ', 6876.8, 997.8),
 ('Tỉnh Tây Ninh', 'Tỉnh', 'Đông Nam Bộ', 4041.3, 1171.7),
 ('Tỉnh Bình Dương', 'Tỉnh', 'Đông Nam Bộ', 2694.6, 2456.3),
 ('Tỉnh Đồng Nai', 'Tỉnh', 'Đông Nam Bộ', 5863.6, 3113.7),
 ('Tỉnh Bà Rịa - Vũng Tàu', 'Tỉnh', 'Đông Nam Bộ', 1981.0, 1152.2),
 ('Thành phố Hồ Chí Minh', 'Thành phố Trung ương', 'Đông Nam Bộ', 2061.4, 9038.6),
 ('Tỉnh Long An', 'Tỉnh', 'Đồng bằng sông Cửu Long', 4494.9, 1695.1),
 ('Tỉnh Tiền Giang', 'Tỉnh', 'Đồng bằng sông Cửu Long', 2510.6, 1766.3),
 ('Tỉnh Bến Tre', 'Tỉnh', 'Đồng bằng sông Cửu Long', 2394.8, 1289.1),
 ('Tỉnh Trà Vinh', 'Tỉnh', 'Đồng bằng sông Cửu Long', 2358.3, 1009.3),
 ('Tỉnh Vĩnh Long', 'Tỉnh', 'Đồng bằng sông Cửu Long', 1525.7, 1022.6),
 ('Tỉnh Đồng Tháp', 'Tỉnh', 'Đồng bằng sông Cửu Long', 3383.8, 1598.8),
 ('Tỉnh An Giang', 'Tỉnh', 'Đồng bằng sông Cửu Long', 3536.7, 1907.4),
 ('Tỉnh Kiên Giang', 'Tỉnh', 'Đồng bằng sông Cửu Long', 6348.8, 1723.7),
 ('Thành phố Cần Thơ', 'Thành phố Trung ương', 'Đồng bằng sông Cửu Long', 1439.0, 1236.0),
 ('Tỉnh Hậu Giang', 'Tỉnh', 'Đồng bằng sông Cửu Long', 1621.7, 732.2),
 ('Tỉnh Sóc Trăng', 'Tỉnh', 'Đồng bằng sông Cửu Long', 3311.9, 1199.5),
 ('Tỉnh Bạc Liêu', 'Tỉnh', 'Đồng bằng sông Cửu Long', 2669.0, 908.2),
 ('Tỉnh Cà Mau', 'Tỉnh', 'Đồng bằng sông Cửu Long', 5221.2, 1194.3)
] 


## Khởi tạo DF từ 2 biến và đặt tên cột từ col_list
df = pd.DataFrame(province_list, columns = col_list)

### Hiển thị DF
# print(df)

### Kiểm tra DF
# print(df.dtypes)

### Kiểm tra dung lượng DF, Số hàng, Số cột
# print(df.info())


#### Lưu và đọc file
#df.to_csv('provinces.csv', index=False)


#### Đọc file CSV đã lưu trữ sang DF mới
# province_df = pd.read_csv('./SS10/provinces.csv') ## phạm vi luôn đi từ tên folder
# print(province_df)



### Bài 1: Trích xuất tên các tỉnh và thành pố trong df để in ra màn hình theo định dạng 

#### Bài chữa của Hùng
# b = ""
# for i in range(0, len(df)):
#     b = b + df["Name"][i] + ", "
# print(b)


### Bài 2: Tìm tên các thành phố và vùng tương ứng trong df.
# df_division_region =  df.loc[df['Division'] == 'Thành phố Trung ương', ['Name', 'Region']]
# print(df_division_region)


### Bài 3: - Vùng  Từ df, hãy tìm: 
## Số vùng địa lý ở Việt Nam.
## Số tỉnh thành trong mỗi vùng địa lý.

### Số vùng
# region_count = df['Region'].value_counts()
# print(region_count)

###### Bài 4: Dân Số: Tìm tỉnh/thành phố có dân số đông nhất và 
## tỉnh/ thành phố có dân số ít nhất.
## In ra tên tỉnh/ thành phố và dân số theo đơn vị người.
# max_pop = df['Population'].max()
# min_pop = df['Population'].min()

# print(max_pop)
# print(min_pop)

# max_pop_province = df[df['Population'] == max_pop].iloc[0,:]
# min_pop_province = df[df['Population'] == min_pop].iloc[0,:]
# print(max_pop_province)
# print(min_pop_province)


###### Bài 5: Diện tích vùng
## Tính tổng diện tích trong các vùng địa lý, 
## sau đó tính tỉ lệ diện tích của từng vùng theo công thức:
## Tỉ lệ diện tích một vùng = Diện tích vùng đó/ Tổng diện tích các vùng.

### Vùng và số lượng tỉnh thành trong từng vùng
regions_count = df['Region'].value_counts() 
# print(regions_count)

### Tính tổng diện tích trong mỗi vùng
area_list = []
for region in regions_count.index:
    area_list.append(df[df['Region'] == region]['Area'].sum())

### diện tích của từng vùng
print(area_list)


### Tính tỉ số diện tích
total_area = df['Area'].sum()
area_proportion_list = [area/total_area*100 for area in area_list]

### construct DataFrame
area_df = pd.DataFrame({
    'Region': regions_count.index,
    'Total Area (km2)': area_list,
    'Area Proportion (%)': area_proportion_list
})

print(area_df)