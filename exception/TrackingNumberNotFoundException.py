class TrackingNumberNotFoundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

try:
    raise TrackingNumberNotFoundException("The tracking number does not exist")

except TrackingNumberNotFoundException as e:
    print(e)


