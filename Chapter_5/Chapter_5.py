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
#     cost_of_insurance = get_cost_of_insurance()
#     total_cost = calculating_insurance(cost_of_insurance)
#     print(total_cost)
#
#
# def get_cost_of_insurance():
#     insurance_cost = float(input('Input cost of insurance: '))
#     return insurance_cost
#
#
# def calculating_insurance(cost_of_insurance):
#     minimal_cost = cost_of_insurance * 0.8
#     return minimal_cost
#
#
# main()
# Task 4
# def main():
#     credit_payment = get_payment_credit()
#     cost_of_insurance = get_insurance_cost()
#     cost_of_tires = get_tires_cost()
#     cost_of_gasoline = get_gasoline_cost()
#     cost_of_engine_oil = get_engine_oil_cost()
#     cost_of_maintenance = get_maintenance_cost()
#     monthly_payment = get_monthly_cost(
#         credit_payment, cost_of_insurance, cost_of_tires, cost_of_gasoline, cost_of_engine_oil, cost_of_maintenance
#     )
#     yearly_payment = get_yearly_cost(
#         credit_payment,
#         cost_of_insurance,
#         cost_of_tires,
#         cost_of_gasoline,
#         cost_of_engine_oil,
#         cost_of_maintenance,
#     )
#     print(monthly_payment)
#     print(yearly_payment)
#
#
# def get_payment_credit():
#     payment = float(input('Input payment credit: '))
#     return payment
#
#
# def get_insurance_cost():
#     insurance_cost = float(input('Input cost of insurance: '))
#     return insurance_cost
#
#
# def get_gasoline_cost():
#     gasoline_cost = float(input('Input cost of gasoline: '))
#     return gasoline_cost
#
#
# def get_engine_oil_cost():
#     engine_oil_cost = float(input('Input cost of engine oil: '))
#     return engine_oil_cost
#
#
# def get_tires_cost():
#     tires_cost = float(input('Input cost of tires: '))
#     return tires_cost
#
#
# def get_maintenance_cost():
#     maintenance_cost = float(input('Input maintenance cost: '))
#     return maintenance_cost
#
#
# def get_monthly_cost(credit_payment, cost_insurance, cost_tires, cost_gasoline, cost_engine_oil, cost_maintenance):
#     monthly_cost = credit_payment + cost_insurance + cost_tires + cost_gasoline + cost_engine_oil + cost_maintenance
#     return monthly_cost
#
#
# def get_yearly_cost(credit_payment, cost_insurance, cost_tires, cost_gasoline, cost_engine_oil, cost_maintenance):
#     yearly_cost = (
#                     credit_payment + cost_insurance + cost_tires + cost_gasoline + cost_engine_oil + cost_maintenance
#                   ) * 12
#     return yearly_cost
#
#
# main()
# Task 5
# def main():
#     estimated_cost = get_estimated_cost()
#     actual_cost = get_actual_value(estimated_cost)
#     property_tax = get_property_tax(actual_cost)
#     print(estimated_cost, property_tax)
#
#
# def get_estimated_cost():
#     estimated_value = float(input('Input estimated value: '))
#     return estimated_value
#
#
# def get_actual_value(estimated_cost):
#     actual_value = estimated_cost * 0.6
#     return actual_value
#
#
# def get_property_tax(actual_value):
#     tax_per_acr = (actual_value / 100) * 0.72
#     return tax_per_acr
#
#
# main()
# Task 6
# def main():
#     fats_grams = get_number_fats_grams()
#     carbohydrates_grams = get_number_carbohydrates_grams()
#     total_fats_calories = get_calories_from_fat(fats_grams)
#     total_carbohydrates_calories = get_calories_from_carbohydrates(carbohydrates_grams)
#     print(total_fats_calories, total_carbohydrates_calories)
#
#
# def get_number_fats_grams():
#     number_of_fats_grams = float(input('Input number of fats grams: '))
#     return number_of_fats_grams
#
#
# def get_number_carbohydrates_grams():
#     number_of_carbohydrates_grams = float(input('Input number of carbohydrates grams: '))
#     return number_of_carbohydrates_grams
#
#
# def get_calories_from_fat(fats_grams):
#     fat_calories = fats_grams * 9
#     return fat_calories
#
#
# def get_calories_from_carbohydrates(carbohydrates_grams):
#     carbohydrates_calories = carbohydrates_grams * 4
#     return carbohydrates_calories
#
#
# main()
# Task 7
# def main():
#     number_of_a_seats = get_number_of_a_seats()
#     number_of_b_seats = get_number_of_b_seats()
#     number_of_c_seats = get_number_of_c_seats()
#     total_income = get_income(number_of_a_seats, number_of_b_seats, number_of_c_seats)
#     print(total_income)
#
#
# def get_number_of_a_seats():
#     a_seats = int(input('Input number of A seats: '))
#     return a_seats
#
#
# def get_number_of_b_seats():
#     b_seats = int(input('Input number of B seats: '))
#     return b_seats
#
#
# def get_number_of_c_seats():
#     c_seats = int(input('Input number of C seats: '))
#     return c_seats
#
#
# def get_income(a_seats, b_seats, c_seats):
#     income = a_seats * 20 + b_seats * 15 + c_seats * 10
#     return income
#
#
# main()
# Task 8
# def main():
#     surface_area = get_area()
#     paint_price = get_cost_paint_container()
#     paint_cost = cost_of_paint(surface_area, paint_price)
#     work_hours = hours_of_work(surface_area)
#     work_cost = cost_of_work(work_hours)
#     total_cost = get_total_cost(work_cost, paint_cost)
#     print(total_cost)
#
#
# def get_area():
#     area = int(input('Input area: '))
#     return area
#
#
# def get_cost_paint_container():
#     paint_cost = int(input('Input cost of paint container: '))
#     return paint_cost
#
#
# def cost_of_paint(surface_area, paint_cost):
#     paint_area = surface_area / 10
#     total_paint_cost = paint_cost * paint_area
#     return total_paint_cost
#
#
# def hours_of_work(surface_area):
#     work_hours = surface_area / 10 * 8
#     return work_hours
#
#
# def cost_of_work(work_hours):
#     work_cost = work_hours * 2000
#     return work_cost
#
#
# def get_total_cost(work_cost, price_of_paint):
#     total_cost = work_cost + price_of_paint
#     return total_cost
#
#
# main()
# Task 9
# def main():
#     sales_tax = get_sales_tax()
#     municipal_tax = get_municipal_tax(sales_tax)
#     federal_tax = get_federal_tax(sales_tax)
#     total_sales = get_total_sales(municipal_tax, federal_tax)
#     print(total_sales)
#
#
# def get_sales_tax():
#     sales_tax = float(input('Input sales_tax: '))
#     return sales_tax
#
#
# def get_municipal_tax(sales_tax):
#     municipal_tax = sales_tax * 0.025
#     return municipal_tax
#
#
# def get_federal_tax(sales_tax):
#     federal_tax = sales_tax * 0.05
#     return federal_tax
#
#
# def get_total_sales(municipal_tax, federal_tax):
#     total_sales = municipal_tax + federal_tax
#     return total_sales
#
#
# main()
# Task 10
# def main():
#     feets = get_feet()
#     inches = get_inches(feets)
#     print(inches)
#
#
# def get_feet():
#     feets = int(input('Input number of feets: '))
#     return feets
#
#
# def get_inches(feets):
#     inches = feets * 12
#     return inches
#
#
# main()
# Task 11 and 12
# def main():
#     first_number = get_first_number()
#     second_number = get_second_number()
#     sum_of_numbers = get_sum(first_number, second_number)
#     answer = get_answer(sum_of_numbers)
#     print(sum_of_numbers, answer)
#
#
# def get_first_number():
#     first_number = int(input('Input first number: '))
#     return first_number
#
#
# def get_second_number():
#     second_number = int(input('Input second number: '))
#     return second_number
#
#
# def get_sum(first_number, second_number):
#     return first_number + second_number
#
#
# def get_answer(sum_of_numbers):
#     answer = int(input('Input your answer: '))
#     return answer == sum_of_numbers
#
#
# main()
# Task 13
# def main():
#     first = int(input('Input first number: '))
#     second = int(input('Input second number: '))
#     maximum = max(first, second)
#     print(maximum)
#
#
# def max(first, second):
#     if first > second:
#         return first
#     else:
#         return second
#
#
# main()
# Task 14
# G = 9.8
#
#
# def main():
#     for i in range(1, 11):
#         falling_distance(i)
#         print(falling_distance(i))
#
#
# def falling_distance(time):
#     return (G*time**2)/2
#
#
# main()
# Task 15
# def main():
#     mass = get_mass()
#     speed = get_speed()
#     kinetic = kinetic_energy(mass, speed)
#     print(kinetic)
#
#
# def get_mass():
#     mass = int(input('Input mass: '))
#     return mass
#
#
# def get_speed():
#     speed = int(input('Input speed: '))
#     return speed
#
#
# def kinetic_energy(mass, speed):
#     kinetic = (mass * speed**2) / 2
#     return kinetic
#
#
# main()
# Task 16
# def main():
#     first_mark = get_first_mark()
#     second_mark = get_second_mark()
#     third_mark = get_third_mark()
#     fourth_mark = get_fourth_mark()
#     fifth_mark = get_fifth_mark()
#     average_value = calc_average(first_mark, second_mark, third_mark, fourth_mark, fifth_mark)
#     grade = determine_grade(average_value)
#     print(grade)
#
#
# def get_first_mark():
#     first_mark = int(input('Input first mark: '))
#     return first_mark
#
#
# def get_second_mark():
#     second_mark = int(input('Input second mark: '))
#     return second_mark
#
#
# def get_third_mark():
#     third_mark = int(input('Input third mark: '))
#     return third_mark
#
#
# def get_fourth_mark():
#     fourth_mark = int(input('Input fourth mark: '))
#     return fourth_mark
#
#
# def get_fifth_mark():
#     fifth_mark = int(input('Input fifth mark: '))
#     return fifth_mark
#
#
# def calc_average(first_mark, second_mark, third_mark, fourth_mark, fifth_mark):
#     average = (first_mark + second_mark + third_mark + fourth_mark + fifth_mark) / 5
#     return average
#
#
# def determine_grade(average_value):
#     if average_value >= 90:
#         return 'A'
#     elif 80 <= average_value <= 89:
#         return 'B'
#     elif 70 <= average_value <= 79:
#         return 'C'
#     elif 60 <= average_value <= 69:
#         return 'D'
#     else:
#         return 'F'
#
#
# main()
# Task 17
# import random
#
#
# def main():
#     count_even = 0
#     count_odd = 0
#     for count in range(100):
#         number = random.randint(1, 100)
#         if number % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     print(count_even)
#     print(count_odd)
#
#
# main()
# Task 18
# def main():
#     simple_number = int(input('Input number: '))
#     number = is_prime(simple_number)
#     print(number)
#
#
# def is_prime(simple_number):
#     k = 0
#     for i in range(2, simple_number):
#         if simple_number % i == 0:
#             k = k + 1
#     if k <= 0:
#         return 'Simple'
#     else:
#         return 'Not simple'
#
#
# main()
# Task 19


