# self represents the instance of the class. It is used to access variables and methods associated with a particular object.

class Vehicle:
    def __init__(self, vehicle_id, vendor_name, gps_status):
        self.vehicle_id = vehicle_id
        self.vendor_name = vendor_name
        self.gps_status = gps_status

    def show_status(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vendor: {self.vendor_name}")
        print(f"GPS Status: {self.gps_status}")

vehicle1 = Vehicle("MH12AB1234", "Vendor A", "Active")
vehicle2 = Vehicle("MH14CD5678", "Vendor B", "Inactive")

vehicle1.show_status()
vehicle2.show_status()