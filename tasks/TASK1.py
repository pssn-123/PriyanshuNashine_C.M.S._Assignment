# task 1 Contorl Flow Statements

"""
1. Write a program that checks whether a given order is delivered or not based on its status (e.g.,
"Processing," "Delivered," "Cancelled"). Use if-else statements for this.
"""
order_status = 'delivered'
if order_status == 'delivered':
    print('The Order is Delivered')
else:
    print('The Order is not Delivered')

"""
2. Implement a switch-case statement to categorize parcels based on their weight into "Light,"
"Medium," or "Heavy."
"""

parcel_weight = 10.5
if 0 <= parcel_weight <= 2 :
    print('Parcel is light weighted')
elif 3 <= parcel_weight <= 5 :
    print('Parcel is medium weighted')
else:
    print('Parcel is heavy weighted')

"""
3. Implement User Authentication 1. Create a login system for employees and customers using Java
control flow statements.
"""
class AuthenticationSystem:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def Authenticate(self):

        valid_users = {
            'priyanshu': 'P$$N1234',
            'ajinkya': 'Aj2345Aj'
        }

        if self.username in valid_users and valid_users[self.username] == self.password:
            return True
        else:
            return False

username = input('Eneter your username : ')
password = input('Enter your password : ')
auth_sys = AuthenticationSystem(username, password)
if auth_sys.Authenticate():
    print('Login Successful')
else:
    print('Invalid Credentials')


"""
4. Implement Courier Assignment Logic 1. Develop a mechanism to assign couriers to shipments based
on predefined criteria (e.g., proximity, load capacity) using loops.
"""
class CourierAssignmentSystem:
    def __init__(self, orders, couriers):
        self.orders = orders
        self.couriers = couriers

    def assign_courier(self):
        for order in self.orders:
            for courier in self.couriers:
                if order.weight <= courier.load_capacity:
                    print(f"Courier {courier.name} assigned to order {order.order_id}")
                    break
            else:
                print(f"No courier available for order {order.order_id}")


# Example usage:
class Order:
    def __init__(self, order_id, weight):
        self.order_id = order_id
        self.weight = weight


class Courier:
    def __init__(self, name, load_capacity):
        self.name = name
        self.load_capacity = load_capacity


orders = [Order(1, 15), Order(2, 25), Order(3, 10)]
couriers = [Courier("Courier A", 20), Courier("Courier B", 30)]

assignment_system = CourierAssignmentSystem(orders, couriers)
assignment_system.assign_courier()
