from abc import ABC, abstractmethod
from dao import CourierUserServiceImpl


class ICourierAdminService(ABC):
    @abstractmethod
    def add_courier_staff(self, name, contact_number):
        pass

    @abstractmethod
    def update_employee(employee_id, role):
        pass

    @abstractmethod
    def delete_employee(employee_id):
        pass
