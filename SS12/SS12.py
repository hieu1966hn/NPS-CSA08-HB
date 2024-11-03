import matplotlib.pyplot as plt

# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# plt.plot(x, y, label='Dữ liệu mẫu')
# plt.xlabel('Thời gian')
# plt.ylabel('Giá trị')
# # plt.legend()
# plt.show()

### plt: là tên viết tắt thông dụng của module.



##### Ví dụ nữa liên quan tới hàm show()
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.show()



#### Ví dụ về hàm title()
# x = [1, 2, 3, 4]
# y = [10, 20, 25, 30]

# plt.plot(x, y)
# plt.title('Biểu đồ tăng trưởng')

# plt.show()


### 6. 
# plt.figure(figsize=(10, 5))
# plt.plot([1,2,3], [4,5,6])
# plt.show()

### 8. 
# data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# plt.hist(data, bins=4)
# plt.show()

### 9. 
# sizes = [20, 30, 25, 25]
# labels = ['A', 'B', 'C', 'D']
# plt.pie(sizes, labels=labels)
# plt.show()



#### 10. 
# plt.plot([1, 2, 3], [4, 5, 6])
# plt.savefig('bieudoduongthang.png')



##### Bài tập thực hành áp dụng

### Bài tập thực hành 2
subjects = ["Math", "Science", "History", "Art", "PE"]
students = [15, 20, 10, 5, 25]

## Vẽ biểu đồ cột
# plt.figure(figsize=(10, 5))
# plt.bar(subjects, students, color="green")
# plt.xlabel('Môn học')
# plt.ylabel('Số lượng học sinh')
# plt.title('Số lượng học sinh thích các môn học')
# plt.show()

## Vẽ biểu đồ tròn
plt.figure(figsize=(8,8))
plt.pie(students, labels=subjects, autopct="%1.1f%%", startangle=140)
plt.title('Số lượng học sinh thích các môn học')
plt.show()