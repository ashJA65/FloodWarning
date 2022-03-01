# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from pickle import TRUE
from haversine import haversine
from pandas import RangeIndex
from collections import Counter
from functools import reduce

from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    """Take list of stations and a coordinate tuple and sort them by proximity to said coordinate"""

    outputList =[] #will append results into this
    distance = 0 #working distance variable

    for i in stations:
        distance = haversine(i.coord,p) 
        outputList.append((i,distance))
    
    outputList.sort(key=lambda y: y[1]) # should sort list by the second item of the tuple
    #https://pythonguides.com/python-sort-list-of-tuples/

    return outputList
    
from sqlalchemy import null
from .utils import sorted_by_key  # noqa

def rivers_with_station(stations):
  """Function that returns a tuple containing stations with a certain river"""

  s = []# instanciate a new list variable with its value(s) set to null
  for station in stations:#this loops through the stations list for refrence each station its a container with its own variables
    s.append(station.river)# adds the name of the river to s
  a = set(s)# converts s into the list a
  return(a)# sends a list back to the line that called this function in this case s from Task1d
    
def stations_by_river(stations):
    """Returns a Python dict (dictionary) that maps river names (the ‘key’)
    to a list of stations on that given river."""

    # Create the dictionary of river->[station] to be returned
    ans = {}
    for station in stations:
        if (station.river not in ans):
            # Create a new list for a not existing river
            ans[station.river] = []
        ans[station.river].append(station.name)
        ans[station.river].sort()
    return ans




def stations_within_radius(stations, centre, r):
    """Take list of stations, coordintate tuple and radius and return a list of all stations within that circle"""

    stationsInCircle=[] # blank list to append in to

    for i in stations:

        if haversine(i.coord,centre) < r: # calculate distance from station to centre of circle

            stationsInCircle.append(i)  # append station into output list if it is within the circle

    return stationsInCircle

def rivers_by_station_number(stations, N):
    """Determines the N rivers with the greatest number of monitoring stations.
    It returns a list of (river name, number of stations) tuples,
    sorted by the number of stations.
    In the case that there are more rivers with the same number of stations as the N th entry,
    these rivers are included in the list."""

    # First, get a complete list of (river name, number of stations) tuples
    complete_list = []
    stations_on_river = stations_by_river(stations)
    for river in stations_on_river:
        complete_list.append((river, len(stations_on_river[river])))

    # Now sort it by numbers of stations in descending order
    complete_list = sorted_by_key(complete_list, 1, reverse=True)
    # The threshold value: the N-th greatest value
    threshold = complete_list[N - 1][1]
    greatest_N = []
    for river in complete_list:
        if river[1] >= threshold:
            greatest_N.append((river))
    return greatest_N