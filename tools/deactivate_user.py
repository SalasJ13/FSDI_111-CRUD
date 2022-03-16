import requests
from pprint import pprint


URL = "http://127.0.0.1:5000/users/"

SAMPLE_USER = {
    "first_name": "Jaz",
    "last_name": "Salas",
    "hobbies": "Read",
}


def get_user():
    user_id = input("Type in the desired user id: ")
    url = "%s%s" % (URL, user_id)
    response = requests.get(url)
    user = {}
    if response.status_code == 200:
        response_json = response.json()
        user = response_json["user"][0]
        print("User: ")
        pprint(user)
    else:
        print("Error while trying to retrieve user.")
    return user.get("id")


def deactivate_user(user_id):
    url = "%s%s" % (URL, user_id)
    response = requests.delete(url)
    if response.status_code == 200 or 204:
        print("User delete")
    else:
        print("Error")


if __name__ == "__main__":
    print("Delete User")
    print("---------")
    user_id = get_user()
    deactivate_user(user_id)
