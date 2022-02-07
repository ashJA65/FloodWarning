from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def run():
    # Build list of stations
    stations = build_station_list()

    cambridge = (52.2053, 0.1218)
    
    #build sorted list of (station,dist) tuples
    distances = stations_by_distance(stations,cambridge)

    # print 10 closest stations
    for i in distances[:10]:
        print (i[0].name, i[0].town, i[1])

    # print 10 furthest stations
    for i in distances[-10:]:
        print ((i[0].name, i[0].town, i[1]))

if __name__ == "__main__":
    run()
    #testchnge