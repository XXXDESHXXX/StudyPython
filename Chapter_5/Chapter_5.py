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
#         )
#     yearly_payment = get_yearly_cost(
#         credit_payment, cost_of_insurance, cost_of_tires, cost_of_gasoline, cost_of_engine_oil, cost_of_maintenance
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
# yearly_cost = (credit_payment + cost_insurance + cost_tires + cost_gasoline + cost_engine_oil + cost_maintenance) *\
#                   12
#    return yearly_cost
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
