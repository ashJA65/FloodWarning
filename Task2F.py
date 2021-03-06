from floodsystem.flood  import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels

import datetime


def run():
    #get station data
    stations = build_station_list()
    update_water_levels(stations)

    #get highest 5 stations
    highest_stations = stations_highest_rel_level(stations, 5)

    for station in highest_stations:
        dt = 2 # 2days
        degree = 4 #polynomial max degree
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        try:
                plot_water_level_with_fit(station, dates, levels, degree)
        except IndexError:
                print("{} station level data missing, skipping...".format(station.name))
                continue

if __name__ == "__main__":
    print("*** Task 2F function fitting ***")
    run()