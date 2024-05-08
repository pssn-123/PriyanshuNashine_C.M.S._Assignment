"""
5. Write a Python program that uses a for loop to display all the orders for a specific customer.
"""
class Customer:
    def __init__(self, name, orders):
        self.name = name
        self.orders = orders

    def display_orders(self):
        print(f"Orders for {self.name}:")
        for order in self.orders:
            print(f"Order ID: {order.order_id}, Status: {order.status}")


# Example usage:
class Order:
    def __init__(self, order_id, status):
        self.order_id = order_id
        self.status = status


orders = [Order(1, "Processing"), Order(2, "Delivered"), Order(3, "Cancelled")]
customer = Customer("John", orders)
customer.display_orders()

"""
6. Implement a while loop to track the real-time location of a courier until it reaches its destination. 
"""
class Courier:
    def __init__(self, name, current_location, destination):
        self.name = name
        self.current_location = current_location
        self.destination = destination

    def track_location(self):
        print(f"Tracking {self.name}...")
        while self.current_location != self.destination:
            print(f"Current location: {self.current_location}")
            # Simulate movement to the next location
            # In real implementation, update current_location based on GPS or other tracking mechanisms
            self.current_location = input("Enter new location: ")
        print("Courier reached the destination.")


# Example usage:
courier = Courier("Courier A", "Warehouse", "Customer's Address")
courier.track_location()
