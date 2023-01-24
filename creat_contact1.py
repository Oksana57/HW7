import csv



print('Давайте заполним телефонный справочник')

def contact_input():
    book=[]
    # dict2={}
    while True:
        for i in range(1,1000):
        
            c_name=input('Введите фамилию абонента: ')
            c_surname=input('Введите имя абонента: ')
            c_phone=input('Введите телефон: ')
            c_info=input('Введите описание: ')
            # dict1={}
            key1=['name', 'surname', 'phone', 'info']

            contact=[c_name, c_surname, c_phone, c_info]
            dict1 = {key1[j]: contact[j] for j in range(len(key1))} 
           
            # contact1=' * '.join(contact)
            # dict2={}
            # dict2={i:dict1}
            book.append(dict1)
            print('хотите ввести еще? введите "да" или "нет": ')
            answer=input()

            if answer=='да':
                # dict2[i]=dict1
               
                continue
                # while True:
                #     dict2={i:dict1}
                
                #     continue
            elif answer=='нет':

        
                # dict2={i:dict1}
                break
        # return book
        
        return book



# book2=contact_input()
# print(book2)

# with open ('contact.txt', 'a', encoding='UTF-8' ) as file1:
#     file1.write(book2)
# def export(book2):
#     csv_columns = ['N','name', 'surname', 'phone', 'info']
#     dict=book2
#     csv_file='data.csv'
#     try:
#         with open(csv_file, 'w') as file_c:
#             writer=csv.DictWriter(file_c, fieldnames=csv_columns)
#             writer.writeheader()
#             for data in dict:
#                 writer.writerow(data)
#     except IOError:
#         print('I/O error') 

# export(book2)                   