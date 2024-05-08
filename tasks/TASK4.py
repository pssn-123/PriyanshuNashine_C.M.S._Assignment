"""
9. Parcel Tracking: Create a program that allows users to input a parcel tracking number.Store the
tracking number and Status in 2d String Array. Initialize the array with values. Then, simulate the
tracking process by displaying messages like "Parcel in transit," "Parcel out for delivery," or "Parcel
delivered" based on the tracking number's status.
"""
class ParcelTrackingSystem:
    def __init__(self):
        self.tracking_records = []

    def track_parcel(self, tracking_number):
        for record in self.tracking_records:
            if record[0] == tracking_number:
                print(f"Tracking number: {tracking_number}, Status: {record[1]}")
                return
        print("Tracking number not found.")

    def update_status(self, tracking_number, status):
        for record in self.tracking_records:
            if record[0] == tracking_number:
                record[1] = status
                print(f"Status updated for tracking number {tracking_number}")
                return
        print("Tracking number not found. Unable to update status.")

    def display_all_records(self):
        print("All parcel tracking records:")
        for record in self.tracking_records:
            print(f"Tracking number: {record[0]}, Status: {record[1]}")

# Example usage:
tracking_system = ParcelTrackingSystem()
tracking_system.tracking_records = [['ABC123', 'In transit'], ['XYZ789', 'Out for delivery']]
tracking_system.track_parcel('ABC123')  # Output: Tracking number: ABC123, Status: In transit
tracking_system.update_status('XYZ789', 'Delivered')  # Output: Status updated for tracking number XYZ789
tracking_system.display_all_records()
# Output:
# All parcel tracking records:
# Tracking number: ABC123, Status: In transit
# Tracking number: XYZ789, Status: Delivered


"""
10. Customer Data Validation: Write a function which takes 2 parameters, data-denotes the data and
detail-denotes if it is name addtress or phone number.Validate customer information based on
following critirea. Ensure that names contain only letters and are properly capitalized, addresses do not
contain special characters, and phone numbers follow a specific format (e.g., ###-###-####). 
"""


def validate_customer_info(name, address, phone_number):
    if not name.replace(" ", "").isalpha():
        return False, "Name should contain only letters."

    if not address.replace(" ", "").isalnum():
        return False, "Address should not contain special characters."

    if not (phone_number[3] == '-' and phone_number[7] == '-' and phone_number[:3].isdigit() and phone_number[4:7].isdigit() and phone_number[8:].isdigit()):
        return False, "Invalid phone number format. Should be ###-###-####."

    return True, "Customer information is valid."


# Example usage:
name = "John Doe"
address = "123 Main St"
phone_number = "123-456-7890"
is_valid, message = validate_customer_info(name, address, phone_number)
print(message)  # Output: Customer information is valid.

"""
11. Address Formatting: Develop a function that takes an address as input (street, city, state, zip code)
and formats it correctly, including capitalizing the first letter of each word and properly formatting the
zip code. 
"""

def format_address(street, city, state, zip_code):
    formatted_address = f"{street.title()}, {city.title()}, {state.upper()} {zip_code}"
    return formatted_address

# Example usage:
street = "123 main st"
city = "cityville"
state = "ny"
zip_code = "12345"
formatted_address = format_address(street, city, state, zip_code)
print("Formatted address:", formatted_address)  # Output: Formatted address: 123 Main St, Cityville, NY 12345

"""
12. Order Confirmation Email: Create a program that generates an order confirmation email. The email
should include details such as the customer's name, order number, delivery address, and expected
delivery date. 
"""

class OrderConfirmationEmail:
    @staticmethod
    def send_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date):
        print("Sending order confirmation email...")
        print(f"To: {customer_name}")
        print(f"Subject: Order Confirmation - #{order_number}")
        print(f"Dear {customer_name},\nYour order #{order_number} has been confirmed.")
        print(f"Delivery Address: {delivery_address}")
        print(f"Expected Delivery Date: {expected_delivery_date}")
        print("Thank you for choosing our service!")


"""
13. Calculate Shipping Costs: Develop a function that calculates the shipping cost based on the distance
between two locations and the weight of the parcel. You can use string inputs for the source and
destination addresses. 
"""

def calculate_shipping_cost(source_address, destination_address, weight):
    # Simulated calculation based on distance and weight
    distance = 10  # Placeholder for distance calculation
    shipping_cost = distance * weight  # Placeholder for shipping cost calculation
    return shipping_cost

# Example usage:
source_address = "123 Main St, City A, State A, 12345"
destination_address = "456 Elm St, City B, State B, 67890"
weight = 5  # in kg
cost = calculate_shipping_cost(source_address, destination_address, weight)
print("Shipping cost:", cost)

"""
14. Password Generator: Create a function that generates secure passwords for courier system
accounts. Ensure the passwords contain a mix of uppercase letters, lowercase letters, numbers, and
special characters
"""
import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

# Example usage:
password = generate_password()
print("Generated password:", password)

"""
15. Find Similar Addresses: Implement a function that finds similar addresses in the system. This can be
useful for identifying duplicate customer entries or optimizing delivery routes.Use string functions to
implement this. 
"""

def find_similar_addresses(address, address_list):
    similar_addresses = []
    for addr in address_list:
        if address.lower() in addr.lower() or addr.lower() in address.lower():
            similar_addresses.append(addr)
    return similar_addresses

# Example usage:
address_list = ["123 Main St", "456 Elm St", "789 Oak St", "Main St 123"]
address = "Main St"
similar_addresses = find_similar_addresses(address, address_list)
print("Similar addresses:", similar_addresses)

