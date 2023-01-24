import csv
import sys

# reader_object=csv.reader(file, delimiter=",")
alist=[]
contact1=[]
line1=''
def import_book():
    with open('data.csv', encoding='UTF-8') as n_file:
        reader_object=csv.reader(n_file, delimiter="*")
        count=0
        n=csv.field_size_limit(sys.maxsize)
        for row in reader_object:
            if count==0:
                alist = ' '.join(row).split()
                   
                # print(f'Справочник содержит столбцы: {"| ".join(row)}')
            elif 0<count<n:
                # line1=','.join(row).split()
                # line1=str(line1)
                # key=row[2]
                # line1=line1[0] + "," + line1[3:4]


                # contact1=' '.join(row).split()
                contact1.append(row)               
            count+=1
            if count==n:
                break
        return alist, contact1
        # contact1



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


alist, _=import_book()
# _, line1=import_book()
_, contact1=import_book()
# print(dict_book(key_of_book(contact1), means_of_book(contact1)))            
# print(import_book()) 
# print(alist)   
# print(line1)
# print(contact1)
# print(contact1[3][2])
key1=key_of_book(contact1)
means1=means_of_book(contact1)
print(dict_book(key1, means1))