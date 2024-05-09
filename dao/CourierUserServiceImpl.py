from dao.ICourierUserService import *


class CourierUserServiceImpl(ICourierUserService):
    def __init__(self, company_obj):
        self.__company_obj = company_obj

    def place_order(self, courier_obj):
        self.__company_obj.get_courierDetails().append(courier_obj)
        print("Order placed successfully.")

    def get_order_status(self, tracking_number):
        # Logic to get order status
        for courier in self.__company_obj.get_courierDetails():
            if courier.get_trackingNumber() == tracking_number:
                return courier.get_status()
        return "Order not found"

    def cancel_order(self, tracking_number):
        # Logic to cancel an order
        for courier in self.__company_obj.get_courierDetails():
            if courier.get_trackingNumber() == tracking_number:
                courier.set_status("Cancelled")
                print("Order cancelled successfully.")
                return
        print("Order not found")

    def get_assigned_order(self, courier_staff_id):
        # Logic to get assigned orders for a staff member
        assigned_orders = []
        for courier in self.__company_obj.get_courierDetails():
            if courier.get_assignedCourierStaffId() == courier_staff_id:
                assigned_orders.append(courier)
        return assigned_orders
