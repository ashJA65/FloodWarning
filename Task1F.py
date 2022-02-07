from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    #obtain stations
    stations = build_station_list()

    #obtain inconsistent stations
    inconsistentStations=inconsistent_typical_range_stations(stations)

    #isolate station names into a seperate list
    inconsistentStationNames = [i.name for i in inconsistentStations]

    #sort list of names alphabetically
    inconsistentStationNames.sort()

    print(inconsistentStationNames)

if __name__ == "__main__":
    run()