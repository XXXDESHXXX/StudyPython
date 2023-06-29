# ***Algorithmic simulator***
# Task 1
# product = 0
# while product < 100:
#     number = int(input('Input number'))
#     product = number * 10
#     print('product = ', product)
# Task 2
# answer = input('Would you like to start? y/n')
# while answer != 'n':
#     first_number = int(input('Write first number: '))
#     second_number = int(input('Write second number: '))
#     sum_of_numbers = first_number + second_number
#     print(sum_of_numbers)
#     answer = input('Would you like to continue? y/n')
# Task 3
# for num in range(0, 1010, 10):
#     print(num)
# Task 4
# amount_of_numbers = 0
# for _ in range(10):
#     amount_of_numbers += int(input('Write your number: '))
#     print('total is', amount_of_numbers)
# Task 5
# sum_of_elements = 0
# denominator = 31
# for i in range(30):
#     sum_of_elements = sum_of_elements + (i+1)/(30-i)
#     print(sum_of_elements)
# Task 6
# x = 0
# x += 1
# x *= 2
# x /= 10
# x -= 100
# Task 7
# for row in range(10):
#     for col in range(15):
#         print('#', end='')
#     print()
# Task 8
# number = int(input('Input number: '))
# while number <= 0:
#     print('Error you input incorrect number')
#     number = int(input('Input number: '))
# Task 9
# number = int(input('Input number: '))
# while number < 1 or number > 100:
#     print('Incorrect number')
#     number = int(input('Input number: '))
# ***Programming tasks***
# Task 1
# dailyCollection = 0
# total_amount_of_errors = 0
# for i in range(5):
#     dailyCollection = int(input('Amount of errors in this day'))
#     while dailyCollection < 0:
#         dailyCollection = int(input('Amount of errors in this day'))
#     total_amount_of_errors += dailyCollection
# print(total_amount_of_errors)
# Task 2
# calories = 0
# for i in range(10, 31, 5):
#     calories = i / 4.2
#     print('Calories = ', calories)
# Task 3
# expenses = 0
# total_expenses = 0
# amount_money = int(input('Input the amount allocated for one month '))
# items_of_expenditure = int(input('Input items of expenditure: '))
# for _ in range(items_of_expenditure):
#     expenses = int(input('Input your expenses: '))
#     total_expenses += expenses
#     while expenses < 0:
#         print('Incorrect number')
#         expenses = int(input('Input your expenses: '))
#         total_expenses += expenses
# total_amount_of_money = amount_money - total_expenses
# print(total_amount_of_money)
# Task 4
# distance = 0
# i = 0
# time = int(input("Input time: "))
# speed = int(input("Input speed: "))
# print("Time\tDistance traveled")
# print("------------------------")
# while i < time:
#     i += 1
#     distance = i * speed
#     print(i, "\t\t", distance)
# Task 5
# monthly_rainfall = 0
# total_millimeters_of_rain = 0
# number_of_months = 0
# number_of_years = int(input("Input number of years: "))
# for _ in range(number_of_years):
#     number_of_months = number_of_years * 12
#     for _ in range(number_of_months):
#         millimeters_of_rain = int(input("Input millimeters of rain in month: "))
#         total_millimeters_of_rain += millimeters_of_rain
#         monthly_rainfall = total_millimeters_of_rain / number_of_months
# print("Number of months is: ", number_of_months)
# print("Millimeters of rain is: ", total_millimeters_of_rain)
# print("Monthly rainfall is: ", monthly_rainfall)
# Task 6
# print('Celsius\tFahrenheit')
# print('------------------')
# for i in range(21):
#     fahrenheit = (9 * i) / 5 + 32
#     print('celsius is: ', i, '\t', 'fahrenheit is: ', fahrenheit)
# Task 7
# kopecks = 0
# salary = 1
# amount_of_days = int(input('Input amount of days: '))
# for _ in range(amount_of_days):
#     salary *= 2
#     kopecks += salary
# salary = kopecks / 100
# print(salary)
# Task 8

