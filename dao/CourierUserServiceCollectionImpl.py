from dao.ICourierUserService import *


class CourierUserServiceCollectionImpl(ICourierUserService):
    def __init__(self, company_obj):
        self.company_obj = company_obj

    def place_order(self, courier_obj):
        self.company_obj.courier_details.append(courier_obj)
        print("Order placed successfully.")

    def get_order_status(self, tracking_number):
        for courier in self.company_obj.courier_details:
            if courier.tracking_number == tracking_number:
                return courier.status
        return "Order not found"

    def cancel_order(self, tracking_number):
        for courier in self.company_obj.courier_details:
            if courier.tracking_number == tracking_number:
                courier.status = "Cancelled"
                print("Order cancelled successfully.")
                return
        print("Order not found")

    def get_assigned_order(self, courier_staff_id):
        assigned_orders = []
        for courier in self.company_obj.courier_details:
            if courier.assigned_courier_staff_id == courier_staff_id:
                assigned_orders.append(courier)
        return assigned_orders
