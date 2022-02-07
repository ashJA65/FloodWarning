from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def s0(stations,N):
    list0 = []
    stations = build_station_list()
    
    for i in stations:
        list0.append(i,N)
 
    list0.sort(key=lambda y: y[1])
    return list0

if __name__ == "__main__":
    print("*** Task 1E: rivers by number of stations ***")

