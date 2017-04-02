from event import Event as event
from network import Network as network
from packet import Packet as packet
from station import Station as station


def main():
    # this_network = network()

    # here should be some xml parser for input data
    # while it is initialized by some hardcoded massive

    this_stations = []

    # input and creation of 3 stations :
    # while implemented easy scenario
    # the first station has one packet to second
    # the second to the third and the third to the first
    # all packets by the same size is equal to 10
    # todo: implement xml configuration file and xml parser

    station_first = station(stationNumber=1, Sifs=1, Difs=2, queue=[event(packet(10, 1, 2)), event(packet(10, 1, 3))])
    station_second = station(stationNumber=2, Sifs=1, Difs=2, queue=[event(packet(10, 2, 3))])
    station_third = station(stationNumber=3, Sifs=1, Difs=2, queue=[event(packet(10, 3, 1))])

    # append method of stations into network

    this_stations.append(station_first)
    this_stations.append(station_second)
    this_stations.append(station_third)

    # while implemented queue in network is empty in default

    this_network = network(stations=this_stations)

    # after implementing all parameters let's start simulation

    start_simulation(this_network)

"""""
     as for this implementation:
     in this model event = transmition of one data frame in the channel
     and backoff counter increase/decrease is incapsulated in each station
"""""


def start_simulation(this_network):
    # while logs will be written into console
    # todo logs into log file

    this_network.initialize_queue()

    # takes the first event from the queue

    this_network.get_priority_event_from_queue()

    while not this_network.queue_is_empty() or not this_network.event is None:
        this_network.execute_event()
    end_simulation()


def end_simulation():
    print("simulation is completed")


# start implement stations and others objects for creation network
main()
