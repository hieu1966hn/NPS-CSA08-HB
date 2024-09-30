class Person: 
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}"
    
class Employee(Person):
    def __init__(self, name, age, address, job_title, salary):
        super().__init__(name, age, address)
        self.job_title = job_title
        self.salary = salary
    
    def display(self):
        return f"{super().display()}, Job Title: {self.job_title}, Salary: {self.salary}"
    
class Manager(Employee):
    def __init__(self, name, age, address, job_title, salary, department):
        super().__init__(name, age, address, job_title, salary)
        self.department = department
    
    def display(self):
        return f"{super().display()}, Department: {self.department}"
    
class Company:
    def __init__(self):
        self.employees = []
    
    ### them mot nhan su vao danh sach quan ly
    def add_employee(self, employee):
        self.employees.append(employee)

    ### Xóa một nhân sự khi biết tên nhân sự đó.
    def remove_employee(self, name):
        ### Tạo một danh sách mới để lưu trữ các nhân viên còn lại sau khi loại bỏ ? nhân sự
        updated_employees = []
        ### Duyệt qua từng nhân viên trong danh sách hiện tại
        for emp in self.employees:
            ### Nếu tên của nhân viên không khớp với tên cần xóa
            if emp.name != name:
                ## Thêm nhân viên đó vào danh sách mới
                updated_employees.append(emp)
        
        ### Cập nhật danh sách nhân viên của công ty
        self.employees = updated_employees

    ### Tìm kiếm nhân sự khi biết tên nhân sự đó
    def find_employee(self, name):
        ### Duyệt danh sách nhân sự trong công ty
        for emp in self.employees:
            if emp.name == name:
                return emp.display()
        return "Employee not found"

    ### Hiển thị toàn bộ thông tin nhân sự có trong công ty ??

mindx = Company()
Hung = Employee("Nguyễn Thái Hùng", 99, "107 Nguyễn Phong Sắc", "Developer", 1000)
Hieu = Manager("Nguyễn Trung Hiếu", 99, "107 Nguyễn Phong Sắc", "Manager", 3000, "MindX School")


mindx.add_employee(Hung)
mindx.add_employee(Hieu)

### Hiển thị thông tin toàn bộ nhân sự trong công ty

### Tìm kiếm theo tên
print(mindx.find_employee("Nguyễn Trung Hiếu"))

### Xóa 1 nhân sự
mindx.remove_employee("Nguyễn Thái Hùng")

### Hiển thị thông tin toàn bộ nhân sự trong công ty sau khi đã xóa 1 nhân viên.


    



