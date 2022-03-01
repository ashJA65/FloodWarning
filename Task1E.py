import py
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number
import floodsystem.datafetcher

def run():
    
    stations = build_station_list()
    print("\n"+str(rivers_by_station_number(stations,10))+"\n")
    

if __name__ == "__main__":
    print("*** Task 1E: rivers by number of stations ***")
run()

