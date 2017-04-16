import random

class Station:
    def __init__(self, t_gen):
        self.packet_queue = []
        self.t_gen = t_gen


class Packet:
    def __init__(self, size):
        self.stage = 0
        self.count = 0
        self.transmitted_bytes = 0
        self.size = size
        self.statement = 'init'


# global variables
T_CURR_MAX = 200
event_queue = []
time_gen = []

# todo delete hardcoded t_gen
# hardcoded for debug. None is queue of packets in stations in init
stations = [Station([10, 30, 100]), Station([60, 80])]


def get_stations_ids():
    stations_ids = []
    for station in stations:
        stations_ids.append(station.id)
    return stations_ids


def change_state(station, env_statement):
    if len(station.packet_queue) > 0:
        # change state of the last packet on the queue of packet
        # in the station
        change_packet_state(station.packet_queue, env_statement)


def choose_backoff():
    # todo delete hardcode
    return 10


def change_packet_state(packets, env_statement):
    for packet in packets:
        if env_statement == 'free':
            # check all possible statements of packet
            if packet.statement == 'missing':
                if packet.count == 0:
                    packet.statement = 'transmit'
                else:
                    packet.count += 1
            if packet.statement == 'transmit':
                # hardcoded change of transmitted bytes
                packet.transmited_size += 1
                env_statement = 'busy'
            if packet.statement == 'init':
                packet.statement = 'missing'
                packet.stage = choose_backoff()
                packet.count = packet.stage
            if packet.statement == 'sleep':
                if packet.count == 0:
                    packet.statement = 'transmit'
                    packet.transmited_size += 1
                else:
                    packet.statement = 'missing'
        else:
            if station.statement == 'transmit':
                # hardcoded
                station.transmitted_size += 1
                if packet.transmited_size == packet.size:
                    # delete packet from queue of packets
                    packets.remove(packet)
            else:
                station.statement = 'sleep'


def generate_packet(station):
    # hardcoded packet size
    new_packet = Packet(10)
    station.packet_queue.append(new_packet)


def simulation():

    env_statement = 'free'
    # life cycle of the network
    time_current = 0
    while time_current <= T_CURR_MAX:
        for station in stations:
            change_state(station, env_statement)
            # check if not empty
            if len(station.t_gen) > 0:
                if time_current == station.t_gen[-1]:
                    generate_packet(station)
                    station.t_gen.remove(time_current)
        time_current += 1

###################################################################
simulation()
