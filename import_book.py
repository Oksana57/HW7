import csv
import sys


def import_book():
    alist=[]
    contact1=[]
    with open('data.csv', encoding='UTF-8') as n_file:
        reader_object=csv.reader(n_file, delimiter="*")
        count=0
        n=csv.field_size_limit(sys.maxsize)
        for row in reader_object:
            if count==0:
                alist = ' '.join(row).split()
                  
            elif 0<count<n:
               
                contact1.append(row)               
            count+=1
            if count==n:
                break
        return alist, contact1

def key_of_book(contact1):
    key_of_book=[]
    for i in range(len(contact1)):
        for j in range(len(contact1[i])-3):
            key_of_book.append(contact1[i][2])
    return key_of_book

def means_of_book(contact1):
    means_of_book=[]
    for i in range(len(contact1)):
        for j in range(len(contact1[i])-3):
            n=contact1[i][0]           
            m=contact1[i][1]
            l=contact1[i][3]
            s=n + ', ' + m +', '+ l
            means_of_book.append(s)
    return means_of_book

def dict_book(key_of_book, means_of_book):
    book1=[]
    dict_book={}
    for k in range(len(key_of_book)):
        dict_book={key_of_book[k]: means_of_book[k]} 
        book1.append(dict_book)
    return book1     

alist, contact1=import_book()
# print(alist, contact1)

key1=key_of_book(contact1)
# print(key1)
means1=means_of_book(contact1)
# print(means1)
book1=dict_book(key1, means1)

# print(book1)

def viewing_book():
    print('|   ', ' | '.join(alist), '  |')
    for i in range(len(contact1)):
        for j in range(len(contact1[i])):
            view1='--'.join(contact1[i])
        # print('|', '|'.join(alist), '|')
        print('|', view1, '|')
    return

# viewing_book()

def find_contact():
    number=input('Введите номер телефона для поиска')
    # if number in import_book.import_book:
    for i in range(len(book1)):
        # for j in range(len(book1[i])):
        if number in book1[i]:
            return print('Такой номер есть')
        else:
            return print('Такого номера нет')
    return