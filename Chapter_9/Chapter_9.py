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
#     dct = {'James': 1, 'Jim': 2, 'STASEBAN': 3}
#     if delete_key in dct:
#         del dct[delete_key]
#         print(dct)
#     else:
#         print('Not found(')
#     if delete_key == 'STASEBAN':
#         print('Stas always EBAN')
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
def main():



main()
