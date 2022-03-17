import requests


URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "color": "gray",
    "license_plate": "Type1",
    "v_type": "1",
    "user_id": "1"
}


def create_vehicle():
    color = input("Enter a color: ")
    license_plate = input("Enter a license_plate: ")
    v_type = input("Enter a vehicle type: ")
    user_id = input("Enter a user_id: ")
    SAMPLE_VEHICLE["color"] = color
    SAMPLE_VEHICLE["license_plate"] = license_plate
    SAMPLE_VEHICLE["v_type"] = v_type
    SAMPLE_VEHICLE["user_id"] = user_id
    response = requests.post(URL, json=SAMPLE_VEHICLE)
    if response.status_code == 204:
        print("Vehicle create.")
    else:
        print("Error")


if __name__ == "__main__":
    print("CREATE VEHICLE")
    print("------------")
    create_vehicle()
