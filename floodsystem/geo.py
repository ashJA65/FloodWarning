# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine
from pandas import RangeIndex

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
    s.append(station.river)# adds each of the river names to the list a for every station
  a = set(s)# converts s into the list a
  return(a)# sends a list back to the line that called this function in this case s from Task1d
    
def stations_by_river(stations):
  a = []# instanciate a new list variable with its value(s) set to null
  b = []# instanciate a new list variable with its value(s) set to null
  c = []# instanciate a new list variable with its value(s) set to null

  for station in stations:#this loops through the stations list for refrence each station its a container with its own variables
    if(station.river == "River Aire"):#check to see if the river name is equvalent to "River Aire"
      a.append(station.name)# adds each of the stations names to the list a if the if statement condition is true
  a.sort()#sorts out the list in an alphabetical order

  for station in stations:#this loops through the stations list for refrence each station its a container with its own variables      
    if(station.river == "River Cam"):#check to see if the river name is equvalent to "River Cam"
      b.append(station.name)# adds each of the stations names to the list b if the if statement condition is true
  b.sort()#sorts out the list in an alphabetical order

  for station in stations:#this loops through the stations list, for refrence each station is a container with its own variables      
    if(station.river == "River Thames"):#check to see if the river name is equvalent to "River Thames"
      c.append(station.name)# adds each of the stations names to the list c if the if statement condition is true
  c.sort()#sorts out the list in an alphabetical order

  return (a,b,c)# sends a list of list back to the line that called this function in this case t from Task1d


def stations_within_radius(stations, centre, r):
    """Take list of stations, coordintate tuple and radius and return a list of all stations within that circle"""

    stationsInCircle=[] # blank list to append in to

    for i in stations:

        if haversine(i.coord,centre) < r: # calculate distance from station to centre of circle

            stationsInCircle.append(i)  # append station into output list if it is within the circle

    return stationsInCircle

def rivers_by_station_number(stations, N):
    "Function that returns a list of tuples containing the river name and the number of stations it has"
    
    s0 = {}
    riverlist = []
    n = 0
        
    for station in stations:
        riverlist.append(station.river)

    for i in RangeIndex(len(riverlist)):
        n = 0
        current_river = ""
        for river in riverlist:
            if river == riverlist[i]:
                current_river = river
                n = n + 1
        if n >= 1:
            s0[current_river] = n

    print(s0)
    sorted_values = sorted(s0.values())
    sorted_s0 = {}

    #sort s0 in value order and return the N highest vales as a list
