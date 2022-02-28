def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples. Each tuple contains a station that has a water level over tol, and the water level of the station"""

    flooded_stations = [] #blank list to append to

    for station in stations:
        relative_level = station.relative_water_level()
        try:
            if relative_level > tol:
                flooded_stations.append((station.name, relative_level))
        except:
            pass
            #ignore errors and return a blank entry

    flooded_stations.sort(key=lambda x: x[1], reverse=True) # sort list by relative level in descending order
    return flooded_stations
