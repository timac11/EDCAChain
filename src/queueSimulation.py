import random
from network import Network as network
from event import Event as event
from packet import Packet as packet
from station import Station as station
import Generator.NormalRandomGenerator as generator

# global variables
T_CURR_MAX = 1000
event_queue = []
time_gen = []

# hardcoded for debug. None is queue of packets in stations in init
stations = [station(1, 2, 1, None), station(2, 2, 1, None), station(3, 2, 1, None)]


def get_stations_ids():
    stations_ids = []
    for station in stations:
        stations_ids.append(station.id)
    return stations_ids


def change_state(station):
    pass


def simulation():

    # implement data for generation
    stations_ids = get_stations_ids()
    time_gen = generator.init(stations_ids, T_CURR_MAX)

    # life cycle of the network
    time_current = 0
    while time_current <= T_CURR_MAX:
        time_current += 1
        for station in stations:
            change_state(station)


