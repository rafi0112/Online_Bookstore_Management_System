from book import *
from customer import add_customer, list_customers
from order import *


def main():
    while True:
        print("\n  Online Bookstore Management System")
        print("1. Add a new book")
        print("2. list all books")
        print("3. Add a customer")
        print("4. List all customers")
        print("5. Place an order")
        print("6. List orders")
        print("7. Exit")

        option = input("Select an Option:  ")
        
        if option == "1":
            title= input("Book Title:  ")
            author= input("Book Author:  ")
            genre = input("Book Genre:  ")
            price = float(input("Book Price:  "))
            add_book(title, author, genre, price)
            print("Book added successfully")

        elif option == "2":
            books = list_books()
            print("\nBook inventory")
            for book in books:
                print(f"{book['title']} ___ {book['author']} ___ {book['price']} Tk")

        elif option == "3":
            name = input("Enter customer name:  ")
            email = input("Enter customer email:  ")
            phone = input("Enter customer phone:  ")
            add_customer(name, email, phone)
            print(" Customer added successfully!")

        elif option == "4":
            customers = list_customers()
            print("\n Customer List:")
            for customer in customers:
                print(f"{customer['name']} - {customer['email']}")

        elif option == "5":
                customer_name = input("Enter customer name:  ")
                book_title = input("Enter book title:  ")
                quantity = int(input("Enter quantity:  "))
                place_order(customer_name, book_title, quantity)
                print("Order placed successfully!")

        elif option == "6":
            orders = list_orders()
            print("\n  Order List:")
            for order in orders:
                print(f"{order['customer_name']} ___ {order['quantity']} ___ {order['book_title']}")

        elif option == "7":
            print("Exiting... Goodbye!")
            break

        else :
            print("invalid ! ")
    
if __name__ == "__main__":
    main()