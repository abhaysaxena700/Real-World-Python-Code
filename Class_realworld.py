#Update GPS status, check if the GPS is down, etc.

class Vehicle:
    def __init__(self, vehicle_id, vendor_name, gps_status):
        self.vehicle_id = vehicle_id
        self.vendor_name = vendor_name
        self.gps_status = gps_status

    def display_status(self):
        print(f"{self.vehicle_id} | {self.vendor_name} | GPS: {self.gps_status}")

    def is_gps_active(self):
        return self.gps_status.lower() == "active"

    def update_gps_status(self, new_status):
        self.gps_status = new_status


# Initial fleet
fleet = [
    Vehicle("OD02AB4321", "Vendor_Alpha", "Active"),
    Vehicle("JH01CD6789", "Vendor_Beta", "Inactive"),
    Vehicle("WB11EF1234", "Vendor_Gamma", "Active")
]

# Step 1: Check GPS status and update if needed
for v in fleet:
    v.display_status()
    if not v.is_gps_active():
        print("⚠️ GPS is DOWN! Notifying Vendor...")
        
        # Let's assume vendor fixed it, now update the status
        print("✅ Vendor has fixed the GPS. Updating status...")
        v.update_gps_status("Active")  # <-- method now used!
print("\n🔄 Rechecking all GPS statuses after updates:")
for v in fleet:
    v.display_status()

