class Employee:
    def __init__(self, employeename, email, contactnumber, role, salary):
        self.__employeeName = employeename
        self.__email = email
        self.__contactNumber = contactnumber
        self.__role = role
        self.__salary = salary

    # setters
    def set_employeeid(self,employeeid):
        self.__employeeID = employeeid

    def set_employeename(self, employeename):
        self.__employeeName = employeename

    def set_email(self, email):
        self.__email = email

    def set_contactnmber(self, contactnumber):
        self.__contactNumber = contactnumber

    def set_role(self, role):
        self.__role = role

    def set_salary(self, salary):
        self.__salary = salary

    # getters
    def get_employeeid(self):
        return self.__employeeID

    def get_employeename(self):
        return self.__employeeName

    def get_email(self):
        return self.__email

    def get_contactnumber(self):
        return self.__contactNumber

    def get_role(self):
        return  self.__role

    def get_salary(self):
        return self.__salary

    # def toString(self):