import random
PACKETS_QUALITY = random.Random(200)
PACKET_SIZE_MAX = 50


def init(stations_ids, t_max):
    time_gen = []
    for i in range(PACKETS_QUALITY):

        # choose random id from the list of posible ids of stations
        station_id_from = random.Random(stations_ids)
        station_id_to = random.Random(stations_ids)
        time = random.Random(t_max)
        packet_size = random.Random(PACKET_SIZE_MAX)

        # event in current version is the pair of station id and time of packet generation and size
        event = station_id_from, station_id_to, time, packet_size
        time_gen.append(event)
    return time_gen
