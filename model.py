import import_book
import csv

key_of_book=import_book.key_of_book

means_of_book=import_book.means_of_book
book1=import_book.dict_book(key_of_book, means_of_book)
def prompt(contact1):
   print('Что вы хотите делать со справочником? ')
   n=int(input('Посмотреть - напишите 1\n Дополнить - напишите 2\n Удалить запись - напишите 3\n заменить - напишите 4 '))



def find_contact(book1, number):
    key1=input('Введите номер телефона для поиска')
    for i in range(len(book1)):
        for j in range(len(book1[i])):
            if key1 in book1[i]:
                return 'Такой номер есть'
            else:
                return 'Такого номера нет'
    return  number         


def del_contact(number):
    with open('data.csv', 'r', encoding='UTF-8') as file1:
        for row in csv.reader(file1):
            if row[2] != number:
                with open('data.csv', 'w', encoding='UTF-8') as file2:
                    writer=csv.DictWriter(file2, delimiter="*")
                    writer.writerow(row)
    return  