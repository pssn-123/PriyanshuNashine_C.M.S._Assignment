from dao.CourierServiceDB import *
from entity.model.Courier import *
from entity.model.Employee import *

class Main_module(CourierServiceDb):

    def login():
        print('Courier Management System Login')
        print("1. Customerr Login")
        print("2. Admin Login")

    def user_menu():

        print("Courier Management System Customer Login")
        print("Menu")
        print("1 Place a new Courier Order : ")
        print("2 Get Order Status : ")
        print("3 Cancel a Courier Order : ")
        print("4 Get Assigned Order : ")


    def admin_menu():
        print("Courier Management System Admin Login")
        print("1. Add an Employee ")
        print("2. Update an Employee")
        print("3. Delete an Employee")


    def main():
        courier_service = CourierServiceDb()
        while not input("Welcome \nEnter to Continue\n"):
            Main_module.login()
            choice = input('Enter the User type :\n')
            if choice == '1':
                while not input("Press Enter to Continue in User Menu\nPress any key to Exit to User Selection:\n"):
                    print("Couriers Table")
                    courier_service.show_couriers()
                    print("User Table")
                    courier_service.show_users()
                    Main_module.user_menu()
                    option = input("Enter the Operation number : \n")
                    if option == '1':
                        user_id = input("Insert your user id :")
                        sender_name = input("Insert Sender name :")
                        sender_address = input("Insert Sender address :")
                        receiver_name = input("Insert Receiver name :")
                        receiver_address = input("Insert receiver addresss :")
                        weight = input("Insert weight of the courier :")
                        status = input("Insert courier status :")
                        tracking_number = input("Insert tracking number :")
                        deliverydate = input("Insert delivery date :")

                        courier = Courier(user_id, sender_name,sender_address, receiver_name, receiver_address, weight, status, tracking_number, deliverydate)
                        courier_service.insert_order(courier)
                        if courier:
                            print("Order Placed successfully.")
                        else:
                            print("Failed to Place Order")


                    elif option == '2':
                        tracking_number = input("Insert tracking id of courier :")
                        get_status = courier_service.get_order_status(tracking_number)
                        print(get_status)

                    elif option == '3':
                        tracking_number = input("Insert tracking id to cancel the order:")
                        cancel_order = courier_service.cancel_order(tracking_number)

                    elif option == '4':
                        assigned_orders = courier_service.get_assigned_orders()


            if choice == '2':
                while not input("Press Enter to Continue in Admin Menu\nPress any key to Exit to User Selection"):
                    courier_service.show_employees()
                    Main_module.admin_menu()
                    option = input("Enter the Operation Number \n:")
                    if option == '1':
                        employee_name = input("Enter Employee Name :")
                        email = input("Enter E-mail ID :")
                        mobile_number = input("Enter Mobile No. :")
                        role = input("Enter Employee's Role :")
                        salary = input("Enter Employee's Salary :")
                        employee = Employee(employee_name, email, mobile_number, role, salary)

                    elif option == '2':
                        pass
                    elif option == '3':
                        pass



if __name__ == "__main__":
    Main_module.main()