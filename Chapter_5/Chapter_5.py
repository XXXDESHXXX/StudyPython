# ***Algorithmic simulator***
# Task 1
# def main():
#     number = int(input('Input number: '))
#     times_ten(number)
#
#
# def times_ten(number):
#     result = number * 10
#     print(result)
#
#
# main()
# Task 2
# def main():
#     show_value(12)
#
#
# def show_value(quantity):
#     print(quantity)
#
#
# main()
# Task 3
# def main():
#     my_function(3, 2, 1)
#
#
# def my_function(a, b, c):
#     print(a, b, c)
#
#
# main()
# Task 4
# def main():
#     x = 1
#     y = 3.4
#     print(x, y)
#     change_us(x, y)
#     print(x, y)
#
#
# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
#
# main()
# Task 5
# def main():
#     my_function(2, 4, 6)
#
#
# def my_function(a, b, c):
#     d = (a + c) / b
#     print(d)
#
#
# main()
# Task 6
# import random
#
#
# def main():
#     generic_function()
#
#
# def generic_function():
#     rand = random.randint(1, 100)
#     print(rand)
#
#
# main()
# Task 7
# def main():
#     number = float(input('Input number: '))
#     result = half(number)
#     print(result)
#
#
# def half(number):
#     return number / 2
#
#
# main()
# Task 8
# def main():
#     result = cube(4)
#     print(result)
#
#
# def cube(num):
#     return num * num * num
#
#
# main()
# Task 9
# def main():
#     number = int(input('Input number: '))
#     print(times_ten(number))
#
#
# def times_ten(x):
#     return x * 10
#
#
# main()
# Task 10
# def main():
#     get_first_name()
#
#
# def get_first_name():
#     name = input('Input your name: ')
#     print(name)
#     return name
#
#
# main()
# ***Programming tasks***
# Task 1
# def main():
#     kilometres = get_kilometres()
#     mill_function(kilometres)
#
#
# def mill_function(kilometres):
#     mills = kilometres * 0.6214
#     print(mills)
#     return mills
#
#
# def get_kilometres():
#     return float(input('Input distance in kilometres: '))
#
#
# main()
# Task 2
# def main():
#     salary = get_purchase()
#     federal_tax = get_federal_tax(salary)
#     regional_tax = get_regional_tax(salary)
#     total_tax = get_total_tax(regional_tax, federal_tax)
#     total_amount = get_total_amount(salary, total_tax)
#     print(salary)
#     print(federal_tax)
#     print(regional_tax)
#     print(total_tax)
#     print(total_amount)
#
#
# def get_purchase():
#     purchase_amount = float(input('Write purchase amount: '))
#     return purchase_amount
#
#
# def get_federal_tax(purchase_amount):
#     federal_taxes = purchase_amount * 0.05
#     return federal_taxes
#
#
# def get_regional_tax(purchase_amount):
#     regional_tax = purchase_amount * 0.025
#     return regional_tax
#
#
# def get_total_tax(regional_tax, federal_taxes):
#     sum_of_taxes = regional_tax + federal_taxes
#     return sum_of_taxes
#
#
# def get_total_amount(salary, total_tax):
#     total_amount = salary + total_tax
#     return total_amount
#
#
# main()
# Task 3
# def main():
#     cost_of_insurance = float(input)