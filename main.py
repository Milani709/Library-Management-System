from functions import (
    add_book,
    display_books,
    search_book,
    register_student,
    issue_book,
    return_book,
    display_issued,
    delete_book
)
def main():
    while True:
        print("---Library Menu-----")
        print("1.Add Book")
        print("2.display all book") 
        print("3.search book ")
        print("4.register student") 
        print("5.Issuse book ")
        print("6.return book") 
        print("7.issued list ")
        print("8.delete book" )
        print("9.Exit")                   
        user = input("Enter choice (1-9):")
        if user == "1":
             add_book()
        elif user =="2":
           display_books() 
        elif user == "3":
            search_book() 
        elif user == "4":
           register_student()
        elif user == "5":
           issue_book()  
        elif user == "6":
            return_book()
        elif user =="7":
            display_issued()    
        elif user == "8":
           delete_book()
        elif user == "9": 
           print("Thank you for visiting")
           break
        else:
            print("Invalid choices")
        
           
main()            