import pandas as pd

## Tạo DF
data = {
    'Name': ['Long', "Hùng", 'Khang', "Đức Anh"],
    "Age": [18, 17, 14, 16],
    "Point": [8.5, 7.0, 10, 9],
}

df = pd.DataFrame(data)


### Truy xuất cột 'Name'
# print(df['Name'])

### Truy xuất tuổi của học sinh đứng thứ 2 trong lớp
# print(df['Age'][1])


######### Mức độ trung bình
### Truy xuất nhiều cột: Truy xuất cột "Name" và "Point" từ DF học sinh.
# print(df[['Name', 'Point']])

### Yêu cầu: Truy xuất tất cả học sinh có điểm số lớn hơn: 8.5
## print(df[df['Point'] > 8.5 ])


########## Nâng cao
### Yêu cầu: Truy xuất học sinh có tên là "Đức Anh" và lấy điểm số của bạn đó (loc[])
## print(df.loc[df['Name'] == 'Đức Anh', "Point"])


### Yêu cầu: Truy xuất tên và tuổi của học sinh thứ 2 trong DF (iloc[])
### print(df.iloc[1,[0, 1]]) # index 2, cột 0 (Name) và cột 1 (Age)



