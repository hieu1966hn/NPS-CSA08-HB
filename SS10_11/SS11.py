#### Code buổi 11
import pandas as pd

####### Dữ liệu về thông tin học sinh trong lớp CSA08
data = {
    'Name': ['Hùng', 'Đức Anh', 'Long', 'Khang'],
    'Age': [15, 16, 17, 18],
    'Checkpoint2': [9, 7, 8, 6]
}

df = pd.DataFrame(data)


### Yêu cầu 1: Thay đổi điểm cp2 của bạn "Hùng" thành 10.
## print(df['Name'] == 'Hùng') ### Chỉ ra được vị trí dòng
df.loc[df['Name'] == 'Hùng', 'Checkpoint2'] = 10

## DF sau khi thay đổi


### Yêu cầu 2: Thay đổi tên của bạn "Hùng" thành "Thái Hùng".
df.loc[df['Name'] == 'Hùng', 'Name'] = "Thái Hùng"


### Yêu cầu 3: Thêm một cột với "Checkpoint1" cho từng học sinh
df['Checkpoint1'] = [1, 2, 3, 4]


### Yêu cầu 4: Thêm một dòng dữ liệu mới cho học sinh "Hiếu"
new_student = {
    'Name': "Trung Hiếu",
    'Age': 18,
    'Checkpoint2': 10,
    'Checkpoint1': 10
}
df = df._append(new_student, ignore_index = True)



###### Xóa dữ liệu khỏi DF

### Yêu cầu 5: Xóa dữ liệu cột "Checkpoint2" 
df = df.drop(columns = ['Checkpoint2'])



### Yêu cầu 6: Xóa dữ liệu hàng có học sinh tên "Hieu"
df = df[df['Name'] != "Trung Hiếu"]
### Hiển thị df hiện tại
print(df)