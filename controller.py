# import creat_contact1
# import csv_creater
import import_book
import model


alist=import_book.import_book
contact1=import_book.import_book

def work_book():
    model.prompt()
    if model.prompt()==1:
        import_book.viewing_book()
    elif model.prompt()==5:
        import_book.find_contact()
    elif model.prompt()==3:
        model.del_contact()

work_book()
