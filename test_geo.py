from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.station import MonitoringStation

"""unit test for the geo module"""

def test_stations_by_distance():
    #create dummy data to use for testing
    station1 = MonitoringStation(station_id='station1',
                                     measure_id='station1',
                                     label='station1',
                                     coord=(6, 3),
                                     typical_range=(0, 1),
                                     river='river1',
                                     town='town1')
    station2 = MonitoringStation(station_id='station2',
                                     measure_id='station2',
                                     label='station2',
                                     coord=(0, 1),
                                     typical_range=(0, 1),
                                     river='river2',
                                     town='town2')
    stations=[station1,station2]
    stationsSorted = stations_by_distance(stations, (0,0))
    assert stationsSorted[0][0].station_id == 'station2' # check first station in list is closest 

    assert stationsSorted[1][0].station_id == 'station1' # check second station is further away

def test_stations_within_radius():
    #create dummy data
    station1 = MonitoringStation(station_id='station1',
                                     measure_id='station1',
                                     label='station1',
                                     coord=(20, 20),
                                     typical_range=(0, 1),
                                     river='river1',
                                     town='town1')
    station2 = MonitoringStation(station_id='station2',
                                     measure_id='station2',
                                     label='station2',
                                     coord=(20, -20),
                                     typical_range=(0, 1),
                                     river='river2',
                                     town='town2')
    stations=[station1,station2]

    testCentre=(21,21)

    #pick out stations within 10km of testCentre
    stationsInRadius= stations_within_radius(stations,testCentre,10)

    #Assert that only 1 station is within the radius
    assert stationsInRadius.len() == 1
    #Assert that the station in the radius is station1
    assert stationsInRadius[0].label == 'station2'