import requests

sheety_endpoint = "https://api.sheety.co/1b804a7375398b54f22f199adbfa614d/copyOfFlightDeals/prices"
class DataManager:

    def __init(self):
        self.destination_data = {}

    def get_destination_data(self):
        data = requests.get(url=sheety_endpoint)
        sheet_data = data.json()
        self.destination_data = sheet_data['prices']
        return self.destination_data


    def update_get_destination_data(self):
        for city in self.destination_data:

            new_data = {
                "price":{
                    "iataCode": city["iataCode"]
                }

            }
            response = requests.put(url=f"{sheety_endpoint}/{city['id']}", json=new_data)
            print(response.text)





