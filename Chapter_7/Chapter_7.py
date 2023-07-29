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
# def main():
#     correct_answers = 0
#     incorrect_answers = 0
#     necessary_answers = ["A", "C", "A", "A", "D",
#                          "B", "C", "A", "C", "B",
#                          "A", "D", "C", "A", "D",
#                          "C", "B", "B", "D", "A"]
#     list_of_incorrect = []
#     list_of_correct = []
#     solution_file = open('Solution.txt', 'r')
#     solution_list = solution_file.readlines()
#     index = 0
#     while index < len(solution_list):
#         solution_list[index] = solution_list[index].rstrip('\n')
#         index += 1
#     i = 0
#     while i < len(necessary_answers):
#         if necessary_answers[i] == solution_list[i]:
#             correct_answers += 1
#             list_of_correct.append(necessary_answers[i])
#         else:
#             incorrect_answers += 1
#             list_of_incorrect.append(solution_list[i])
#             print("The question #", i + 1, " is wrong!", sep="")
#         i += 1
#     if incorrect_answers >= 15:
#         print('You are not pass the exam( ')
#     else:
#         print('You are pass the exam! Congratulations!')
#     print(correct_answers, incorrect_answers, list_of_correct, list_of_incorrect)
#     solution_file.close()
#
#
# main()
# Task 8
# def main():
#     girls_names_file = open('GirlNames.txt', 'r')
#     boys_names_file = open('BoysNames.txt', 'r')
#     girls_names_list = girls_names_file.read().splitlines()
#     boys_names_list = boys_names_file.read().splitlines()
#     search = input('Input name, please: ')
#     if search in girls_names_list:
#         print('Yes it is found')
#     else:
#         print('It is not found')
#     if search in boys_names_list:
#         print('Yes, it is found')
#     else:
#         print('It is not found')
#     girls_names_file.close()
#     boys_names_file.close()
#
#
# main()
# Task 9
# def main():
#     population_file = open('USPopulation.txt', 'r')
#     population_list = population_file.readlines()
#     index = 0
#     while index < len(population_list):
#         population_list[index] = int(population_list[index])
#         index += 1
#     annual_change = annualchange(population_list)
#     total = 0
#     for elements in annual_change:
#         total += elements
#     average = total / len(annual_change)
#     print(average)
#     print(max(annual_change))
#     print(min(annual_change))
#
#
# def annualchange(population_list):
#     annual_change = [0] * (len(population_list) - 1)
#     index = 0
#     while index < len(population_list) - 1:
#         annual_change[index] = population_list[index + 1] - population_list[index]
#         index += 1
#     return annual_change
#
#
# main()
# Task 10
# def main():
#     total_wins = 0
#     winners_file = open('Winners.txt', 'r')
#     winners_list = winners_file.read().splitlines()
#     search = input('Input team name that you wanna find: ')
#     for value in winners_list:
#         if value == search:
#             total_wins += 1
#     print(total_wins)
#
#
# main()
# Task 11
# Task 12
# def main():
#     n = int(input("n="))
#     lst = []
#     for i in range(2, n + 1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             lst.append(i)
#     print(lst)
#
#
# main()
# Task 13
# import random
#
#
# def main():
#     task_file = open('Task13.txt', 'r')
#     answer_list = task_file.read().splitlines()
#     answer = input('Would you like to start game? ')
#     while answer == 'yes':
#         question = input('Ask a question, please: ')
#         print(answer_list[random.randint(1, 12)])
#         answer = input('Would you like to continue?')
#
#
# main()
