class CourierCompany:

    # parameterized constructor
    def __init__(self, companyname):
        self.__companyName = companyname
        self.__courierDetails = []
        self.__employeeDetails = []
        self.__locationDetails = []

    # setters
    def set_courierId(self, courierId):
        self.__courierID = courierId

    def set_courierdetails(self, courierdetails):
        self.__courierDetails = courierdetails

    def set_employeedetails(self, employeedetails):
        self.__employeeDetails = employeedetails

    def set_locationdetails(self,locationdetails):
        self.__locationDetails = locationdetails

    # getters
    def get_courierId(self):
        return self.__courierID

    def get_courierdetails(self):
        return self.__courierDetails

    def get_employeedetaisl(self):
        return self.__employeeDetails

    def get_locationdetails(self):
        return self.__locationDetails

    # def toString():
