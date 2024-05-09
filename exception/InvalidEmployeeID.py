class InvalidEmployeeID(Exception):
    def __init__(self, msg = 'The Entered EmployeeId id Invalid'):
        self.msg = msg
        super().__init__(self.msg)

try:

except InvalidEmployeeID as e:
    print(e)
