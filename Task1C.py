from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()
    
    #Cambridge coordinate
    cambridge = (52.2053, 0.1218)

    #Find stations within 10km of coordinate
    camStations=stations_within_radius(stations,cambridge,10) 
    
    #for each Station object in camStations, pick out the name and add it to a list
    camStationsNames = [i.name for i in camStations]

    #Sort list alphabetically
    camStationsNames.sort() 

    print(camStationsNames)

if __name__ == "__main__":
    run()