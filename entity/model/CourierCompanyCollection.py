class CourierCompanyCollection:
    def __init__(self, company_name):
        self.company_name = company_name
        self.courier_details = []
        self.employee_details = []
        self.location_details = []

    def add_courier(self, courier):
        self.courier_details.append(courier)

    def add_employee(self, employee):
        self.employee_details.append(employee)
