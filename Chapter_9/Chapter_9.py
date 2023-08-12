# ***Algorithmic simulator***
# Task 1
# def main():
#     dictionary = {'a': 1,
#                   'b': 2,
#                   'c': 3}
#     print(dictionary)
#
#
# main()
# Task 2
# def main():
#     dictionary = dict()
#     print(dictionary)
#
#
# main()
# Task 3
# def main():
#     search = input('Input name that you want to find in dictionary: ')
#     dct = {'James': 1, 'Anna': 2}
#     if search in dct:
#         print(dct[search])
#     else:
#         print('Not found(')
#
#
# main()
# Task 4
# def main():
#     delete_key = input('Input key that you want to delete in dictionary: ')
#     dct = {'James': 1, 'Jim': 2}
#     if delete_key in dct:
#         del dct[delete_key]
#         print(dct)
#     else:
#         print('Not found(')
#
#
# main()
# Task 5
# def main():
#     myset = {10, 20, 30, 40}
#     print(myset)
#
#
# main()
# Task 6
# def main():
#     set1 = {1, 2, 3, 4}
#     set2 = {5, 6, 7, 8}
#     set3 = set1.union(set2)
#     print(set3)
#
#
# main()
# Task 7
# def main():
#     set1 = {1, 2, 3, 4}
#     set2 = {1, 2, 7, 8}
#     set3 = set1.intersection(set2)
#     print(set3)
#
#
# main()
# Task 8
# def main():
#     set1 = {1, 2, 3}
#     set2 = {3, 4, 5}
#     set3 = set1.difference(set2)
#     print(set3)
#
#
# main()
# Task 9
# def main():
#     set1 = {1, 2, 3}
#     set2 = {3, 4, 5}
#     set3 = set2.difference(set1)
#     print(set3)
#
#
# main()
# Task 10
# def main():
#     set1 = {1, 2, 3}
#     set2 = {2, 3, 5}
#     set3 = set1.symmetric_difference(set2)
#     print(set3)
#
#
# main()
# Task 11
# import pickle
#
#
# def main():
#     dct = {'James': 1,
#            'Anna': 2,
#            'Jim': 3}
#     outputfile = open('dct.dat', 'wb')
#     pickle.dump(dct, outputfile)
#     outputfile.close()
#
#
# main()
# Task 12
# import pickle
#
#
# def main():
#     input_file = open('dct.dat', 'rb')
#     object_of_file = pickle.load(input_file)
#     print(object_of_file)
#
#
# main()
# ***Programming tasks***
# Task 1
# def main():
#     curse_dictionary = {'CS101': 3004,
#                          'CS102': 4501,
#                          'CS103': 6755,
#                          'CS104': 1411}
#     professors_dictionary = {'CS101': 'Haints',
#                              'CS102': 'Alvarado',
#                              'CS103': 'Rich',
#                              'NT110': 'Berk',
#                              'CM241': 'Li'}
#     time_dictionary = {'CS101': '8:00',
#                        'CS102': '9:00',
#                        'CS103': '10:00',
#                        'NT110': '11:00',
#                        'CM241': '13:00'}
#     search = input('Input a curse number: ')
#     print(curse_dictionary[search.upper()])
#     print(professors_dictionary[search.upper()])
#     print(time_dictionary[search.upper()])
#
#
# main()
# Task 2
# import random
#
#
# def main():
#     right_answers = 0
#     mistakes = 0
#     states_dictionary = {'Arizona': 'Phoenix',
#                          'New Mexico': 'Santa Fe',
#                          'Colorado': 'Denver',
#                          'Nevada': 'California',
#                          'Oregon': 'Salem',
#                          'Washington': 'Olympia'}
#     answer = ''
#     continue_answer = 'YES'
#     try:
#         while continue_answer == 'YES':
#             state, capital = random.choice(list(states_dictionary.items()))
#             print(state)
#             answer = input('Input capital of this state: ')
#             if answer == capital:
#                 right_answers += 1
#             else:
#                 mistakes += 1
#             continue_answer = input('Would you like to continue').upper()
#         print(right_answers)
#         print(mistakes)
#     except KeyError:
#         print('You answer on all questions')
#
#
# main()
# Task 3
# def main():
#     coding_table = {'A': '%', 'B': '@', 'D': '^'}
#     coding_file = open('Coding_file.txt', 'r')
#     file_content = coding_file.readline()
#     list_content = list(file_content)
#     new_file_content = ''
#     for letters in list_content:
#         for key, value in coding_table.items():
#             if letters == key:
#                 new_file_content += value
#     print(new_file_content)
#
#
# main()
# Task 4
# def main():
#     my_string = ("Welcome! Are are are you completely new to programming? "
#               "'If not then we presume you will be looking for information "
#               "about why and and  how to get started with Python. "
#               "Fortunately an experienced programmer in any programming "
#               "language (whatever it may be) can pick up Python very very "
#               "very very very quickly. It's also easy for beginners "
#               "to use 4 4 4 4   and learn, so jump in!")
#     new_file = open('text_file_9.4.txt', 'w')
#     content = my_string.split()
#     content_clear = set([])
#     for i in content:
#         if i.endswith('.') or i.endswith(',') \
#                 or i.endswith('!') or i.endswith(':') \
#                 or i.endswith(')') or i.endswith('?') \
#                 or i.endswith('}') or i.endswith('"'):
#             new_file.write(i[:-1] + '\n')
#             content_clear.update([i[:-1]])
#             continue
#         if i.startswith('.') or i.startswith(',') \
#                 or i.startswith('!') or i.startswith(':') \
#                 or i.startswith('(') or i.startswith('?') \
#                 or i.startswith('{') or i.startswith("'") or \
#                 i.startswith('"'):
#             new_file.write(i[1:] + '\n')
#             content_clear.update([i[1:]])
#             continue
#         else:
#             new_file.write(i + '\n')
#             content_clear.update([i])
#     print(len(content_clear))
#     new_file.close()
#
#
# main()
# Task 5
# def main():
#     my_str = ("Welcome! Are are are you completely new to programming? "
#               "'If not then we presume you will be looking for information "
#               "about why and and  how to get started with Python. "
#               "Fortunately an experienced programmer in any programming "
#               "language (whatever it may be) can pick up Python very very "
#               "very very very quickly. It's also easy for beginners "
#               "to use 4 4 4 4   and learn, so jump in!")
#     validated_str = replace_letters(my_str, [',', '.', '!', '?', ')', '('])
#     validated_list = validated_str.split()
#     word_dictionary = {}
#     for word in validated_list:
#         word_counter = 0
#         for words in validated_list:
#             if word == words:
#                 word_counter += 1
#                 word_dictionary[word] = word_counter
#     print(word_dictionary)
#
#
# def replace_letters(my_str, symbols):
#     for symbol in symbols:
#         my_str = my_str.replace(symbol, "")
#     return my_str
#
#
# main()
# Task 6
# def main():
#     my_str = ("Welcome! Are are are you completely new to programming? 'If"
#               " not then we presume you will be looking for information about "
#               "why and how to get started with Python. Fortunately an "
#               "experienced programmer in any programming language (whatever "
#               "it may be) can pick up Python very quickly. It's also easy for"
#               " beginners to use and learn, so jump in! can pick up Python "
#               "very quickly. Newton ")
#     my_str2 = ("Welcome! Are are are you completely new to programming? 'If "
#                "not then we presume you will be looking for information about "
#                "why and how to get started with Python. Fortunately an "
#                "experienced programmer in any programming language (whatever "
#                "it may be) can pick up Python very quickly. It's also easy "
#                "for beginners to use and learn, so jump in! can pick "
#                "up Python very quickly. Lomonosov")
#     first_set = set()
#     second_set = set()
#     file_name = 'text_count.txt'
#     file_name2 = 'text_count_2.txt'
#     first_split_str = split_str(my_str)
#     second_split_str = split_str(my_str2)
#     create_file(first_split_str, file_name)
#     create_file(second_split_str, file_name2)
#     first_replaced_content = replace_letters(my_str, [',', '.', '!', '?', ')', '('])
#     second_replaced_content = replace_letters(my_str2, [',', '.', '!', '?', ')', '('])
#     first_updated_set = set_update(first_set, first_replaced_content)
#     second_updated_set = set_update(second_set, second_replaced_content)
#     print_func(first_updated_set, second_updated_set)
#
#
# def create_file(splited_str, file_name):
#     text_file = open(str(file_name), 'w')
#     for words in splited_str:
#         text_file.write(words + '\n')
#     text_file.close()
#
#
# def split_str(my_str):
#     splited_str = my_str.split()
#     return splited_str
#
#
# def replace_letters(my_str, symbols):
#     for symbol in symbols:
#         my_str = my_str.replace(symbol, "")
#     replaced_splited_str = my_str.split()
#     return replaced_splited_str
#
#
# def set_update(set_name, content_rstrip):
#     for element in content_rstrip:
#         set_name.update([element])
#     return set_name
#
#
# def print_func(first_set, second_set):
#     print('All unique words in both files: ')
#     union_file = first_set | second_set
#     print('Number of words: ', len(union_file))
#     print()
#     print('Set words included in both files:')
#     inter_file = first_set & second_set
#     print(inter_file)
#     print('Number of words: ', len(inter_file))
#     print()
#     print('Set words from the first file that are not '
#           'included in the second one:')
#     diff_file = first_set - second_set
#     print(diff_file)
#     print('Number of words: ', len(diff_file))
#     print()
#     print('Set words from the second file that are not'
#           ' included in the first one:')
#     diff_file2 = second_set - first_set
#     print(diff_file2)
#     print('Number of words: ', len(diff_file2))
#     print()
#     print('Shows a set of words that are included in either the \n '
#           'first or second file, but are not included in both \n'
#           'files at the same time:')
#     sym_diff_file = first_set ^ second_set
#     print(sym_diff_file)
#     print('Number of words: ', len(sym_diff_file))
#
#
# main()
# Task 7
def main():



main()
