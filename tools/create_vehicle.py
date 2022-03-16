import requests


URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "color": "gray",
    "license_type": "Type1",
    "v_type": "bicycle"
}


def create_vehicle():
    color = input("Enter a color: ")
    license_type = input("Enter a license type: ")
    vehicle_type = input("Enter a vehicle type: ")
    SAMPLE_VEHICLE["color"] = color
    SAMPLE_VEHICLE["license_type"] = license_type
    SAMPLE_VEHICLE["v_type"] = vehicle_type
    response = requests.post(URL, json=SAMPLE_VEHICLE)
    if response.status_code == 204:
        print("Vehicle create.")
    else:
        print("Error")


if __name__ == "__main__":
    print("CREATE VEHICLE")
    print("------------")
    create_vehicle()
