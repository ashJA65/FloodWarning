from .utils import sorted_by_key


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

def stations_highest_rel_level(stations, N):
    """
    Return a list of N stations
    Each station has the highest water level relative to the typical range.
    The list is sorted in descending order by relative level
    """

    stations_rel_level = [] #blank list to append to

    for station in stations:
        
        relative_level = station.relative_water_level()

        # only append if relative level is present
        if relative_level != None:
            stations_rel_level.append(station)

        stations_rel_level.sort(key=lambda x: x. relative_water_level() , reverse=True) #sort in descending order by rel water level
        flooded_stations = stations_rel_level[:N] # return N stations in list (cropping)

    return flooded_stations
