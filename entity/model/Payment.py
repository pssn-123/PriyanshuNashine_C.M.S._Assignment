class Payment:

    def __init__(self, paymentid, courierid, amount, paymentdate):
        self.__paymentId = paymentid
        self.__courierId = courierid
        self.__amount = amount
        self.__paymentDate = paymentdate

    # setters
    def set_paymentid(self, paymentid):
        self.__paymentId = paymentid

    def set_courierid(self, courierid):
        self.__courierId = courierid

    def set_amount(self, amount):
        self.__amount = amount

    def set_paymentdate(self, paymentdate):
        self.__paymentDate = paymentdate

    # getters
    def get_paymentid(self):
        return self.__paymentId

    def get_courierid(self):
        return  self.__courierId

    def get_amount(self):
        return  self.__amount

    def get_paymentdate(self):
        return  self.__paymentDate

    def toString(self):
        print()