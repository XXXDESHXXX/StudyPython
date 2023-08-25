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
# import pickle
# import employee as emp
#
#
# LOOK_UP = 1
# ADD = 2
# CHANGE = 3
# DELETE = 4
# PRINT = 5
# QUIT = 6
#
#
# def main():
#     employee = load_employees()
#     choice = 0
#     while choice != QUIT:
#         choice = get_menu_choice()
#         if choice == LOOK_UP:
#             look_up(employee)
#         elif choice == ADD:
#             add(employee)
#         elif choice == CHANGE:
#             change(employee)
#         elif choice == DELETE:
#             delete(employee)
#         elif choice == PRINT:
#             print(employee)
#     save_employees(employee)
#
#
# def load_employees():
#     try:
#         with open('employees.dat', 'rb') as file:
#             employees = pickle.load(file)
#             file.close()
#     except EOFError:
#         employees = {}
#     return employees
#
#
# def get_menu_choice():
#     print()
#     print('Menu')
#     print('1. Find')
#     print('2. Add')
#     print('3. Change')
#     print('4. Delete')
#     print('5. Print')
#     print('6. Quit')
#     choice = int(input('Input your choice: '))
#     while choice < LOOK_UP or choice > QUIT:
#         choice = int(input('Input your choice: '))
#     return choice
#
#
# def look_up(employee):
#     identifier = input('Input identifier: ')
#     print(employee.get(identifier, 'Not found'))
#
#
# def add(employee):
#     name = input('Name: ')
#     identifier = input('Identifier: ')
#     department = input('Department: ')
#     post = input('Post: ')
#     entry = emp.Employee(name, identifier, department, post)
#     if identifier not in employee:
#         employee[identifier] = entry
#         print('In dictionary')
#     else:
#         print('Not found')
#
#
# def change(employee):
#     identifier = input('Identifier: ')
#     if identifier in employee:
#         name = input('Input new telephone number: ')
#         department = input('Input new department: ')
#         post = input('Input new post: ')
#         entry = emp.Employee(name, identifier, department, post)
#         employee[identifier] = entry
#         print('Update')
#     else:
#         print('Not found')
#
#
# def delete(employee):
#     identifier = input('Input identifier: ')
#     if identifier in employee:
#         del employee[identifier]
#         print('Deleted')
#     else:
#         print('Not found')
#
#
# def save_employees(employee):
#     with open('employees.dat', 'wb') as file:
#         pickle.dump(employee, file)
#         file.close()
#
#
# main()
# Task 8
# class RetailItem:
#     def __init__(self, description, amount, cost):
#         self.__description = description
#         self.__amount = amount
#         self.__cost = cost
#
#     def get_description(self):
#         return self.__description
#
#     def get_amount(self):
#         return self.__amount
#
#     def get_cost(self):
#         return self.__cost
#
#     def set_description(self, description):
#         self.__description = description
#
#     def set_amount(self, amount):
#         self.__amount = amount
#
#     def set_cost(self, cost):
#         self.__cost = cost
#
#     def __str__(self):
#         return f'{self.__description}, {self.__amount}, {self.__cost}'
#
#
# class CashRegister:
#
#     def __init__(self):
#         self.__cart = [
#             RetailItem(description='test', amount='test', cost=123),
#             RetailItem(description='test_2', amount='test_2', cost=455),
#         ]
#
#     def purchase_item(self, retail_item):
#         self.__cart.append(retail_item)
#
#     def get_total(self):
#         total_cost = 0
#         for retail_item in self.__cart:
#             total_cost += retail_item.get_cost()
#         return total_cost
#
#     def show_items(self):
#         show_items = []
#         for retail_item in self.__cart:
#             show_items.append(str(retail_item))
#         return show_items
#
#     def clear(self):
#         self.__cart.clear()
#
#
# def main():
#     cart = CashRegister()
#     choice = 'No'
#     while choice.upper() != 'YES':
#         retail_item = RetailItem(
#             description=input('Input descr'),
#             amount=input('Input amount'),
#             cost=int(input('Input cost')),
#         )
#         cart.purchase_item(retail_item)
#         choice = input('Are you ready to buy all this items?')
#     print(cart.show_items())
#     print(cart.get_total())
#     cart.clear()
#
#
# main()
# Task 9
# class Question:
#     def __init__(self,
#                  question,
#                  first_answer,
#                  second_answer,
#                  third_answer,
#                  fourth_answer,
#                  correct_answer,
#                  ):
#         self.__question = question
#         self.__first_answer = first_answer
#         self.__second_answer = second_answer
#         self.__third_answer = third_answer
#         self.__fourth_answer = fourth_answer
#         self.__correct_answer = correct_answer
#
#     def get_question(self):
#         return self.__question
#
#     def get_first_answer(self):
#         return self.__first_answer
#
#     def get_second_answer(self):
#         return self.__second_answer
#
#     def get_third_answer(self):
#         return self.__third_answer
#
#     def get_fourth_answer(self):
#         return self.__fourth_answer
#
#     def get_correct_answer(self):
#         return self.__correct_answer
#
#     def set_question(self, question):
#         self.__question = question
#
#     def set_first_answer(self, first_answer):
#         self.__first_answer = first_answer
#
#     def set_second_answer(self, second_answer):
#         self.__second_answer = second_answer
#
#     def set_third_answer(self, third_answer):
#         self.__third_answer = third_answer
#
#     def set_fourth_answer(self, fourth_answer):
#         self.__fourth_answer = fourth_answer
#
#     def set_correct_answer(self, correct_answer):
#         self.__correct_answer = correct_answer
#
#
# class Quiz:
#     def __init__(self, questions, amount_of_players):
#         self.__questions = questions
#         self.__amount_of_players = amount_of_players
#         self.__winner_score = [0 for _ in range(amount_of_players)]
#         self.__question_index = 0
#
#     def get_question_index(self):
#         return self.__question_index
#
#     def set_question_index(self, question_index):
#         self.__question_index = question_index
#
#     def get_questions(self):
#         return self.__questions
#
#     def get_amount_of_players(self):
#         return self.__amount_of_players
#
#     def set_questions(self, questions):
#         self.__questions = questions
#
#     def set_amount_of_players(self, amount_of_players):
#         self.__amount_of_players = amount_of_players
#
#     def start_game(self):
#         while self.__question_index < len(self.__questions):
#             self.game_round()
#         print('WINNER IS PLAYER!')
#         print('--------------------------------------')
#         print(self.__winner_score.index(max(self.__winner_score)))
#
#     def game_round(self):
#         for turn in range(self.__amount_of_players):
#             for i in range(5):
#                 question = self.__questions[i]
#                 print(question.get_question())
#                 print("It's ", turn, "player turn")
#                 print('You got next variant of answers: ')
#                 print(question.get_first_answer(), '0')
#                 print(question.get_second_answer(), '1')
#                 print(question.get_third_answer(), '2')
#                 print(question.get_fourth_answer(), '3')
#                 answer = int(input('Input number of your answer'))
#                 if answer == question.get_correct_answer():
#                     self.__winner_score[turn] += 1
#         self.__question_index += 5
#
#
# def main():
#     quiz = Quiz(
#         [
#             Question("Какое животное издает му", "Корова", "Кошка", "Собака", "Муха", 0),
#             Question("Сколько планет в солнечной системе", "7", "9", "8", "10", 2),
#             Question("Как называется столица Франции?", "Мадрид", "Париж", "Рим", "Берлин", 1),
#             Question("Какой химический элемент имеет символ 'O'?", "Кислород", "Водород", "Азот", "Углерод",
#                      0),
#             Question("Какой газ является основной составляющей воздуха?", "Кислород", "Водород", "Азот", "Углерод",
#                      2),
#             Question("Какой цвет получается смешением синего и красного?", "Зеленый", "Фиолетовый", "Оранжевый",
#                      "Желтый", 1),
#             Question("Как называется самая большая планета в солнечной системе?", "Марс", "Венера", "Юпитер", "Сатурн",
#                      2),
#             Question("Какой город является столицей Японии?", "Киото", "Осака", "Токио", "Хоккайдо", 2),
#             Question("Сколько континентов на Земле?", "4", "5", "6", "7", 3),
#             Question("Какой город называют 'Вечным городом'?", "Париж", "Рим", "Лондон", "Мадрид", 1),
#         ],
#         2,
#     )
#     quiz.start_game()
#
#
# main()
