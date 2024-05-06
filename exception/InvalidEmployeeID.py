class InvalidEmployeeID(Exception):
    def __init__(self, msg):
        super().__init__(msg)

try:
    raise InvalidEmployeeID('Invalid EmployeeID: ')

except InvalidEmployeeID as e:
    print(e)
