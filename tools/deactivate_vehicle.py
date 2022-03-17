import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "color": "gray",
    "license_plate": "Type1",
    "v_type": "1",
    "user_id": "1"
}


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
        print("Error")
    return vehicle.get("id")


def deactivate_vehicle(vehicleId):
    url = "%s%s" % (URL, vehicleId)
    response = requests.delete(url)
    if response.status_code == 204:
        print("Vehicle delete")
    else:
        print("Error")


if __name__ == "__main__":
    print("DELETE VEHICLE")
    print("------")
    vehicleId = get_vehicle()
    deactivate_vehicle(vehicleId)
