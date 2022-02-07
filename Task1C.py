from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()

    cambridge = (52.2053, 0.1218)

    camStations=stations_within_radius(stations,cambridge,10)
    stationNames=[ i.name for i in camStations]
    print(stationNames)

if __name__ == "__main__":
    run()