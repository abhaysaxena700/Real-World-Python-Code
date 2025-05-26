# Step 1: Create a base class
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type

    def display_info(self):
        print("Vehicle ID:", self.vehicle_id)
        print("Vehicle Type:", self.vehicle_type)

# Step 2: Create a subclass that inherits from Vehicle
class TrackedVehicle(Vehicle):
    def __init__(self, vehicle_id, vehicle_type, gps_status, vendor_name):
        # Inherit vehicle_id and vehicle_type from the base class
        super().__init__(vehicle_id, vehicle_type)
        
        # Add new attributes specific to tracked vehicles
        self.gps_status = gps_status
        self.vendor_name = vendor_name

    def display_info(self):
        # Override display_info to show extended info
        super().display_info()
        print("GPS Status:", self.gps_status)
        print("Vendor Name:", self.vendor_name)
# Step 3: Create an object of TrackedVehicle and display info
v1 = TrackedVehicle("OD02AB0191", "Tanker", "Working", "MD Logistics")
v1.display_info()
