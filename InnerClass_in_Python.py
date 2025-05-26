class Vendor:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    class Vehicle:
        def __init__(self, vehicle_id, gps_status):
            self.vehicle_id = vehicle_id
            self.gps_status = gps_status

    # Method to add a new vehicle to the vendor's list
    def add_vehicle(self, vehicle_id, gps_status):
        # Create a Vehicle object using the inner Vehicle class
        v = self.Vehicle(vehicle_id, gps_status)
        # Append the vehicle object to the vehicles list
        self.vehicles.append(v)

    # Method to display all vehicles under this vendor
    def show_vehicles(self):
        # Print vendor's name
        print(f"Vendor: {self.name}")
        # Loop through each vehicle object in the vehicles list
        for v in self.vehicles:
            print(f"Vehicle ID: {v.vehicle_id}, GPS: {v.gps_status}")

# Create an object of the Vendor class & Add vehicles to this vendor
v1 = Vendor("Western Carriers")
v1.add_vehicle("OD02AB1234", "Active")
v1.add_vehicle("OD02AB5678", "Inactive")

# Display report
v1.show_vehicles()
