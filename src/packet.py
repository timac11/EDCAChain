"""
This class is created for
    implementing of entity of packet
    Class consists of next parameters:
        {
           @:param size: size of current packet
           @:param fromStation: id of transmiting station
           @:param toStation: id of recieving station
           @:param currentState: the part of packet that is transmitted
           @:param transmitted: if packet is transmitted, it is equal to True
            transmitted : function {
                @:param partSize: Size of transmited per one step
                @:return: nothing
            }

        }
"""
import random

class Packet:
    def __init__(self, size, fromStation, toStation):
        # there are states:
        # 'missing' and 'transmit'
        # during 'missing' state packet works with backoff
        # timer and state
        # by default state is missing

        self.size = size
        self.fromStation = fromStation
        self.toStation = toStation
        self.transmitted = False
        self.transmitted_size = 0
        self.state = 'missing'
        self.missing_time = 0

        # in the begining backoff and
        # backoff counter are 0

        # time - is packet parameter
        # by that queue consisting of packets is sorted
        # int

        self.time = 0

        # Also every packet has priority in the station
        # While hardcoded without priority

        self.priority = 0

        #self.backoff_counter = 0
        #self.backoff = 0

        self.choose_backoff()

    def transmit_frame_of_packet(self, part_size):
        self.transmitted_size = self.transmitted_size + part_size

    def is_transmitted(self):
        self.transmitted = True

    def choose_backoff(self):
        # todo random backoff
        # while hardcoded with 10

        self.backoff = random.randint(1, 10)
        self.backoff_counter = random.randint(1, self.backoff)
        self.set_time(self.backoff_counter)

    def change_state(self):
        if self.state == 'missing':
            if self.backoff_counter == 0:
                self.choose_backoff()
            else:
                self.backoff_counter -= 1
        else:
            if self.backoff_counter > 0:
                self.backoff_counter -= 1
        print("packet from station", self.fromStation, "backoff counter =", self.backoff_counter)

    def set_time(self, time):
        self.time += time

    def get_time(self):
        return self.time
