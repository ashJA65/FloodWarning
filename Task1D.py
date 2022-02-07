from floodsystem.geo import rivers_with_station #this refrences the function "rivers_with_station" from the .py path "\floodsystem.geo"
from floodsystem.geo import stations_by_river #this refrences the function "stations_by_river" from the .py path "\floodsystem.geo"
from floodsystem.stationdata import build_station_list #this refrences the function "build_station_list" from the .py path "\floodsystem.stationdata"

def run():
    stations = build_station_list()# Calls the function "build_station_list" and returns a list of stations of moritoringStation
    s = rivers_with_station(stations)# Calls the function "rivers_with_station"
    t = stations_by_river(stations)# Calls the function "stations_by_river"

    a = []# instanciate a new list variable with its value(s) set to null
    for i in range(10): #forloop function that runs 10 times as stated in the range
        a.append(list(sorted(s))[i])# For every loop(loops 10 times) this adds i from the s set var whiles converting it from a set to a list (where i is the number of loop etc(1/10))

    print(str(len(s)) + " stations. " + "First 10 - " + str(a))# converts both a(list) and s(set) into a string then calculates the length of s and finally displays it in the termainal 
    print(t)# Displays the list in the Terminal

if __name__ == "__main__":
    print("*** Task 1D: rivers with a station(s) ***")# Displays a title to the Terminal
run()# Calls the function above "run"