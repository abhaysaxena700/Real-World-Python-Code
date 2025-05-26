# The class itself = Class Attributes (shared by all objects)
# A specific object = Instance Attributes (unique for each object)

class Vehicle:
    # Class Attribute
    gps_enabled = True

    def __init__(self, vehicle_id, vendor_name, location):
        # Instance Attributes
        self.vehicle_id = vehicle_id
        self.vendor_name = vendor_name
        self.location = location

    def display_info(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vendor: {self.vendor_name}")
        print(f"Current Location: {self.location}")
        print(f"GPS Enabled: {Vehicle.gps_enabled}")

vehicle1 = Vehicle("WB1234", "Tata Logistics", "Jamshedpur")
vehicle2 = Vehicle("BR5678", "DHL India", "Rourkela")

vehicle1.display_info()
print("-----")
vehicle2.display_info()