class Vehicle:
    def __init__(self, vehicle_id, number_plate, gps_status, vendor_name):
        self.vehicle_id = vehicle_id
        self.number_plate = number_plate
        self.gps_status = gps_status
        self.vendor_name = vendor_name

    def show_status(self):
        return f"Vehicle {self.number_plate} (ID: {self.vehicle_id}) - GPS: {self.gps_status}"
vehicles = [
    Vehicle(101, "UP32AB1234", "Active", "Tata Logistics"),
    Vehicle(102, "DL01CD5678", "Inactive", "Mahindra Cargo"),
    Vehicle(103, "MH12EF9101", "Active", "Ashok Logistics"),
    Vehicle(104, "BR05GH2345", "Inactive", "Tata Logistics")
]

# Logic to check GPS status and flag vehicles
for v in vehicles:
    if v.gps_status == "Inactive":
        print(f"ALERT: GPS down for {v.number_plate} ({v.vendor_name})")
