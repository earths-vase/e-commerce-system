from customer import Customer
from product import Product
from order import Order

def main():
    # Create customers
    customer1 = Customer(1, "Alice", "alice@example.com")
    customer2 = Customer(2, "Bob", "bob@example.com")

    # Create products
    laptop = Product(1, "Laptop", 999.99)
    smartphone = Product(2, "Smartphone", 499.99)

    # Create orders
    order1 = Order(101, customer1)
    order1.add_product(laptop)
    order1.add_product(smartphone)

    order2 = Order(102, customer2)
    order2.add_product(smartphone)

    # Display order information
    print("Order 1 Information:")
    order1.display_info()

    print("\nOrder 2 Information:")
    order2.display_info()

if __name__ == "__main__":
    main()
