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
# class Employee:
#     def __init__(self, name, identifier, department, post):
#         self.__name = name
#         self.__identifier = identifier
#         self.__department = department
#         self.__post = post
#
#     def __str__(self):
#         return f'{self.__name}, {self.__post}, {self.__department}, {self.__identifier}'
#
#
# def main():
#     first_employee = Employee('Suzan', 47899, 'Accounting', 'Vice President')
#     second_employee = Employee('Mark', 39119, 'IT', 'Programming')
#     third_employee = Employee('Joe', 81774, 'Production', 'Engineer')
#     print(first_employee)
#     print(second_employee)
#     print(third_employee)
#
#
# main()
# Task 5
# class RetailItem:
#     def __init__(self, description, amount, cost):
#         self.__description = description
#         self.__amount = amount
#         self.__cost = cost
#
#     def __str__(self):
#         return f'{self.__description}, {self.__amount}, {self.__cost}'
#
#
# def main():
#     first_product = RetailItem('jacket', 12, 59.95)
#     second_product = RetailItem('jeans', 40, 34.95)
#     third_product = RetailItem('shirt', 20, 24.95)
#     print(first_product)
#     print(second_product)
#     print(third_product)
#
#
# main()
# Task 6
# class Patient:
#     def __init__(self, first_name, last_name, address, phone, telephone_number):
#         self.__first_name = first_name
#         self.__last_name = last_name
#         self.__full_name = f'{self.__first_name} {self.__last_name}'
#         self.__address = address
#         self.__phone = phone
#         self.__telephone_number = telephone_number
#
#     def get_first_name(self):
#         return self.__first_name
#
#     def get_last_name(self):
#         return self.__last_name
#
#     def get_full_name(self):
#         return f'{self.__first_name} {self.__last_name}'
#
#     def get_address(self):
#         return self.__address
#
#     def get_phone(self):
#         return self.__phone
#
#     def get_telephone_number(self):
#         return self.__telephone_number
#
#     def set_first_name(self, first_name):
#         self.__first_name = first_name
#
#     def set_last_name(self, last_name):
#         self.__last_name = last_name
#
#     def set_full_name(self):
#         self.__full_name = f'{self.__first_name} {self.__last_name}'
#
#     def set_address(self, address):
#         self.__address = address
#
#     def set_phone(self, phone):
#         self.__phone = phone
#
#     def set_telephone_number(self, telephone_number):
#         self.__telephone_number = telephone_number
#
#     def __str__(self):
#         return f'{self.__full_name}, {self.__telephone_number}, {self.__phone}, {self.__address}'
#
#
# class Procedure:
#     def __init__(self, name, date, doctor_name, cost):
#         self.__name = name
#         self.__date = date
#         self.__doctor_name = doctor_name
#         self.__cost = cost
#
#     def get_name(self):
#         return self.__name
#
#     def get_date(self):
#         return self.__date
#
#     def get_doctor_name(self):
#         return self.__doctor_name
#
#     def get_cost(self):
#         return self.__cost
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_date(self, date):
#         self.__date = date
#
#     def set_doctor_name(self, doctor_name):
#         self.__doctor_name = doctor_name
#
#     def set_cost(self, cost):
#         self.__cost = cost
#
#     def __str__(self):
#         return f'{self.__name}, {self.__date}, {self.__cost}, {self.__doctor_name}'
#
#
# def main():
#     patient = Patient('Nikolai', 'Ivanov', 'Minsk', '23125', '3751231231')
#     first_procedure = Procedure('examination', '22.04.2023', 'I.A.Akimovich', 750)
#     second_procedure = Procedure('X-ray', '31.05.2023', 'A.B.Dmitrovich', 1050)
#     third_procedure = Procedure('Blood test', '21.09.2023', 'I.K.Adamovich', 2600)
#     print(patient, '\n')
#     print(first_procedure, '\n')
#     print(second_procedure, '\n')
#     print(third_procedure, '\n')
#     cost = first_procedure.get_cost() + second_procedure.get_cost() + third_procedure.get_cost()
#     print(cost)
#
#
# main()
# Task 7
# class Employee:
#     def __init__(self, name, identifier, department, post):
#         self.__name = name
#         self.__identifier = identifier
#         self.__department = department
#         self.__post = post
#
#     def __str__(self):
#         return f'{self.__name}, {self.__post}, {self.__department}, {self.__identifier}'
#
#
# def main():
#     first_employee = Employee('Suzan', 47899, 'Accounting', 'Vice President')
#     second_employee = Employee('Mark', 39119, 'IT', 'Programming')
#     third_employee = Employee('Joe', 81774, 'Production', 'Engineer')
#     print(first_employee)
#     print(second_employee)
#     print(third_employee)
#
#
# main()
