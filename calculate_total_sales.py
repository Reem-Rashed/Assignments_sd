# this program calculate total sales
def calculate_total_sales(book_price, quantity_sold):
    total_sales = book_price * quantity_sold
    # multiplication book price *quantity
    return total_sales


# return totale sales
print("Welcome to the Bookstore Sales Calculator!")  # welcome to the user
price = float(
    input("Enter the price of a single book: ")
)  # Input the price of a single book
quantity = int(
    input("Enter the number of books sold: ")
)  # Input the number of books sold
total = calculate_total_sales(
    price, quantity
)  # Call the function to calculate total sales
print(f"Total sales for today: ${total:.2f}")  # Display the total sales amount