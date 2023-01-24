# import creat_contact  
# from creat_contact    куегктimport contact_input
# from user import book_veiw
import csv
from creat_contact1  import contact_input

book2=contact_input()
def export(book2):
    csv_columns = ['name', 'surname', 'phone', 'info']
    dict=book2
    csv_file='data.csv'
    try:
        with open(csv_file, 'a') as file_c:
            writer=csv.DictWriter(file_c, fieldnames=csv_columns, delimiter="*")
            writer.writeheader()
            for data in dict:
                writer.writerow(data)
    except IOError:
        print('I/O error')  
    return


export(book2)      