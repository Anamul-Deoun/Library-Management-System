import add_books
import view_all_books
import restore_books
import update_book_file, delete_book_file

all_books = []

while True:
    print("Welcome to Library Management System!")
    print("1. Exit")
    print("2. Add Books")
    print("3. View All Books")
    print("4. Book Update")
    print("5. Book Delete")

    all_books = restore_books.restore_all_books(all_books)

    menu = input("Enter your choice (1-5): ")
    
    if menu == "1":
        print("Exiting the Library Management System. Goodbye!")
        break
    elif menu == "2":
        all_books = add_books.add_books(all_books)
    elif menu == "3":
        view_all_books.view_all_books(all_books)
    elif menu == "4":
        update_book_file.update_books(all_books)
    elif menu == "5":
        delete_book_file.delete_books(all_books)
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")