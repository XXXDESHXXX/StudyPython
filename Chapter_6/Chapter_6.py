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
#     my_file = open('numbers.txt', 'w')
#     for i in range(1, 101):
#         my_file.write(str(i) + '\n')
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
