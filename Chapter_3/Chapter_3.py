# ***Algorithmic simulator***
# Task 1
# x = int(input('x = '))
# if x > 100:
#     y = 20
#     z = 40
#     print(z)
#     print(y)
# Task 2
# a = int(input('a = '))
# if a < 10:
#     b = 0
#     c = 1
#     print(c)
#     print(b)
# Task 3
# a = int(input('a = '))
# if a < 10:
#     b = 0
#     print(b)
# else:
#     b = 99
#     print(b)
# Task 4
# score = int(input('Write your score: '))
# A_score = 80
# B_score = 70
# C_score = 50
# D_score = 40
# if score >= A_score:
#     print('Your level - А.')
# else:
#     if score >= B_score:
#         print('Your level - В. ')
#     else:
#         if score >= C_score:
#             print('Your level - С. ')
#         else:
#             if score >= D_score:
#                 print('Your level - D.')
#             else:
#                 print('Your level - F. ')
# Task 5
# amount1 = int(input('amount1 = '))
# amount2 = int(input('amount2 = '))
# if amount1 > 10 and amount2 < 100:
#     if amount1 > amount2:
#         print(amount1)
#     else:
#         print(amount2)
# Task 6
# speed = int(input('speed = '))
# if 24 < speed < 56:
#     print('Speed is normal')
# else:
#     print('emergency speed')
# Task 7
# points = int(input('Point = '))
# if 9 < points < 51:
#     print('Uncorrected points')
# else:
#     print('Correct!')
# ***Programming tasks***
# Task 1
# number = int(input('Write number of your week day'))
# if number == 1:
#     print("It's Monday")
# elif number == 2:
#     print("It's Tuesday")
# elif number == 3:
#     print("It's Wednesday")
# elif number == 4:
#     print("It's Thursday")
# elif number == 5:
#     print("It's Friday")
# elif number == 6:
#     print("It's Saturday")
# elif number == 7:
#     print("It's Sunday")
# else:
#     print('Your number is incorrect!')
# Task 2
# first_width = float(input('Width of the first rectangle '))
# first_height = float(input('Height of the first rectangle'))
# second_width = float(input('Width of the second rectangle'))
# second_height = float(input('Height of the second rectangle'))
# first_square = first_height * first_width
# second_square = second_height * second_width
# if first_square == second_square:
#     print('Equal')
# elif first_square > second_square:
#     print('First is higher')
# elif second_square > first_square:
#     print('Second is higher')
# Task 3
# age = float(input('Write your age '))
# if age <= 1:
#     print("It's baby")
# elif 13 >= age > 1:
#     print("It's kid")
# elif 13 < age < 20:
#     print("It's teenager")
# elif age >= 20:
#     print("It's Adult")
# Task 4
# number = int(input('Write number '))
# if number == 1:
#     print('I')
# elif number == 2:
#     print('II')
# elif number == 3:
#     print('III')
# elif number == 4:
#     print('IV')
# elif number == 5:
#     print('V')
# elif number == 6:
#     print('VI')
# elif number == 7:
#     print('VII')
# elif number == 8:
#     print('VIII')
# elif number == 9:
#     print('IX')
# elif number == 10:
#     print('X')
# else:
#     print('Error')
# Task 5
# mass = float(input('Your mass is: '))
# weight = mass * 9.8
# if weight > 500:
#     print('Your weight is high')
# elif weight < 100:
#     print('Your weight is light')
# Task 6
# month = int(input('Write your month'))
# day = int(input('Write your day'))
# year = int(input('Write your year(2 number)'))
# if day * month == year:
#     print("It's magic data!")
# else:
#     print("It's not magic data(")
# Task 7
# first_color = input('Write your color for mix')
# second_color = input('Write your second color for mix')
# if first_color == 'Red' and second_color == 'Blue':
#     print('Violet')
# if second_color == 'Red' and first_color == 'Blue':
#     print('Violet')
# elif second_color == 'Red' and first_color == 'Yellow':
#     print('Orange')
# elif first_color == 'Red' and second_color == 'Yellow':
#     print('Orange')
# elif first_color == 'Blue' and second_color == 'Yellow':
#     print('Green')
# elif second_color == 'Blue' and first_color == 'Yellow':
#     print('Green')
# else:
#     print('Error')
# Task 8
# people = int(input('Amount of people: '))
# hot_dogs = int(input('Amount of hot dogs for every people: '))
# sausages = hot_dogs * people
# buns = sausages * 2
# packet_of_sausages = sausages / 10
# packet_of_buns = buns / 8
# remains_of_sausages = sausages % 10
# remains_of_buns = buns % 8
# print('Amount of remains buns is: ', remains_of_buns)
# print('Amount of remains sausages is: ', remains_of_sausages)
# print('Necessary packet of sausages is: ', packet_of_sausages)
# print('Necessary packet of buns is: ', packet_of_buns)
# Task 9
# pocket = int(input("Your pocket is: "))
# if pocket == 0:
#     print("Green")
# if 1 < pocket < 10 and pocket % 2 == 0:
#     print("Black")
# elif 10 > pocket > 1 == pocket % 2:
#     print("Red")
# elif 11 < pocket < 18 and pocket % 2 == 0:
#     print("Red")
# elif 11 < pocket < 18 and pocket % 2 == 1:
#     print("Black")
# elif 19 < pocket < 28 and pocket % 2 == 1:
#     print("Red")
# elif 19 < pocket < 28 and pocket % 2 == 0:
#     print("Black")
# elif 29 < pocket < 36 and pocket % 2 == 1:
#     print("Black")
# elif 29 < pocket < 36 and pocket % 2 == 0:
#     print("Red")
# else:
#     print("Error")
# Task 10
# print("You are at the game 'Counting machine'! You must enter the required number of coins to get 1 ruble! ")
# kopecks_50 = int(input("Write amount of a 50 kopecks: "))
# kopecks_10 = int(input("Write amount of a 10 kopecks: "))
# kopecks_5 = int(input("Write amount of a 5 kopecks: "))
# total_kopecks_50 = kopecks_50 * 50
# total_kopecks_10 = kopecks_10 * 10
# total_kopecks_5 = kopecks_5 * 5
# if total_kopecks_50 + total_kopecks_10 + total_kopecks_5 == 100:
#     print("You are win! Congratulations!")
# else:
#     print("Sorry, you are not winner(")
# Task 11
# amount_of_books = int(input('Write amount of books that you take in this month'))
# point = False
# if amount_of_books == 0:
#     print('You should buy some books in our shop')
# elif amount_of_books == 2:
#     point = 5
# elif amount_of_books == 4:
#     point = 15
# elif amount_of_books == 6:
#     point = 30
# elif amount_of_books >= 8:
#     point = 60
# else:
#     print('Error')
# print('You have ', point)
# Task 12
# discount = 0
# cost = 99
# amount = int(input('Write amount of a packets that you buy in our company: '))
# if 10 < amount < 19:
#     discount = 0.1
# if 20 < amount < 49:
#     discount = 0.2
# if 50 < amount < 99:
#     discount = 0.3
# if amount >= 100:
#     discount = 0.4
# total_discount = amount * cost * discount
# total_cost = amount * cost - total_discount
# if 0.1 <= discount <= 0.4:
#     print('Total discount is: ', total_discount)
# else:
#     print("You don't have discount(")
# print('Total cost is: ', total_cost)
# Task 13
# mass = int(input('Write mass of your packet: '))
# cost = 0
# if mass <= 200:
#     cost = mass / 100 * 150
# elif 200 < mass <= 600:
#     cost = mass / 100 * 300
# elif 600 < mass <= 1000:
#     cost = mass / 100 * 400
# elif mass > 1000:
#     cost = mass / 100 * 475
# else:
#     print('Error')
# print('Your salary = ', cost)
# Task 14
# mass = float(input('Write your mass: '))
# height = float(input('Write your height: '))
# BMI = mass / height
# if BMI < 18.5:
#     print('BMI is too small')
# elif 18.5 < BMI < 25:
#     print('BMI is normal')
# elif BMI > 25:
#     print('BMI is big')
# else:
#     print('Error')
# Task 15
# seconds = int(input('Write seconds, please: '))
# minute = 0
# hours = 0
# days = 0
# if 3600 >= seconds >= 60:
#     minute = seconds / 60
#     print('seconds = ', seconds, 'minute = ', minute)
# if 86400 >= seconds >= 3600:
#     minute = seconds / 60
#     hours = seconds / 3600
#     print('seconds = ', seconds, 'minute = ', minute, 'hours = ', hours)
# if seconds >= 86400:
#     minute = seconds / 60
#     hours = seconds / 3600
#     days = seconds / 86400
#     print('seconds = ', seconds, 'minute = ', minute, 'hours = ', hours, 'days = ', days)
# Task 16
# year = int(input('Write year: '))
# if year % 100 == 0 and year % 400 == 0:
#     print('This year is leap ')
# elif year % 100 != 0 and year % 4 == 0:
#     print('This year is leap ')
# else:
#     print('This year is not leap ')
# Task 17
# print("Reboot the computer and try to connect.\n(Y/N) Enter Y for yes or N for no.")
#
# user_answer = input("Did that fix the problem? ")
#
# if user_answer == "Y" or user_answer == "y" or user_answer == "N" or user_answer == "n":
#     if user_answer == "N" or user_answer == "n":
#         print("Reboot the router and try to connect")
#         user_answer = input("Did that fix the problem?")
#
#     if user_answer == "Y" or user_answer == "y" or user_answer == "N" or user_answer == "n":
#         if user_answer == "N" or user_answer == "n":
#             print("Make sure the cables between the router & modem are plugged in firmly")
#             user_answer = input("Did that fix the problem?")
#
#             if user_answer == "Y" or user_answer == "y" or user_answer == "N" or user_answer == "n":
#                 if user_answer == "N" or user_answer == "n":
#                     print("Move the router to\nto a new location\nand try to connect")
#                     user_answer = input("Did that fix the problem?")
#
#                     if user_answer == "Y" or user_answer == "y" or user_answer == "n" or user_answer == "N":
#                         print("Get a new router")
#                     else:
#                         print("Please enter Y for yes or N for no. Rerun program and try again.")
#                 else:
#                     print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
#         else:
#             print("Please enter \"Y\" for yes or \"N\" for no.\n Rerun program and try again.")
# else:
#     print("Pleas enter Y or y for yes or N or n for no")
# Task 18
#
# message = ""
#
# vegetarian = input("Is anyone in your party a vegetarian? ")
# if vegetarian == "yes" or vegetarian == "no":
#     vegan = input("Is anyone in your party a vegan? ")
#
#     if vegan == "yes" or vegan == "no":
#         gluten_free = input("Is anyone in your party gluten-free? ")
#
#         if gluten_free == "yes" or gluten_free == "no":
#             message = "\nHere are your restaurant choices:\n"
#
#             if vegetarian == "yes":
#
#                 if vegan == "yes":
#
#                     if gluten_free == "yes" or gluten_free == "no":
#                         message += "Corner Cafe\n" + \
#                                    "The Chef's Kitchen\n"
#                 else:
#                     if gluten_free == "yes":
#                         message += "Main Street Pizza Company\n" + \
#                                    "Corner Cafe\n" + \
#                                    "The Chef's Kitchen\n"
#                     else:
#                         message += "Main Street Pizza Company\n" + \
#                                    "Corner Cafe\n" + \
#                                    "Mama's Fine Italian\n" + \
#                                    "The Chef's Kitchen\n"
#             else:  # vegetarian == "no"
#
#                 if vegan == "yes":
#
#                     if gluten_free == "yes" or gluten_free == "no":
#                         message += "Corner Cafe\nThe Chef's Kitchen\n"
#
#                 else:  # vegan == "no"
#
#                     if gluten_free == "yes":
#                         message += "Main Street Pizza Company\n" + \
#                                    "Corner Cafe\n" + \
#                                    "The Chef's Kitchen\n"
#
#                     else:  # gluten free == "no"
#                         message += "Joe's Gourmet Burgers\n" + \
#                                    "Main Street Pizza Company\n" + \
#                                    "Corner Cafe\n" + \
#                                    "Mama's Fine Italian\n" + \
#                                    "The Chef's Kitchen\n"
#
#         else:
#             message = "Enter either 'yes' or 'no'.\nRerun the program and try again."
#
#     else:
#         message = "Enter either 'yes' or 'no'.\nRerun the program and try again."
#
# else:
#     message = "Enter either 'yes' or 'no'.\nRerun the program and try again."
#
# print(message)