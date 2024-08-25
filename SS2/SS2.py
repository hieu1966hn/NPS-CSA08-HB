# ## Tạo class point
# class Point:
#     def __init__(self, x, y):  ## Hàm khởi tạo thuộc tính.
#         self.x = x
#         self.y = y

#     ## Viết phương thức
#     def add(self, point):
#         ### Cộng điểm hiện tại với một điểm khác
#         return Point(self.x + point.x, self.y + point.y)

#     ### Trừ điểm hiện tại với một điểm khác.
#     def sub(self, point):
#         ### trừ điểm hiện tại với một điểm khác
#         return Point(self.x - point.x, self.y - point.y)

#     ## Hiển thị tọa độ của điểm
#     def __str__(self): ## Phương thức này giúp định dạng đầu ra khi in một đối tượng Point.
#         ## Khi gọi print(point1), phương thức này sẽ được tự động gọi để hiển thị theo định dạng (x,y)
#         return f"({self.x}, {self.y})"

# ## Ví dụ sử dụng
# point1 = Point(2,3)
# point2 = Point(4,5)

# ## Cộng 2 điểm trên
# print("Cộng hai điểm point1 và point2", point1.add(point2))

# ## Trừ 2 điểm trên
# print("Trừ hai điểm point1 và point2", point1.sub(point2))


### Thực hành với Kế thừa
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def make_sound(self):
#         return f"{self.name} makes a sound. "


# class Dog(Animal):
#     def __init__(self, name, species, breed):
#         ## Gọi hàm khởi tạo của lớp cha
#         super().__init__(name, "Dog")
#         self.breed = breed

#     def make_sound(self):
#         return super().make_sound() + f"{self.name} barks"
    
# # class Cat(Animal):



# ### Sử dụng các lớp
# dog = Dog("Buddy", "Golden Retriever", "nô")

# print(dog.make_sound())


### Thực hành với kế thừa nhiều lớp
class Bird:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating."
    
class Flyer: 
    def __init__(self, wing_span):
        self.wing_span = wing_span
    
    def fly(self):
        return f"Flying with a wingspan of {self.wing_span} meters."

class FlyingBird(Bird, Flyer):
    def __init__(self, name, wing_span):
        ## Gọi hàm khởi tạo của cả 2 lớp cha
        Bird.__init__(self, name)
        Flyer.__init__(self, wing_span)
    
    def show_info(self):
        return f"{self.name} can fly with a wingspan of {self.wing_span} meters."


## Sử dụng lớp FlyingBird  
eagle = FlyingBird("Eagle", 2.5)

print(eagle.eat())
print(eagle.fly())
print(eagle.show_info())