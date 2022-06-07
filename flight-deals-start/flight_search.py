import requests

API_key = "6R0rKXobGojm8MTURko6tbxqj1LF0N2-"
kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{kiwi_endpoint}//locations/query"
        headers = {
            "apikey": API_key
        }
        Params = {
            "term": city_name, "location_types": "city"
        }
        response = requests.get(url=location_endpoint, params=Params, headers=headers)
        print(response)
        results = response.json()['locations']
        code = results[0]['code']
        return code
        print(response.text)





