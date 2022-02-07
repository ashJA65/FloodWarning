from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    station1 = MonitoringStation(station_id='station1',
                                     measure_id='station1',
                                     label='station1',
                                     coord=(6, 3),
                                     typical_range=(0, 1))
    station2 = MonitoringStation(station_id='station2',
                                     measure_id='station2',
                                     label='station2',
                                     coord=(0, 1),
                                     typical_range=(0, 1))
    stations=[station1,station2]
    stationsSorted = stations_by_distance(stations, (0,0))
it
    assert stationsSorted[0][0].station_id == 'station2' # check first station in list is closest 

    assert stationsSorted[1][0].station_id == 'station1' # check second station is further away

