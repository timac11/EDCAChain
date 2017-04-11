""""
This class contains the basis of
determination of discrete event
object: {
            @:param: packet (object)
            @:param: index (int)
}
"""


class Event:
    def __init__(self, packet):
        self.packet = packet
        # by default every index equals 0
        self.index = 0

