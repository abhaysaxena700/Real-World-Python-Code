# A class in Python is like a blueprint for creating objects. Each object is an instance of a class with its own properties (data) and methods (functions).
# __init__ method:a special method that runs when you create an object. It initializes object data.

# Define a simple class
class Vehicle:
    def __init__(self, vehicle_id, vendor_name, gps_status):
        self.vehicle_id = vehicle_id
        self.vendor_name = vendor_name
        self.gps_status = gps_status

    def display_status(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vendor: {self.vendor_name}")
        print(f"GPS Status: {self.gps_status}")

# Create objects (vehicles)
v1 = Vehicle("DL01AB1234", "Vendor_A", "Active")
v2 = Vehicle("MH05XY9876", "Vendor_B", "Inactive")

# Display status
v1.display_status()
v2.display_status()
