# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from haversine import haversine


from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):

    outputList =[] #will append results into this
    distance = 0 #working distance variable

    for i in stations:
        distance = haversine(i.coord,p) 
        outputList.append((i,distance))
    
    #todo: sort list by distance

    return outputList