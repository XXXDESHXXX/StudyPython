# ***Algorithmic simulator***
# Task 1
# def main():
#     my_list = ['Einstein', 'Newton', 'Copernicus', 'Kepler']
#     print(my_list)
#
#
# main()
# Task 2
# def main():
#     names = [1, 2, 3, 4, 5, 6, 9, 11, 222]
#     for number in names:
#         print(number)
#
#
# main()
# Task 3
# import random
#
#
# def main():
#     iteration = 0
#     element = random.randint(1, 101)
#     numbers1 = []
#     while iteration != 100:
#         iteration += 1
#         numbers1.append(element)
#         element = random.randint(1, 100)
#     numbers2 = [numbers1]
#     print(numbers2)
#
#
# main()
# Task 5
# def main():
#     my_list = [1, 3, 44, 55, 100]
#     result = sum_list(my_list)
#     print(result)
#
#
# def sum_list(my_list):
#     total = 0
#     for value in my_list:
#         total += value
#     return total
#
#
# main()
# Task 6
# def main():
#     my_list = ['Rubi', 'Anton', 'Artem']
#     search = input('Input name that you want find: ')
#     if search in my_list:
#         print(search, 'is found!')
#     else:
#         print('This name not found')
#
#
# main()
# Task 7
# list1 = [40, 50, 60]
# list2 = [10, 20, 30]
# list3 = list1 + list2
# print(list3)
# Task 8
# import random
#
#
# ROWS = 5
# COLUMNS = 3
#
#
# def main():
#     values = [[0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0],
#               [0, 0, 0]]
#     for r in range(ROWS):
#         for c in range(COLUMNS):
#             values[r][c] = int(input('Input value: '))
#
#     print(values)
#
#
# main()
# ***Programming tasks***
# Task 1
# def main():
#     total_sales = 0
#     sales_list = []
#     for _ in range(7):
#         week_sales = int(input('Input sales of every day in this week: '))
#         sales_list.append(week_sales)
#     print(sales_list)
#     for value in sales_list:
#         total_sales += value
#     print(total_sales)
#
#
# main()
# Task 2
# import random
#
#
# def main():
#     lottery_number = 0
#     list_of_numbers = []
#     for _ in range(7):
#         lottery_number = random.randint(0, 9)
#         list_of_numbers.append(lottery_number)
#     print(list_of_numbers)
#
#
# main()
# Task 3
# def main():
#     total_rainfall = 0
#     list_of_rainfall = []
#     for _ in range(12):
#         month_rainfall = float(input('Input amount of rainfall in this month: '))
#         list_of_rainfall.append(month_rainfall)
#     for value in list_of_rainfall:
#         total_rainfall += value
#     average_rainfall = total_rainfall / 12
#     print(total_rainfall, average_rainfall, max(list_of_rainfall), min(list_of_rainfall))
#
#
# main()
# Task 4
# def main():
#     sum_of_numbers = 0
#     list_of_numbers = []
#     for _ in range(20):
#         number = int(input('Input number: '))
#         list_of_numbers.append(number)
#     for value in list_of_numbers:
#         sum_of_numbers += value
#     average_value = sum_of_numbers / 12
#     print(sum_of_numbers, average_value, max(list_of_numbers), min(list_of_numbers))
#
#
# main()
# Task 5
# def main():
#     my_list = []
#     my_file = open('charge_account.txt', 'r')
#     my_list = my_file.read()
#     search = input('Input search number: ')
#     if search in my_list:
#         print(search, 'Is found')
#     else:
#         print(search, 'Is not found')
#
#
# main()
# Task 6
# def main():
#     my_list = []
#     for _ in range(10):
#         value = int(input('Input list number: '))
#         my_list.append(value)
#     number = int(input('Input number: '))
#     function_value = logic_function(my_list, number)
#     print(function_value)
#
#
# def logic_function(my_list, number):
#     list_of_max_numbers = []
#     for value in my_list:
#         if value > number:
#             list_of_max_numbers.append(value)
#     return list_of_max_numbers
#
#
# main()
# Task 7


def main():
    correct_answers = 0
    incorrect_answers = 0
    list_of_correct = []
    list_of_incorrect = []
    marks_file = open('Marks.txt', 'r')
    solution_file = open('Solution.txt', 'r')
    solution_list = solution_file.readlines()
    mark_list = marks_file.readlines()
    marks_file.close()
    solution_file.close()
    index = 0
    while index < len(mark_list):
        mark_list[index] = mark_list[index].rstrip('\n')
        solution_list[index] = solution_list[index].rstrip('\n')
        index += 1
    for mark_value in mark_list:
        if mark_value == solution_list:
            list_of_correct.append(solution_list)
            correct_answers += 1
        elif mark_value != solution_list:
            list_of_incorrect.append(solution_list)
            incorrect_answers += 1
    if correct_answers >= 15:
        print('You are pass the exam!')
    else:
        print("You are don't pass(")
    print(correct_answers, incorrect_answers)
    print(list_of_incorrect)


main()
