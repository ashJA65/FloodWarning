
from floodsystem.flood  import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels

import datetime

def run():
    #create stations
    stations = build_station_list()

    #get data
    update_water_levels(stations)

    #get 5 highest water level stations over the past 5 days
    highest_stations = stations_highest_rel_level(stations, 5)

    for station in highest_stations:
        
        dt = 10
        #get data from past 10 days
        
        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            plot_water_levels(station, dates, levels)
            print("Relative water level of " + station.name + ": " + str(station.relative_water_level()))
        except IndexError:
            print("{} station level data missing, skipping...".format(station.name))
            continue
        

if __name__ == "__main__":
    print("*** Task 2E: plot water level  ***")
    run()