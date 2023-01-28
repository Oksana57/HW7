# import creat_contact1
# import csv_creater
import import_book
import model


alist=import_book.import_book
contact1=import_book.import_book

def work_book():
    model.prompt()
    u=model.user_input()
    if u==1:
        import_book.viewing_book()
    elif u==5:
        import_book.find_contact()
    elif u==3:
        # import_book.user_number()
        import_book.import_book()
        import_book.del_contact()

work_book()
