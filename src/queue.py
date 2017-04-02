"""
This class is created for
    queue of packets into a station
    Class consists of next parameters:
        {
           @param int: number: number of packets
           @param list: queue: queue of buffered packets into stations

        }
"""


class Queue:
    def __init__(self, number, queue):
        self.number = number
        self.queue = queue