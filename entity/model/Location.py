class Location:

    # default constructor
    def __init__(self, locationid, locationname, address):
        self.__locationId = locationid
        self.__locationName = locationname
        self.__address = address

    # setters
    def set_locationid(self,locationid):
        self.__locationId = locationid

    def set_locationname(self, locationname):
        self.__locationName = locationname

    def set_address(self, address):
        self.__address = address

    # getters
    def get_locationid(self):
        return self.__locationId

    def get_locationname(self):
        return self.__locationName

    def get_address(self):
        return self.__address

    # def toString():
