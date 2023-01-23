# import var1.creat_contact as creat_contact
from creat_contact import contact_input

book=contact_input()
def export_f(book):
    with open ('contact1.txt', 'a', encoding='UTF-8' ) as file1:
        file1.write(book+'\n')
    return 
export_f(book)       