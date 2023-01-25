import import_book
import csv

import sys

key_of_book=import_book.key_of_book

means_of_book=import_book.means_of_book

book1=import_book.dict_book
contact1=import_book.import_book
alist=import_book.import_book

def prompt():
    print('Что вы хотите делать со справочником? ')
    n=int(input('Посмотреть - напишите 1\n Дополнить - напишите 2\n Удалить запись - напишите 3\n Заменить - напишите 4\n Найти - нпишите 5\n'))
    return n


def find_contact():
    number=input('Введите номер телефона для поиска')
    # if number in import_book.import_book:
    for i in book1:
        for j in i:
            if number in book1[i]:
                return 'Такой номер есть'
            else:
                return 'Такого номера нет'
   

def del_contact(number):
    with open('data.csv', 'r', encoding='UTF-8') as file1:

        for row in csv.reader(file1):
            if row[2] != number:
                with open('data.csv', 'w', encoding='UTF-8') as file2:
                    writer=csv.DictWriter(file2, delimiter="*")
                    writer.writerow(row)
    return  

# prompt()

# def viewing_book():
    
#     print('|   ', ' | '.join(alist), '  |')
#     for i in range(len(contact1)):
#         for j in range(len(contact1[i])):
#             view1='--'.join(contact1[i])
#         # print('|', '|'.join(alist), '|')
#         print('|', view1, '|')
#     return

# viewing_book()

