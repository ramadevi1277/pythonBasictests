import json

def create_json_file(data):
    with open("C:/Users/rcheepurupalli/PycharmProjects/pythonBasictests/test.json", "w") as f:
        json.dump(data, f, indent=4)


def reading_data_from_json():
    with open("C:/Users/rcheepurupalli/PycharmProjects/pythonBasictests/test.json") as json_file:
        json_data = json.load(json_file)
        for i in json_data["users"]:
            print ("username is %s and password is %s" % (i["user_name"], i["pwd"]))


if __name__ == "__main__":
    data = {"users":
        [
            {
                "user_name": "rama",
                "pwd": "gsdlgds",
            },
            {
                "user_name": "devi",
                "pwd": "gskjgdsjgsd",

            },
            {
                "user_name": "chvs",
                "pwd": "gsgdsgd",
            }

        ]
    }
    create_json_file(data)
    reading_data_from_json()