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

class Packet():
    def __init__(self,size, fromStation, toStation):
        self.size = size
        self.currentState = size
        self.fromStation = fromStation
        self.toStation = toStation
        self.transmitted = False
    def transmitFrameOfPacket(self, partSize):
        self.size = self.size - partSize
    def isTrusmitted (self):
        self.transmitted = True