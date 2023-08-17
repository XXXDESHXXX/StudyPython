# ***Algorithmic simulator***
# Task 1
# class Car:
#     def __init__(self):
#         self.way = 30
#
#     def go(self):
#         return self.way + 1
#
#
# def main():
#     my_car = Car()
#     my_car.go()
#     print(my_car.go())
#
#
# main()
# Task 2
# class Book:
#     def __init__(self, name, author, publisher):
#         self.name = name
#         self.author = author
#         self.publisher = publisher
#
#     def set_book_name(self, name):
#         self.name = name
#
#     def set_book_author(self, author):
#         self.author = author
#
#     def set_book_publisher(self, publisher):
#         self.publisher = publisher
#
#     def get_book_name(self):
#         return self.name
#
#     def get_book_author(self):
#         return self.author
#
#     def get_book_publisher(self):
#         return self.publisher
#
#
# def main():
#     name = input('Enter book name: ')
#     author = input('Enter book author: ')
#     publisher = input('Enter book publisher: ')
#     book = Book(name, author, publisher)
#     print(book.get_book_name())
#     print(book.get_book_author())
#     print(book.get_book_publisher())
#
#
# main()
# ***Programming tasks***
# Task 1
# class Pet:
#     def __init__(self, name, animal_type, age):
#         self.__name = name
#         self.__animal_type = animal_type
#         self.__age = age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_animal_type(self, animal_type):
#         self.__animal_type = animal_type
#
#     def set_age(self, age):
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_animal_type(self):
#         return self.__animal_type
#
#     def get_age(self):
#         return self.__age
#
#
# def main():
#     age = int(input('Enter age: '))
#     animal_type = input('Enter animal type: ')
#     name = input('Enter a name: ')
#     pet = Pet(name, animal_type, age)
#     print(pet.get_name())
#     print(pet.get_age())
#     print(pet.get_animal_type())
#
#
# main()
# Task 2
# class Car:
#     def __init__(self, year_model, make):
#         self.__year_model = year_model
#         self.__make = make
#         self.__speed = 0
#
#     def accelerate(self):
#         self.__speed += 5
#
#     def stop(self):
#         self.__speed -= 5
#
#     def get_speed(self):
#         return self.__speed
#
#
# def main():
#     make = input('Enter company name: ')
#     year_model = int(input('Enter year model: '))
#     car = Car(year_model, make)
#     for i in range(0, 5):
#         car.accelerate()
#         print(car.get_speed())
#     for i in range(0, 5):
#         car.stop()
#         print(car.get_speed())
#
#
# main()
# Task 3
# class Information:
#     def __init__(self, name, address, telephone_number):
#         self.__name = name
#         self.__address = address
#         self.__telephone_number = telephone_number
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_address(self, address):
#         self.__address = address
#
#     def set_telephone_number(self, telephone_number):
#         self.__telephone_number = telephone_number
#
#     def get_name(self):
#         return self.__name
#
#     def get_address(self):
#         return self.__address
#
#     def get_telephone_number(self):
#         return self.__telephone_number
#
#     def __str__(self):
#         return f'{self.__name}, {self.__address}, {self.__telephone_number}'
#
#
# def main():
#     my_info = Information('Kirill', 'Belarus', 3564241)
#     friend_info = Information('Nikita', 'Belarus', 35642424)
#     family_info = Information('Tatyana', 'Belarus', 362621123)
#     print(my_info)
#     print(friend_info)
#     print(family_info)
#
#
# main()
# Task 4
