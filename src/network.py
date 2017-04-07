"""
    This class emulates
    network work
"""


# Helpful function for sorting queue by time

def sort_by_time(event):
    return -1*event.packet.time


class Network:
    def __init__(self, stations):
        self.stations = stations

        # transmitted packets in the network

        self.current_station = None

    def set_current_station(self, event):
        self.current_station = self.get_station_by_id(event.packet.from_station)

    def get_station_by_id(self, station_id):
        # There is not situations with invalid station id
        this_station = None
        for station in self.stations:
            if station_id == station.station_number:
                this_station = station
                break
        return this_station
