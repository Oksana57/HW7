import csv

# reader_object=csv.reader(file, delimiter=",")
alist=[]
contact1=[]
def import_book():
    with open('data.csv', encoding='UTF-8') as n_file:
        reader_object=csv.reader(n_file, delimiter="*")
        count=0
        for row in reader_object:
            if count==0:
                alist = ' '.join(row).split()
                   
                # print(f'Справочник содержит столбцы: {"| ".join(row)}')
            else:
                # contact1=[row[0], row[1], row[2], row[3], row[4]]
                # contact1=' '.join(row).split()
                contact1.append(row)
                # print(f'{row[0]} * {row[1]} * {row[2]} * {row[3]} * {row[4]}')   
            count+=1
        return alist, contact1

print(import_book())    
