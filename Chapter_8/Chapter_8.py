# ***Algorithmic simulator***
# Task 1
# def main():
#     choice = input('Input your choice: ')
#     if choice.upper() and choice.lower() == 'y' or 'Y':
#         print('Yes')
#
#
# main()
# Task 2
# def main():
#     count_space = 0
#     mystring = input('Input string: ')
#     for letter in mystring:
#         if letter.isspace():
#             count_space += 1
#     print(count_space)
#
#
# main()
# Task 3
# def main():
#     count_digit = 0
#     mystring = input('Input string: ')
#     for letter in mystring:
#         if letter.isdigit():
#             count_digit += 1
#     print(count_digit)
#
#
# main()
# Task 4
# def main():
#     count_lower = 0
#     mystring = input('Input string: ')
#     for letter in mystring:
#         if letter.islower():
#             count_lower += 1
#     print(count_lower)
#
#
# main()
# Task 5
# def main():
#     mystring = input('Input string: ')
#     if mystring.endswith('.com'):
#         print('True')
#     else:
#         print('False')
#
#
# main()
# Task 6
# def main():
#     mystring = input('Input string: ')
#     new_string = mystring.replace('d', 'D')
#     print(new_string)
#
#
# main()
# Task 7
# def main():
#     mystring = input('Input string: ')[::-1]
#     print(mystring)
#
#
# main()
# Task 8
# def main():
#     mystring = input('Input string: ')
#     print(mystring[:3])
#
#
# main()
# Task 9
# def main():
#     mystring = input('Input string: ')
#     new_string = mystring[-3:]
#     print(new_string)
#
#
# main()
# Task 10
# def main():
#     mystring = 'cakes>milk>apple>bananas>STAA$$'
#     new_string = mystring.split('>')
#     print(new_string)
#
#
# main()
# ***Programming tasks***
# Task 1
# def main():
#     initial = ""
#     mystring = input('Input your full name: ')
#     for letter in mystring.split():
#         initial += letter[:1] + "."
#     print(initial)
#
#
# main()
# Task 2
# def main():
#     sum_of_numbers = 0
#     my_string = input('Input string of numbers: ')
#     for value in my_string:
#         sum_of_numbers += int(value)
#     print(sum_of_numbers)
#
#
# main()
# Task 3
# def main():
#     date = input('Input date in format dd/mm/yyyy: ')
#     months = ["January", "February", "March", "April", "May",
#               "June", "July", "August", "September", "October",
#               "November", "December"]
#     date_list = date.split('/')
#     new_date = str(months[int(date_list[0]) - 1]) + " " + str(
#         date_list[1]) + "," + " " + str(date_list[2])
#     print(new_date)
#
#
# main()
# Task 4
# def main():
#     character = (" ", ",", ".", "?", "0", "1", "2", "3", "4", "5", "6", "7",
#                  "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
#                  "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
#                  "W", "X", "Y", "Z")
#     morse = (" ", "--..--", ".-.-.-", "..--..", "-----", ".----", "..---",
#              "...--", "....-", ".....", "-....", "--...", "---..", "----.",
#              ".-", "-...",
#              "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
#              ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
#              "..-", "...-", ".--", "-..-",
#              "-.-", "--..")
#     string = input('Input string: ')
#     index = 0
#     while index < len(string):
#         position = character.index(string[index])
#         print(morse[position],
#               end=" ")
#         index += 1
#
#
# main()
# Task 5
# def main():
#     telephone_number = input('Input your telephone number: ')
#     for ch in telephone_number:
#         if ch.islower():
#             ch = ch.upper()
#         if ch.isdigit():
#             print(ch, end='')
#         elif ch == '-':
#             print('-', end='')
#         elif ch == 'A' or ch == 'B' or ch == 'C':
#             print('2', end='')
#         elif ch == 'D' or ch == 'E' or ch == 'F':
#             print('3', end='')
#         elif ch == 'G' or ch == 'H' or ch == 'I':
#             print('4', end='')
#         elif ch == 'J' or ch == 'K' or ch == 'L' \
#                 or ch == 'V':
#             print('5', end='')
#         elif ch == 'M' or ch == 'N' or ch == 'O' \
#                 or ch == 'U':
#             print('6', end='')
#         elif ch == 'P' or ch == 'Q' or ch == 'R' \
#                 or ch == 'S' or ch == 'T':
#             print('7', end='')
#         elif ch == 'W' or ch == 'X' or ch == 'Y' \
#                 or ch == 'Z':
#             print('8', end='')
#         else:
#             print('-', end='')
#
#
# main()
# Task 6
# def main():
#     word_counter = 1
#     text_file = open('Text.txt', 'r')
#     content = text_file.readline()
#     num_string = 0
#     while num_string < len(content):
#         content_split = content.split()
#         word_counter += len(content.split())
#         content = text_file.readline()
#         num_string += 1
#     median_of_words = word_counter / num_string
#     print(median_of_words)
#
#
# main()
# Task 7
# def main():
#     upper_counter = 0
#     lower_counter = 0
#     number_counter = 0
#     space_counter = 0
#     text_file = open('Text.txt', 'r')
#     content = text_file.readlines()
#     for string in content:
#         for ch in string:
#             if ch.islower():
#                 lower_counter += 1
#             if ch.isalnum():
#                 number_counter += 1
#             if ch.isspace():
#                 space_counter += 1
#             if ch.isupper():
#                 upper_counter += 1
#     print(upper_counter, lower_counter, number_counter, space_counter)
#
#
# main()
# Task 8
# def main():
#     my_string = input("Enter a string: ")
#     print()
#     print(my_string)
#     capitalizer_first_word(my_string)
#
#
# def capitalizer_first_word(my_string):
#     my_string2 = my_string.split()
#
#     for i in range(0, len(my_string2)):
#         if my_string2[i - 1].endswith('.') or my_string2[i - 1].endswith('!') \
#                 or my_string2[i - 1].endswith('?'):
#             print(my_string2[i].capitalize(), end=' ')
#         else:
#             print(my_string2[i], end=' ')
#
#
# main()
# Task 9
# def main():
#     list_of_vowels = ('a', 'e', 'y', 'o')
#     consonants_counter = 0
#     vowels_counter = 0
#     my_string = input('Input string: ')
#     for ch in my_string:
#         if ch in list_of_vowels:
#             vowels_counter += 1
#         else:
#             consonants_counter += 1
#     print(consonants_counter, vowels_counter)
#
#
# main()
# Task 10
# from collections import Counter
#
#
# def main():
#     user_string = input("Enter a string: ")
#     max_3 = Counter(user_string).most_common(3)
#     print("The most frequently occuring letter is", max_3)
#
#
# main()
# Task 11
# def main():
#     my_string = input('Input a string: ')
#     print(my_string[0].upper(), end='')
#     for i in range(1, len(my_string)):
#         if my_string[i].isupper():
#             print(' ', end='')
#             print(my_string[i].lower(), end='')
#         else:
#             print(my_string[i], end='')
#
#
# main()
# Task 12
def main():
    my_string = input('Input a string: ')
    split_string = my_string.split()
    for i in split_string:
        new_string = i[1:] + i[0]
        print(new_string + 'KI', end=' ')


main()
