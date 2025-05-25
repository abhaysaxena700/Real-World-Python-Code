# An object is an instance of a class. It bundles data (attributes) and functions (methods) that operate on that data.

# Step 1: Create a class
class Vehicle:
    def __init__(self, vehicle_id, number_plate, gps_status, vendor_name):
        self.vehicle_id = vehicle_id
        self.number_plate = number_plate
        self.gps_status = gps_status
        self.vendor_name = vendor_name

    def show_status(self):
        return f"Vehicle {self.number_plate} (ID: {self.vehicle_id}) - GPS: {self.gps_status}"
    

# Step 2: Create an object (a specific vehicle)
vehicle1 = Vehicle(vehicle_id=101, number_plate="UP32AB1234",  vendor_name="Tata Logistics",gps_status="Active")

# Step 3: Use object method
print(vehicle1.show_status())
