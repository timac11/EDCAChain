from network import Network as network
import ConfigurationParser as parser


def main():

    this_stations = parser.xml_parsing()

    # creation of network with parameters of stations
    this_network = network(stations=this_stations)

    # after implementing all parameters let's start simulation
    simulation(this_network)

"""""
     as for this implementation:
     in this model event = transmition of one data frame in the channel
     and backoff counter increase/decrease is incapsulated in each station
"""""


def sort_by_time(event):
    return -1*event.packet.time


def initialize_queue(this_network, queue_events):
    for station in this_network.stations:
        # first_output_event is function simulating buffer with the size is 1
        queue_events.append(station.get_first_output_event())


def get_priority_event_from_queue(this_network, queue_events):
    sort_queue(queue_events)
    # returns event for packet transmission
    event = queue_events.pop()
    event.packet.state = 'transmit'
    this_network.set_current_station(event)
    return event


def queue_is_empty(queue_events):
    return len(queue_events) == 0


def push_to_queue(queue_events, event):
    queue_events.append(event)


def sort_queue(queue_events):
    queue_events.sort(key=sort_by_time)


def change_state_of_each_event(queue_events):
    for event in queue_events:
        event.packet.change_state()


def freeze_all_backoffs(queue_events):
    for event in queue_events:
        event.packet.state = 'sleep'


def unfreeze_all_backoffs(queue_events):
    for event in queue_events:
        event.packet.state = 'missing'


def simulation(this_network):

    queue_events = []
    event = None

    # init event queue
    initialize_queue(this_network, queue_events)

    # get priority event from event queue
    event = get_priority_event_from_queue(this_network, queue_events)

    while not queue_is_empty(queue_events) or event is not None:

        if event is None:
            event = get_priority_event_from_queue(this_network, queue_events)

        if event.packet.backoff_counter == 0:
            event.packet.transmit_frame_of_packet(part_size=1)
            # Freeze all backoff of packets in packet queue
            freeze_all_backoffs(queue_events)
            print("station", event.packet.from_station,
                  "transmits to", event.packet.to_station,
                  event.packet.transmitted_size, "frames of",
                  event.packet.size, "size")
            if event.packet.size == event.packet.transmitted_size:
                print("transmitted completed",
                      "packet information:", event.packet)
                # update queue, event and queue into the transmitted station
                event = None
                unfreeze_all_backoffs(queue_events)
                next_station_event = this_network.current_station.get_first_output_event()
                if next_station_event is not None:
                    queue_events.append(next_station_event)
                    sort_queue(queue_events)
        else:
            event.packet.backoff_counter -= 1
            print("packet from station", event.packet.from_station, "backoff counter =",
                  event.packet.backoff_counter)
            # decrease or increase backoff time of each station
        change_state_of_each_event(queue_events)


def end_simulation():
    print("simulation is completed")

main()
