print('Давайте заполним телефонный справочник')

def contact_input():
    book=[]
   
    while True:
        while True:
            for i in range(1,1000):
                str1=str(i)
                my_contact_name=input('Введите фамилию абонента: ')
                my_contact_surname=input('Введите имя абонента: ')
                my_contact_phone=input('Введите телефон: ')
                my_contact_info=input('Введите описание: ')

                contact=[str1, my_contact_name, my_contact_surname,my_contact_phone, my_contact_info]
                contact1=' * '.join(contact)
        
                print('хотите ввести еще? введите "да" или "нет": ')
                answer=input()

                if answer=='да':
                    book.append(contact1)
                    
                    continue
                elif answer=='нет':
                    book.append(contact1)
                    
                    break
            # return book
            book='\n'.join(book)
            return book+'\n'
    with open ('contact.txt', 'a', encoding='UTF-8' ) as file1:
        file1.write(book +'\n')
      

book2=contact_input()
print(book2)

with open ('contact.txt', 'a', encoding='UTF-8' ) as file1:
    file1.write(book2)