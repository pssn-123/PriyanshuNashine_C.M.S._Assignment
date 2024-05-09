from dao import CourierUserServiceImpl
from dao.ICourierAdminService import *


class CourierAdminServiceCollectionImpl(CourierUserServiceImpl, ICourierAdminService):
    def __init__(self, company_obj):
        super().__init__(company_obj)

    def add_courier_staff(self, name, contact_number):
        # Logic to add courier staff
        new_employee_id = len(self.__company_obj.get_employeeDetails()) + 1
        new_employee = {"employeeID": new_employee_id, "name": name, "contactNumber": contact_number}
        self.__company_obj.get_employeeDetails().append(new_employee)
        return new_employee_id
