import save_all_books
from datetime import datetime

def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book ["title"] == search_book:
            title = input("Enter New Book Title: ")
            author = input("Enter New Author Name: ")
            year = int(input("Enter New Publishing Year: "))
            price = int(input("Enter New Price: "))
            quantity = int(input("Enter New Quantity Number: "))

            book_last_update_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book["title"] = title
            book["author"] = author
            book["year"] = year
            book["price"] = price
            book["quantity"] = quantity
            book["bookLastUpdateAt"] = book_last_update_at

            save_all_books.save_all_books(all_books)
            print("Book Updated Successfully.")
            return all_books
        
    print("Book Not Found.")
