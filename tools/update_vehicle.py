import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "color": "gray",
    "license_type": "Type1",
    "v_type": "bicycle"
}


def update_vehicle(vehicleId):
    SAMPLE_VEHICLE["color"] = input("Enter a color: ")
    SAMPLE_VEHICLE["license_type"] = input("Enter a license type: ")
    SAMPLE_VEHICLE["v_type"] = input("Enter a vehicle type: ")
    url = "%s%s" % (URL, vehicleId)
    response = requests.put(url, json=SAMPLE_VEHICLE)
    if response.status_code == 204:
        print("Vehiccle updated")
    else:
        print("Error")


def get_vehicle():
    vehicleId = input("Type in the desired vehicle id: ")
    url = "%s%s" % (URL, vehicleId)
    response = requests.get(url)
    vehicle = {}
    if response.status_code == 200:
        response_json = response.json()
        vehicle = response_json["vehicle"][0]
        print("Vehicle: ")
        pprint(vehicle)
    else:
        print("Errors while trying to retrieve vehicle")
    return vehicle.get("id")


if __name__ == "__main__":
    print("UPDATE VEHICLE")
    print("---------")
    vehicleId = get_vehicle()
    update_vehicle(vehicleId)
