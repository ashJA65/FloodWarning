from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station
from floodsystem.station import MonitoringStation
from pandas import RangeIndex

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
                                     coord=(52.208096, -0.112962),
                                     typical_range=(0, 1),
                                     river='river1',
                                     town='town1')
    station2 = MonitoringStation(station_id='station2',
                                     measure_id='station2',
                                     label='station2',
                                     coord=(52.208096, 0.112962),
                                     typical_range=(0, 1),
                                     river='river2',
                                     town='town2')
    stations=[station1,station2]

    testCentre=(52.208490, 0.120794)

    #pick out stations within 10km of testCentre
    stationsInRadius= stations_within_radius(stations,testCentre,10)
    
    #Assert that only 1 station is within the radius
    assert len(stationsInRadius) == 1
    #Assert that the station in the radius is station1
    assert stationsInRadius[0].name == 'station2'

from floodsystem.geo import rivers_by_station_number
def test_rivers_by_station_number():
        
        station1 = MonitoringStation(station_id='station1',
                                     measure_id='station1',
                                     label='station1',
                                     coord=(52.208096, -0.112962),
                                     typical_range=(0, 1),
                                     river='river1',
                                     town='town1')
        station2 = MonitoringStation(station_id='station2',
                                     measure_id='station2',
                                     label='station2',
                                     coord=(47.245091, 8.114722),
                                     typical_range=(0, 1),
                                     river='river2',
                                     town='town2')
        station3 = MonitoringStation(station_id='station3',
                                     measure_id='station3',
                                     label='station3', 
                                     coord=(-2.208096, 9.638102),                                
                                     typical_range=(0, 1),
                                     river='river2',
                                     town='town3')
        station4 = MonitoringStation(station_id='station4',
                                     measure_id='station4',
                                     label='station4', 
                                     coord=(22.208096, 9.638102),                                
                                     typical_range=(0, 1),
                                     river='river3',
                                     town='town4')
                                    
        

        stations=[station1,station2,station3,station4] 
        

        assert rivers_by_station_number(station1,1) == [('river1' , 1)]
        #assert rivers_by_station_number(station1,station2, station3, 1) == {"river2": 2}
        #assert rivers_by_station_number([station1,station2, station3], 2) == {"river2": 2, "river1": 1}


from floodsystem.geo import stations_by_river
    
def test_stations_by_river():

    station1 = MonitoringStation(station_id='station1',
                                     measure_id='station1',
                                     label='station1',
                                     coord=(52.208096, -0.112962),
                                     typical_range=(0, 1),
                                     river='river1',
                                     town='town1')
    station2 = MonitoringStation(station_id='station2',
                                     measure_id='station2',
                                     label='station2',
                                     coord=(47.245091, 8.114722),
                                     typical_range=(0, 1),
                                     river='river2',
                                     town='town2')
    station3 = MonitoringStation(station_id='station3',
                                     measure_id='station3',
                                     label='station3', 
                                     coord=(-2.208096, 9.638102),                                
                                     typical_range=(0, 1),
                                     river='river2',
                                     town='town3')
    station4 = MonitoringStation(station_id='station4',
                                     measure_id='station4',
                                     label='station4', 
                                     coord=(22.208096, 9.638102),                                
                                     typical_range=(0, 1),
                                     river='river3',
                                     town='town4')



def test_rivers_with_stations():
    station1 = MonitoringStation(station_id='sta1',
                                     measure_id='sta1',
                                     label='Test Station 1',
                                     coord=(0., 1.),
                                     typical_range=(0., 1.),
                                     river='river1',
                                     town='test_town_1')
    station2 = MonitoringStation(station_id='sta2',
                                     measure_id='sta2',
                                     label='Test Station 2',
                                     coord=(1., 1.),
                                     typical_range=(0., 1.),
                                     river='river1',
                                     town='test_town_2')
    station3 = MonitoringStation(station_id='sta3',
                                     measure_id='sta3',
                                     label='Test Station 3',
                                     coord=(10., 10.),
                                     typical_range=(0., 1.),
                                     river='river2',
                                     town='test_town_3')

    stations = [station1, station2, station3]
    rivers = rivers_with_station(stations)

    assert len(rivers) == 2
    assert 'river1' in rivers
    assert 'river2' in rivers
