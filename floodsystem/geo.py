# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):

    outputList =[] #will append results into this
    distance = 0 #working distance variable

    for i in stations:
        distance = math.sqrt( (i.coord[0]-p[0])**2 + (i.coord[1]-p[1])**2 ) # perform pythag calculation on x and y distances from station to input cooord p
        outputList.append((i,distance))
    
    return outputList