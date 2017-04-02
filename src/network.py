"""
    This class emulates
    network work
"""


class Network:
    def __init__(self, stations):
        self.stations = stations

        # transmitted packets in the network
        self.transmitted_packets = []

        # True state is empty in begining
        # self.state = True
        # self.fromStation = -1
        # self.toStation = -1
        # base queue events for all stations in network
        # may be will be emplemented as new base class
        # queue is event list

        self.queue_events = []

        # event in the begining is not determind

        self.event = None

    def queue_is_empty(self):
        return len(self.queue_events) == 0

    def push_to_queue(self, event):
        self.queue_events.append(event)

    def sort_queue(self):
        self.queue_events.sort(key=self.sort_by_time)

    def sort_by_time(event):
        return event.time

    def initialize_queue(self):
        for station in self.stations:
            # first_output_event is function simulating buffer with the size is 1
            self.queue_events.append(station.get_first_output_event())
        print(self.queue_events)

    def get_priority_event_from_queue(self):

        # returns event for packet transmission
        self.event = self.queue_events.pop()
        print(self.event)
        self.event.packet.state = 'transmit'
        return self.event

    def execute_event(self):
        # while all size hardcoded by 1 (this configuration will be written in xml configuration )
        # after transmission 1 frame states of all stations are changed
        # todo after xml implementation parser part_size is changeable

        if self.event is None:
            self.get_priority_event_from_queue()

        self.event.packet.transmit_frame_of_packet(part_size=1)
        print("station", self.event.packet.fromStation,
              "transmits to", self.event.packet.toStation,
              self.event.packet.transmitted_size, "frames of",
              self.event.packet.size, "size")
        if self.event.packet.size == self.event.packet.transmitted_size:
            print("transmitted completed",
                  "packet information:", self.event.packet)
            self.event = None
        # decrease or increase backoff time of each station

        self.change_state_of_each_event()

    def change_state_of_each_event(self):
        for event in self.queue_events:
            event.packet.change_state()

    ##################################################################


    # Getters and setters for parameters

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def set_from_station(self, fromStation):
        self.fromStation = fromStation

    def get_from_station(self):
        return self.fromStation

    def set_to_station(self, toStation):
        self.toStation = toStation

    def get_to_station(self):
        return self.toStation

    #########################################

    def station_management(self):
        return 0

    def start_simulation(self):
        return 0
