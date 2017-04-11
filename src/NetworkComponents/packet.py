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
    def __init__(self, size, from_station, to_station):

        self.__size = size
        self.__time = 0
        self.__ack = False
        self.__from_station = from_station
        self.__to_station = to_station

        self.transmitted = False
        self.transmitted_size = 0
        self.state = 'missing'

        self.choose_backoff()

    @property
    def ack(self):
        return self.__ack

    @ack.setter
    def ack(self, ack):
        self.__ack = ack

    @property
    def size(self):
        return self.__size

    @property
    def from_station(self):
        return self.__from_station

    @property
    def to_station(self):
        return self.__to_station

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    def transmit_frame_of_packet(self, part_size):
        self.transmitted_size = self.transmitted_size + part_size

    def is_transmitted(self):
        self.transmitted = True

    def choose_backoff(self):
        # todo random backoff to delete and implement present
        self.backoff = random.randint(1, 30)
        self.backoff_counter = random.randint(1, self.backoff)
        self.__time = self.backoff_counter

    def change_state(self):
        if self.state == 'missing':
            if self.backoff_counter == 0:
                self.choose_backoff()
            else:
                self.backoff_counter -= 1
        else:
            if self.state == 'transmit':
                if self.backoff_counter > 0:
                    self.backoff_counter -= 1
        print("packet from station", self.from_station, "backoff counter =", self.backoff_counter)
