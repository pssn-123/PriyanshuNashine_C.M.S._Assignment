"""
7. Create an array to store the tracking history of a parcel, where each entry represents a location
update.
"""
class Parcel:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        self.tracking_history = []

    def add_location_update(self, location):
        self.tracking_history.append(location)

    def display_tracking_history(self):
        print(f"Tracking history for parcel {self.tracking_number}:")
        for idx, location in enumerate(self.tracking_history, start=1):
            print(f"{idx}. {location}")


# Usage
parcel = Parcel("ABC123")
parcel.add_location_update("Warehouse")
parcel.add_location_update("In transit")
parcel.add_location_update("Out for delivery")
parcel.display_tracking_history()

