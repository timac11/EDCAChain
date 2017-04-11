"""
    This class emulates
    network work
"""

def sort_by_time(event):
    return -1*event.packet.time


class Network:
    def __init__(self, stations):
        self.__stations = stations

    @property
    def stations(self):
        return self.__stations

    @stations.setter
    def stations(self, stations):
        self.__stations = stations

    def get_station_by_id(self, station_id):
        this_station = None
        for station in self.stations:
            if station_id == station.station_number:
                this_station = station
                break
        return this_station
