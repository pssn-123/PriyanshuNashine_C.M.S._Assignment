from util.connectionutil.DBConnection import *
from entity.model.Courier import *
from entity.model.Employee import *
from dao.ICourierUserService import *
from dao.ICourierAdminService import *
from exception.InvalidEmployeeID import *


class CourierServiceDb(ICourierUserService, Courier, ICourierAdminService, Employee):
    def __init__(self):
        self.connection = DBConnection.getConnection()

    @staticmethod
    def insert_order(courier: Courier) -> bool:
        try:
            connection = DBConnection.getConnection()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO Couriers (UserID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, " \
                        "Status, TrackingNumber, DeliveryDate) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                data = [courier.get_userid(), courier.get_sendername(), courier.get_senderaddress(),
                        courier.get_receivername(), courier.get_receiveraddress(), courier.get_weight(),
                        courier.get_status(), courier.get_trackingnumber(), courier.get_deliverydate()
                        ]
                cursor.execute(query, data)
                connection.commit()
                return True
                cursor.close()
                connection.close()
        except Exception as e:
            print("Error while inserting order:", e)
            return False

    @staticmethod
    def get_order_status(tracking_number):
        try:
            connection = DBConnection.getConnection()
            if connection:
                cursor = connection.cursor()
                query = "SELECT Status FROM Couriers WHERE TrackingNumber = %s"
                cursor.execute(query, (tracking_number,))
                result = cursor.fetchone()
                cursor.close()
                connection.close()
                if result:
                    return result[0]
                else:
                    return "Order not found"
        except Exception as e:
            print("Error while fetching order status:", e)
            return "Error"

    @staticmethod
    def cancel_order(tracking_number):
        connection = DBConnection.getConnection()
        try:
            if connection:
                cursor = connection.cursor()
                query = "UPDATE Couriers SET Status = 'Cancelled' WHERE TrackingNumber = %s"
                cursor.execute(query, (tracking_number,))
                connection.commit()
                affected_rows = cursor.rowcount
                cursor.close()
                connection.close()
                if affected_rows > 0:
                    print("Order cancelled successfully.")
                else:
                    print("Order not found.")
        except Exception as e:
            print("Error while cancelling order:", e)

    @staticmethod
    def get_assigned_orders(self, courier_staff_id):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                query = "SELECT * FROM Courier WHERE AssignedCourierStaffId = %s"
                cursor.execute(query, (courier_staff_id,))
                results = cursor.fetchall()
                cursor.close()
                self.connection.close()
                assigned_orders = []
                for row in results:
                    assigned_orders.append({
                        "TrackingNumber": row[7],
                        "SenderName": row[1],
                        "ReceiverName": row[3],
                        "Weight": row[5],
                        "Status": row[6]
                    })
                return assigned_orders
        except Exception as e:
            print("Error while fetching assigned orders:", e)
            return []

    @staticmethod
    def get_delivery_history(self, tracking_number):
        """Retrieve and display the delivery history of a specific parcel."""
        cursor = self.connection.cursor()
        try:
            # Execute SELECT query
            cursor.execute("SELECT * FROM delivery_history WHERE tracking_number = %s", (tracking_number,))
            delivery_history = cursor.fetchall()
            print("Delivery History:")
            for record in delivery_history:
                print(record)
            cursor.close()
        except Exception as e:
            print(f"Error retrieving delivery history: {e}")

    def show_couriers(self):
        cursor = self.connection.cursor()
        query = 'Select * from couriers'
        cursor.execute(query)
        couriers = cursor.fetchall()
        self.connection.commit()
        for courier in couriers:
            print(courier)

    def show_employees(self):
        cursor = self.connection.cursor()
        query = 'Select * from employee'
        cursor.execute(query)
        employees = cursor.fetchall()
        self.connection.commit()
        for employee in employees:
            print(employee)

    def show_users(self):
        cursor = self.connection.cursor()
        query = 'Select * from users'
        cursor.execute(query)
        users = cursor.fetchall()
        self.connection.commit()
        for user in users:
            print(user)

    def add_courier_staff(employee: Employee) -> bool:
        try:
            connection = DBConnection.getConnection()
            if connection:
                cursor = connection.cursor()
                query = "INSERT INTO Employee (Name, Email, ContactNumber, Role, Salary) VALUES (%s, %s, %s, %s, %s)"
                data = [employee.get_employeename(), employee.get_email(), employee.get_contactnumber(),
                        employee.get_role(), employee.get_salary()]
                cursor.execute(query, data)
                connection.commit()
                return True
                cursor.close()
                connection.close()
        except Exception as e:
            print('Error', e)
            return False

    def update_employee(employee_id, role):
        try:
            connection = DBConnection.getConnection()
            if connection:
                cursor = connection.cursor()
                query = 'Update Employee set Role = %s where employeeid = %s'
                cursor.execute(query, (role, employee_id,))
                connection.commit()
        except InvalidEmployeeID as e:
            print("Error :", e)

    def delete_employee(employee_id):
        try:
            connection = DBConnection.getConnection()
            if connection:
                cursor = connection.cursor()
                query = 'Delete from employee where employeeid = %s'
                cursor.execute( query, employee_id)
                cursor.commit()
                return True
        except InvalidEmployeeID as e:
            print("Error :", e)
            return False

