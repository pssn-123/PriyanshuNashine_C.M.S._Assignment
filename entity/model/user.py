class User:

    # parameterized constructor
    def __init__(self, userid, username, email, password, contactnumber, address):
        self.__userID = userid
        self.__userName = username
        self.__email = email
        self.__password = password
        self.__contactNumber = contactnumber
        self.__address = address
        print("In default constructor")

    # setters
    def set_UserID(self, userid):
        self.__userID = userid

    def set_userName(self, username):
        self.__userName = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_contactNumber(self, contactnumber):
        self.__contactNumber = contactnumber

    def set_Address(self, address):
        self.__address = address

    # getters
    def get_UserID(self):
        print(self.__userID)

    def get_UserName(self):
        print(self.__userName)

    def get_email(self):
        print(self.__email)

    def get_password(self):
        print(self.__password)

    def get_contactNumber(self):
        print(self.__contactNumber)

    def get_address(self):
        print(self.__address)

    # def toString(self):


obj = User(101, "Amit", "Amit@xyz.com", "12345678", "832636363", 'Nagpur')
obj.set_email('email')
obj.get_email()