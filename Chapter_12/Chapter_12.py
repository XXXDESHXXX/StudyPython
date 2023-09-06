# ***Programming tasks***
# Task 1
# def main():
#     number = int(input('Input number'))
#     printing(number)
#
#
# def printing(number):
#     if number != 1:
#         printing(number - 1)
#     print(number)
#
#
# main()
# Task 2
# def main():
#     first_number = int(input('Input first number: '))
#     second_number = int(input('Input second number: '))
#     numbers = multiplication(first_number, second_number)
#     print(numbers)
#
#
# def multiplication(first_number, second_number):
#     if first_number == 0:
#         return 0
#     return second_number + multiplication(first_number - 1, second_number)
#
#
# main()
# Task 3
# def main():
#     string_of_stars = int(input('Input amount of a stars: '))
#     printing(string_of_stars)
#
#
# def printing(string_of_stars):
#     if string_of_stars > 0:
#         print('*' * string_of_stars)
#         printing(string_of_stars - 1)
#
#
# main()
# Task 4
# def main():
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#     max_element(numbers)
#
#
# def max_element(numbers):
#     if len(numbers) <= 1:
#         return numbers[0]
#     else:
#         print(numbers[1:])
#         max = max_element(numbers[1:])
#         return max if max > numbers[0] else numbers[0]
#
#
# main()
# Task 5
# def main():
#     numbers = [62, 50, 40, 30, 1]
#     total_sum = sum_of_numbers(numbers)
#     print(total_sum)
#
#
# def sum_of_numbers(numbers):
#     if not numbers:
#         return 0
#     return numbers[0] + sum_of_numbers(numbers[1:])
#
#
# main()
# Task 6
# def main():
#     number = int(input('Input number: '))
#     total_sum = sum_of_numbers(number)
#     print(total_sum)
#
#
# def sum_of_numbers(number):
#     if number == 0:
#         return 0
#     return number + sum_of_numbers(number - 1)
#
#
# main()
# Task 7
# def main():
#     degree_number = int(input('Input degree: '))
#     number = int(input('Input number: '))
#     total_number = degree(degree_number, number)
#     print(total_number)
#
#
# def degree(degree_number, number):
#     if degree_number <= 0:
#         return 1
#     return number * degree(degree_number - 1, number)
#
#
# main()
