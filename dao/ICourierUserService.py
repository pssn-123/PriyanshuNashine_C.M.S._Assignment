from abc import ABC, abstractmethod
from entity.model.Courier import *


class ICourierUserService(ABC):
    @abstractmethod
    def insert_order(self, courier:Courier)-> bool:
        pass

    @abstractmethod
    def get_order_status(self, tracking_number):
        pass

    @abstractmethod
    def cancel_order(self,tracking_number):
        pass

    @abstractmethod
    def get_assigned_orders(self, courier_staff_id):
        pass

