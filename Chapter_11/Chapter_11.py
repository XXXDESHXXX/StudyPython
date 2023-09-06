# ***Algorithmic simulator***
# Task 2
# class Plant:
#     def __init__(self, plant_type):
#         self._plant_type = plant_type
#
#     def message(self):
#         print("Я - планета.")
#
#
# class Tree(Plant):
#     def init(self):
#         Plant.__init__(self, 'дерево')
#
#     def message(self):
#         print("Я - дерево.")
#
#
# def main():
#     p = Plant('саженец')
#     t = Tree('123')
#     p.message()
#     t.message()
#
#
# main()
# ***Programming tasks***
# Task 1
# class Employee:
#     def __init__(self, name, number):
#         self.name = name
#         self.number = number
#
#     def get_name(self):
#         return self.name
#
#     def get_number(self):
#         return self.number
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_number(self, number):
#         self.number = number
#
#
# class ProductionWorker(Employee):
#     def __init__(self, name, number, shift_number, rate):
#         super().__init__(name, number)
#         self.shift_number = shift_number
#         self.rate = rate
#
#     def get_shift_number(self):
#         return self.shift_number
#
#     def get_rate(self):
#         return self.rate
#
#     def set_rate(self, rate):
#         self.rate = rate
#
#     def set_shift_number(self, shift_number):
#         self.shift_number = shift_number
#
#     def __str__(self):
#         return f'name is: {self.name},' \
#                f'number is: {self.number},' \
#                f'shift_number is: {self.shift_number},' \
#                f'rate is: {self.rate}'
#
#
# def main():
#     name = input('Input name: ')
#     number = int(input('Input employee number: '))
#     shift_number = int(input('Input shift number(1-day, 2-night): '))
#     rate = int(input('Input rate: '))
#     worker = ProductionWorker(name, number, shift_number, rate)
#     print(worker)
#
#
# main()
# Task 2
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, name):
#         self.name = name
#
#
# class ShiftSupervisor(Employee):
#     def __init__(self, name, annual_bonus, production_award):
#         super().__init__(name)
#         self.annual_bonus = annual_bonus
#         self.production_award = production_award
#
#     def get_annual_bonus(self):
#         return self.annual_bonus
#
#     def get_production_award(self):
#         return self.production_award
#
#     def set_annual_bonus(self, annual_bonus):
#         self.annual_bonus = annual_bonus
#
#     def set_production_award(self, production_award):
#         self.production_award = production_award
#
#     def __str__(self):
#         return f'name is: {self.name},' \
#                f'annual bonus is: {self.annual_bonus},' \
#                f'production_award is: {self.production_award}'
#
#
# def main():
#     worker = ShiftSupervisor('Kate', 250, 130)
#     print(worker)
#
#
# main()
# Task 3
# class Person:
#     def __init__(self, name, address, telephone):
#         self.name = name
#         self.address = address
#         self.telephone = telephone
#
#     def get_name(self):
#         return self.name
#
#     def get_address(self):
#         return self.address
#
#     def get_telephone(self):
#         return self.telephone
#
#     def set_name(self, name):
#         self.name = name
#
#     def set_address(self, address):
#         self.address = address
#
#     def set_telephone(self, telephone):
#         self.telephone = telephone
#
#
# class Customer(Person):
#     def __init__(self, name, address, telephone, mailing, client_number):
#         super().__init__(name, address, telephone)
#         self.client_number = client_number
#         self.mailing = mailing
#
#     def get_client_number(self):
#         return self.client_number
#
#     def get_mailing(self):
#         return self.mailing
#
#     def set_client_number(self, client_number):
#         self.client_number = client_number
#
#     def set_mailing(self, mailing):
#         self.mailing = mailing
#
#     def __str__(self):
#         return f'name is: {self.name},' \
#                f'address is: {self.address},' \
#                f'telephone is: {self.telephone},' \
#                f'mailing is: {self.mailing},' \
#                f'client_number is: {self.client_number}'
#
#
# def main():
#     mailing = bool(input(
#     'Would you like to get mails from us? 1 - Yes, 2 - No:'
#     ))
#     customer = Customer('Donald', 'USA', 2351234, mailing, 15003)
#     print(customer)
#
#
# main()
