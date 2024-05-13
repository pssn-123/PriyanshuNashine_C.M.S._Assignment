class Courier:

    # parameterized constructor
    def __init__(self, userid, sendername, senderaddress, receivername, receiveraddress, weight, status, trackingnumber, deliverydate):
        self.__userID = userid
        self.__senderName = sendername
        self.__senderAddress = senderaddress
        self.__receiverName = receivername
        self.__receiverAddress = receiveraddress
        self.__weight = weight
        self.__status = status
        self.__tarckingNumber = trackingnumber
        self.__deliveryDate = deliverydate


    # setters
    def set_courierid(self,courierid):
        self.__courierID = courierid

    def set_sendername(self, sendername):
        self.__senderName = sendername

    def set_senderaddress(self, senderaddress):
        self.__senderAddress = senderaddress

    def set_receivername(self, receivername):
        self.__receiverName = receivername

    def set_receiveraddress(self, receiveraddress):
        self.__receiverAddress = receiveraddress

    def set_weight(self, weight):
        self.__weight = weight

    def set_status(self,status):
        self.__status = status

    def set_trackingnumber(self, trackingnumber):
        self.__tarckingNumber = trackingnumber

    def set_deliverydate(self, deliverydate):
        self.__deliveryDate = deliverydate

    def set_userid(self, userid):
        self.__userID = userid

    # getters
    def get_courierid(self):
        return self.__courierID

    def get_sendername(self):
        return self.__senderName

    def get_senderaddress(self):
        return self.__senderAddress

    def get_receivername(self):
        return self.__receiverName

    def get_receiveraddress(self):
        return self.__receiverAddress

    def get_weight(self):
        return self.__weight

    def get_status(self):
        return self.__status

    def get_trackingnumber(self):
        return self.__tarckingNumber

    def get_deliverydate(self):
        return self.__deliveryDate

    def get_userid(self):
        return self.__userID

'''
    # default constructor
    def __init__(self):
        self.__courierID = ''
        self.__senderName = ''
        self.__senderAddress = ''
        self.__receiverName = ''
        self.__receiverAddress = ''
        self.__weight = ''
        self.__status = ''
        self.__tarckingNumber = ''
        self.__deliveryDate = ''
        self.__userID = ''
'''
