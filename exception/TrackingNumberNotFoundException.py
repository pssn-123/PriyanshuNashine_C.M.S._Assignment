class TrackingNumberNotFoundException(Exception):
    def __init__(self, msg = 'Tracking number not found '):
        self.msg = msg
        super().__init__(self.msg)

try:
    pass
except TrackingNumberNotFoundException as e:
    print(e)


