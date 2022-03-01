"""Unit test for the flood module"""

from floodsystem.flood import *
from floodsystem.station import MonitoringStation


def test_stations_level_over_threshold():
    station1 = MonitoringStation(station_id='test1',
                                 measure_id='test2',
                                 label='test1',
                                 coord=(5, 6),
                                 typical_range=(0., 1.),
                                 river='test1',
                                 town='test1')
    station2 = MonitoringStation(station_id='test2',
                                 measure_id='test2',
                                 label='test2',
                                 coord=(1., 1.),
                                 typical_range=(1., 0.),
                                 river='test2',
                                 town='test2')

    station1.latest_level = 0.7
    station2.latest_level = 0.6

    stations = [station1, station2]

    assert stations_level_over_threshold(stations, 0.5)[0][0] == "test1"


def stations_highest_rel_level():
    station1 = MonitoringStation(station_id='test1',
                                 measure_id='test2',
                                 label='test1',
                                 coord=(5, 6),
                                 typical_range=(0., 1.),
                                 river='test1',
                                 town='test1')
    station2 = MonitoringStation(station_id='test2',
                                 measure_id='test2',
                                 label='test2',
                                 coord=(1., 1.),
                                 typical_range=(1., 0.),
                                 river='test2',
                                 town='test2')

    station1.latest_level = 0.5
    station2.latest_level = 0.6

    stations = [station1, station2]

    assert stations_highest_rel_level(stations, 3) == [station2, station1]
    assert stations_highest_rel_level(stations, 2) == [station2]

    station1.latest_level = 0.5
    station2.latest_level = 0.6

    assert stations_highest_rel_level(stations, 3) == [station2, station1]
    assert stations_highest_rel_level(stations, 2) == [station2, station1]
