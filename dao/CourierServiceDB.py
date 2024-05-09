from util.connectionutil.DBConnection import *


class CourierServiceDb:
    def __init__(self):
        self.connection = DBConnection.getConnection()

    @staticmethod
    def insert_order(self, courier_obj):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                query = "INSERT INTO Courier (SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, " \
                        "Status, TrackingNumber, DeliveryDate) " \
                        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                data = (courier_obj.sender_name, courier_obj.sender_address, courier_obj.receiver_name,
                        courier_obj.receiver_address, courier_obj.weight, courier_obj.status,
                        courier_obj.tracking_number, courier_obj.delivery_date)
                cursor.execute(query, data)
                self.connection.commit()
                print("Order inserted successfully.")
                cursor.close()
                self.connection.close()
        except Exception as e:
            print("Error while inserting order:", e)

    @staticmethod
    def get_order_status(self, tracking_number):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                query = "SELECT Status FROM Courier WHERE TrackingNumber = %s"
                cursor.execute(query, (tracking_number,))
                result = cursor.fetchone()
                cursor.close()
                self.connection.close()
                if result:
                    return result[0]
                else:
                    return "Order not found"
        except Exception as e:
            print("Error while fetching order status:", e)
            return "Error"

    @staticmethod
    def cancel_order(self, tracking_number):
        try:
            if self.connection:
                cursor = self.connection.cursor()
                query = "UPDATE Courier SET Status = 'Cancelled' WHERE TrackingNumber = %s"
                cursor.execute(query, (tracking_number,))
                self.connection.commit()
                affected_rows = cursor.rowcount
                cursor.close()
                self.connection.close()
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


