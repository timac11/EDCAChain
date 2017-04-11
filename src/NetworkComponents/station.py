"""
    This class is created for
    implementing of entity of station
    Class consists of next parameters:
        {
           @:param sifs: short interframe space
           @:param difs: distributed interframe space
           @:param queue: queue of packets of recieving station
           @:param backoff: backoff at the moment
           @:param backoffCounter: backoff counter for current station
            getNextPacket : function {
                @:param:
                @:return:
            }
            queueIsEmpty : function {
                @:param:
                @:return: True, if there is not packets in queue
            }
            changeState, trySendPacket, resolveBackoff, resolveTransmition : function {
                @:param:
                @:return:
            }
        }
"""


class Station:
    def __init__(self, station_number, difs, sifs, queue):
        self.difs = difs
        self.sifs = sifs
        self.queue = queue
        self.station_number = station_number

    def get_first_output_event(self):
        if not self.queue_is_empty():
            this_ev = self.queue.pop()
            return this_ev
        else:
            return None

    def queue_is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

