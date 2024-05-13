from abc import ABC, abstractmethod
from dao import CourierUserServiceImpl,CourierAdminService


class ICourierAdminService(ABC):
    @abstractmethod
    def add_courier_staff(self, name, contact_number):
        pass
