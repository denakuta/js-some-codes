import time as t

# class Cat:
#     name = None
#     age = None
#     isHappy = None
#
#     def __init__(self, name, age, isHappy):
#         self.set_data(name, age, isHappy)
#         self.get_data()
#
#
#     def set_data(self, name = None, age = None, isHappy = None):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
#
#     def get_data(self):
#         print(self.name, 'age:', self.age, '. Happy:', self.isHappy)
#
#


# cat1 = Cat('Murzik', 5, True)
# # cat1.set_data("Murzik", 5, True)
#
# cat2 = Cat('Barsik', 7, False)
# # cat2.set_data("Barsik", 7, False)
#
# # cat1.get_data()
# # cat2.get_data()


class Book:
    def  __init__(self, title, author, age):
        self.title = title
        self.author = author
        self.age = age

    def info(self):
        print(f"{self.title} - {self.author} - {self.age}")

class EBook(Book):
    def  __init__(self, title, author, age, file_size):
        super().__init__(title, author, age)
        self.file_size = file_size



books = [
    EBook('Война и мир', 'Толстой', 1867, 5.6),
    EBook('Преступление и наказание', 'Достоевский', 1866, 4.2),
    EBook('Анна Каренина', 'Толстой', 1877, 3.8),
    EBook('Мастер и Маргарита', 'Булгаков', 1967, 6.1),
    EBook('Евгений Онегин', 'Пушкин', 1833, 2.5)
]

for i in books:
    i.info()
    t.sleep(0.5)