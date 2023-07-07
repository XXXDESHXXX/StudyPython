# ***Algorithmic simulator***
# Task 1
# def main():
#     name = input('Input your name: ')
#     my_file = open('my_name.txt', 'w')
#     my_file.write(name)
#     my_file.close()
#     print('Name wrote')
#
#
# main()
# Task 2
# def main():
#     name = input('Input your name: ')
#     my_file = open('my_name.txt', 'w')
#     my_file.write(name)
#     my_file = open('my_name.txt', 'r')
#     content = my_file.read()
#     print(content)
#     print('Name wrote')
#     my_file.close()
#
#
# main()
# Task 3
# def main():
#     my_file = open('numbers.txt', 'w')
#     for i in range(1, 101):
#         my_file.write(str(i) + '\n')
#     my_file.close()
#     print('Finish')
#
#
# main()
# Task 4
# def main():
#     my_file = open('numbers.txt', 'w')
#     for i in range(1, 101):
#         my_file.write(str(i) + '\n')
#     my_file = open('numbers.txt', 'r')
#     content = my_file.read()
#     print(content)
#     my_file.close()
#     print('Finish')
#
#
# main()
# Task 5
# def main():
#     sum_of_numbers = 0
#     my_file = open('numbers.txt', 'r')
#     content = my_file.readline()
#     while content != '':
#         sum_of_numbers += int(content)
#         print(content)
#         content = my_file.readline()
#     print(sum_of_numbers)
#     my_file.close()
#     print('Finish')
#
#
# main()
# Task 6
# def main():
#     my_file = open('numbers.txt', 'r')
#     my_file.close()
#     print('Finish')
#
#
# main()
# Task 7
# import os
#
#
# def main():
#     found = False
#     search = input('Input name that you want to delete: ')
#     students_file = open('students.txt', 'r')
#     temp_file = open('temp.txt', 'w')
#     student = students_file.readline()
#     while student != '':
#         score = int(students_file.readline())
#         student = student.rstrip('\n')
#         if student != search:
#             temp_file.write(student + '\n')
#             temp_file.write(str(score) + '\n')
#         else:
#             found = True
#         student = students_file.readline()
#     students_file.close()
#     temp_file.close()
#     os.remove('students.txt')
#     os.rename('temp.txt', 'students.txt')
#     if found:
#         print('File updated')
#     else:
#         print('File not updated')
#
#
# main()
# Task 8
# import os
#
#
# def main():
#     found = False
#     search = input('Input student that mark you want to delete: ')
#     update_score = int(input('Input update student score: '))
#     students_file = open('students.txt', 'r')
#     temp_file = open('temp.txt', 'w')
#     student = students_file.readline()
#     while student != '':
#         score = int(students_file.readline())
#         student = student.rstrip('\n')
#         if student == search:
#             temp_file.write(student + '\n')
#             temp_file.write(str(update_score) + '\n')
#             found = True
#         else:
#             temp_file.write(student + '\n')
#             temp_file.write(str(score) + '\n')
#         student = students_file.readline()
#     students_file.close()
#     temp_file.close()
#     os.remove('students.txt')
#     os.rename('temp.txt', 'students.txt')
#     if found:
#         print('File updated')
#     else:
#         print('File not updated')
#
#
# main()
# ***Programming tasks***
# Task 1
# def main():
#     my_file = open('6.1_Numbers.txt', 'r')
#     all_numbers = my_file.read()
#     my_file.close()
#     print(all_numbers)
#
#
# main()
# Task 2
# def main():
#     filename = input('Input filename: ')
#     num_str = int(input('Input numer of string: '))
#     my_file = open(filename, 'r')
#     try:
#         for content in my_file:
#             if num_str > 0:
#                 print(content)
#             num_str -= 1
#         my_file.close()
#     except ValueError:
#         print('Error')
#     except FileNotFoundError:
#         print('FileNotFoundError')
#
#
# main()
# Task 3
# def main():
#     strings = 0
#     filename = input('Input filename: ')
#     my_file = open(filename, 'r')
#     try:
#         for content in my_file:
#             content = content.rstrip('\n')
#             strings += 1
#             print(strings, ':', content)
#         my_file.close()
#     except ValueError:
#         print('Error')
#     except FileNotFoundError:
#         print('FileNotFoundError')
#
#
# main()
# Task 4
# def main():
#     strings = 0
#     filename = input('Input filename: ')
#     my_file = open(filename, 'r')
#     try:
#         for content in my_file:
#             content = content.rstrip('\n')
#             strings += 1
#             print(content)
#         print('Amount of strings is: ', strings)
#         my_file.close()
#     except ValueError:
#         print('Error')
#     except FileNotFoundError:
#         print('FileNotFoundError')
#
#
# main()
# Task 5
# def main():
#     sum_of_numbers = 0
#     my_file = open('numbers.txt', 'r')
#     content = my_file.readline()
#     while content != '':
#         content = content.rstrip('\n')
#         sum_of_numbers += int(content)
#         print(content)
#         content = my_file.readline()
#     print(sum_of_numbers)
#     my_file.close()
#
#
# main()
# Task 6
# def main():
#     sum_of_numbers = 0
#     amount_of_numbers = 0
#     my_file = open('numbers.txt', 'r')
#     content = my_file.readline()
#     while content != '':
#         content = content.rstrip('\n')
#         sum_of_numbers += int(content)
#         amount_of_numbers += 1
#         content = my_file.readline()
#     average_of_numbers = sum_of_numbers / amount_of_numbers
#     print(average_of_numbers)
#     my_file.close()
#
#
# main()
# Task 7
# import random
#
#
# def main():
#     diapason = int(input('Input diapason of numbers: '))
#     my_file = open('6.7_Numbers.txt', 'w')
#     for content in range(diapason):
#         my_file.write(f"{random.randint(1, 500)} \n")
#     my_file.close()
#
#
# main()
# Task 8
# def main():
#     sum_of_numbers = 0
#     strings = 0
#     filename = input('Input filename: ')
#     my_file = open(filename, 'r')
#     try:
#         for content in my_file:
#             content = content.rstrip('\n')
#             strings += 1
#             sum_of_numbers += int(content)
#             print(content)
#         print('Amount of strings is: ', strings)
#         print('Sum of numbers is: ', sum_of_numbers)
#         my_file.close()
#     except ValueError:
#         print('Error')
#     except FileNotFoundError:
#         print('FileNotFoundError')
#
#
# main()
# Task 9
# def main():
#     sum_of_numbers = 0
#     amount_of_numbers = 0
#     try:
#         my_file = open('numbers.txt', 'r')
#         content = my_file.readline()
#         while content != '':
#             content = content.rstrip('\n')
#             sum_of_numbers += int(content)
#             amount_of_numbers += 1
#             content = my_file.readline()
#         average_of_numbers = sum_of_numbers / amount_of_numbers
#         print(average_of_numbers)
#         my_file.close()
#     except ValueError:
#         print('ValueError')
#     except IOError:
#         print('IOError')
#
#
# main()
# Task 10
# def main():
#     amount_of_players = int(input('Input amount of players: '))
#     golf_file = open('golf.txt', 'w')
#     for content in range(amount_of_players):
#         name = input('Input name: ')
#         score = int(input('Input score: '))
#         golf_file.write(f"{name} \n")
#         golf_file.write(f"{score} \n")
#     golf_file.close()
#
#
# main()
# def main():
#     golf_file = open('golf.txt', 'r')
#     name = golf_file.readline()
#     while name != '':
#         score_field = golf_file.readline()
#         name = name.rstrip('\n')
#         score_field = score_field.rstrip('\n')
#         print('Name: ', name)
#         print('Score: ', score_field)
#         name = golf_file.readline()
#     golf_file.close()
#
#
# main()
# Task 11
# def main():
#     name = input('Input your name: ')
#     descr = input('Write your description: ')
#     my_file = open('html.html', 'w')
#     my_file.write(f"<!DOCTYPE html> \n")
#     my_file.write(f"<html> \n")
#     my_file.write(f"<head> \n")
#     my_file.write(f"</head> \n")
#     my_file.write(f"<body> \n")
#     my_file.write(f"<center> \n")
#     my_file.write(f"<h1> {name} </h1 \n")
#     my_file.write(f"</center> \n")
#     my_file.write(f"<hr /> \n")
#     my_file.write(f"{descr} \n")
#     my_file.write(f"<hr /> \n")
#     my_file.write(f"</body> \n")
#     my_file.write(f"</html> \n")
#     my_file.close()
#
#
# main()
# Task 12
# DAYS_YEAR = 365
#
#
# def main():
#     days = 2
#     open_file = open('steps.txt', 'r')
#     content = open_file.readline()
#
#     total_jan = 0
#     total_feb = 0
#     total_mar = 0
#     total_apr = 0
#     total_may = 0
#     total_jun = 0
#     total_jul = 0
#     total_aug = 0
#     total_sep = 0
#     total_oct = 0
#     total_nov = 0
#     total_dec = 0
#     while content != '':
#         if days <= 32:
#             content = content.rstrip('\n')
#             total_jan += int(content)
#             days += 1
#         if 32 < days <= 60:
#             content = content.rstrip('\n')
#             total_feb += int(content)
#             days += 1
#         if 60 < days <= 90:
#             content = content.rstrip('\n')
#             total_mar += int(content)
#             days += 1
#         if 90 < days <= 121:
#             content = content.rstrip('\n')
#             total_apr += int(content)
#             days += 1
#         if 121 < days <= 151:
#             content = content.rstrip('\n')
#             total_may += int(content)
#             days += 1
#         if 151 < days <= 182:
#             content = content.rstrip('\n')
#             total_jun += int(content)
#             days += 1
#         if 182 < days <= 212:
#             content = content.rstrip('\n')
#             total_jul += int(content)
#             days += 1
#         if 212 < days <= 243:
#             content = content.rstrip('\n')
#             total_aug += int(content)
#             days += 1
#         if 243 < days <= 273:
#             content = content.rstrip('\n')
#             total_sep += int(content)
#             days += 1
#         if 273 < days <= 304:
#             content = content.rstrip('\n')
#             total_oct += int(content)
#             days += 1
#         if 304 < days <= 334:
#             content = content.rstrip('\n')
#             total_nov += int(content)
#             days += 1
#         if 334 < days <= 365:
#             content = content.rstrip('\n')
#             total_dec += int(content)
#             days += 1
#
#         content = open_file.readline()
#     print('Jan: ', total_jan)
#     print('Feb: ', total_feb)
#     print('Mar: ', total_mar)
#     print('Apr: ', total_apr)
#     print('May: ', total_may)
#     print('Jun: ', total_jun)
#     print('Jul: ', total_jul)
#     print('Aug: ', total_aug)
#     print('Sep: ', total_sep)
#     print('Oct: ', total_oct)
#     print('Nov: ', total_nov)
#     print('Dec: ', total_dec)
#     open_file.close()
#
#
# main()
