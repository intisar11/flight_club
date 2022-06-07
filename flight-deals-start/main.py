from data_manager import DataManager

dataManager = DataManager()
sheets_data = dataManager.get_destination_data()


if sheets_data[0]['iataCode'] == "":
    from flight_search import FlightSearch
    flightsearch = FlightSearch()
    for row in sheets_data:
        row['iataCode'] = flightsearch.get_destination_code(row["city"])
    print(f"Sheet Data:\n{sheets_data}")

    dataManager.destination_data = sheets_data
    dataManager.update_get_destination_data()






