# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import *


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    #dummy data with correct range
    assert MonitoringStation("1", "1", "sta1", (0., 1.), (1, 4), "River 1",
                                 "Town 1").typical_range_consistent() == True

    #test for missing data                             
    assert MonitoringStation("11", "1", "sta1", (0., 1.), None, "River 1",
                                 "Town 1").typical_range_consistent() == False

    #test for max value being less than min value
    assert MonitoringStation("1", "1", "sta1", (0., 1.), (1, -1), "River 1",
                                 "Town 1").typical_range_consistent() == False
    

def test_inconsistent_typical_range_stations():
    #dummy data with some faults
    station1 = MonitoringStation(station_id="sta1",
                                     measure_id="sta1",
                                     label="Station A",
                                     coord=(0, 1),
                                     typical_range=(1., 4.),
                                     river="River 1",
                                     town="Town 1")
    station2 = MonitoringStation(station_id="sta2",
                                     measure_id="sta2",
                                     label="Station B",
                                     coord=(1, 1),
                                     typical_range=None,
                                     river="River 2",
                                     town="Town 2")
    station3 = MonitoringStation(station_id="sta3",
                                     measure_id="sta3",
                                     label="Station C",
                                     coord=(0, 3),
                                     typical_range=(1, -4),
                                     river="River 2",
                                     town="Town 3")

    assert inconsistent_typical_range_stations([station1]) == []
    assert inconsistent_typical_range_stations([station1, station2]) == [station2]
    assert inconsistent_typical_range_stations([station2, station3]) == [station2, station3]