# def main():
#     for number in range(1, 100):
#         if is_prime(number):
#             print(number)
#
#
# def is_prime(number):
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#         return True
#
#
# main()
# Task 20
# def main():
#     current_amount = get_current_amount()
#     interest_rate = get_interest_rate()
#     number_of_months = get_number_of_months()
#     future_amount = get_future_amount(current_amount, number_of_months, interest_rate)
#     print(future_amount)
#
#
# def get_current_amount():
#     current_amount = int(input('Input current amount: '))
#     return current_amount
#
#
# def get_interest_rate():
#     interest_rate = int(input('Input interest rate: '))
#     return interest_rate
#
#
# def get_number_of_months():
#     number_of_months = int(input('Input number of months: '))
#     return number_of_months
#
#
# def get_future_amount(current_amount, number_of_months, interest_rate):
#     future_amount = current_amount * (number_of_months + 1)**interest_rate
#     return future_amount
#
#
# main()
# Task 21
# import random
#
#
# def game():
#     print('Hello, now you play game, where you need to guess number! ')
#     number = random.randint(1, 100)
#     answer = int(input('Input number'))
#     while True:
#         if answer > number:
#             print('Too big number')
#             answer = int(input('Input number'))
#         elif answer < number:
#             print('Too small number')
#             answer = int(input('Input number'))
#         elif answer == number:
#             continue_answer = input('Would you like to continue? ')
#             if continue_answer == 'Yes':
#                 number = random.randint(1, 100)
#                 answer = int(input('Input number'))
#             else:
#                 break
#     print('You are win!')
#     print(answer)
#     return answer
#
#
# game()
# Task 22
# import random
#
#
# def game():
#     while True:
#         computer_variant = random.randint(1, 3)
#         computer_item = None
#         if computer_variant == 1:
#             computer_item = 'rock'
#         elif computer_variant == 2:
#             computer_item = 'scissors'
#         elif computer_variant == 3:
#             computer_item = 'paper'
#         else:
#             print('Fool')
#         human_item = input('Input your item (rock, paper, scissors)')
#         print(computer_item)
#         if computer_item == 'rock' and human_item == 'scissors':
#             print('Rock win!')
#         elif human_item == 'rock' and computer_item == 'scissors':
#             print('Rock win!')
#         elif computer_item == 'scissors' and human_item == 'paper':
#             print('Scissors win!')
#         elif human_item == 'scissors' and computer_item == 'paper':
#             print('Scissors win!')
#         elif computer_item == 'paper' and human_item == 'rock':
#             print('Paper win!')
#         elif human_item == 'paper' and computer_item == 'rock':
#             print('Paper win!')
#         elif computer_item == human_item:
#             print('We need to try again )')
#             computer_variant = random.randint(1, 3)
#         else:
#             break
#
#
# game()
