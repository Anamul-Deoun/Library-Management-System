from save_all_books import save_all_books
import random
from datetime import datetime

def add_books(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    price = int(input("Enter Book Price: "))
    
    while True:
        try:
            year = int(input("Enter Publishing Year Number: "))
            break
        except ValueError:
            print("Invalid Input. Please Enter a Valid Integer.")

    while True:
        try:
            quantity = int(input("Enter Quantity Number: "))
            break
        except ValueError:
            print("Invalid Input. Please Enter a Valid Integer.")
            
    
    isbn = random.randint(10000, 99999)
    bookAddAt = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity,
        "bookAddAt": bookAddAt,
    }
    
    all_books.append(book)
    save_all_books(all_books)
    
    print("Books Added Successully")
    
    return all_books
    