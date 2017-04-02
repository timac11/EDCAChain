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
states = ["transmit", "mis", "sleep", "init"]


class Station:
    # SIFS = 1
    # DIFS = 2
    def __init__(self, stationNumber, Difs, Sifs, queue):
        self.Difs = Difs
        self.Sifs = Sifs
        self.queue = queue
        self.backoff = 1
        # while backoff counter is hardcoded by 100 * backoff
        self.backoffCounter = 100 * self.backoff
        self.state = 'init'
        #self.network = network

    def get_first_output_event(self):
        this_ev = self.queue.pop()
        print(this_ev)
        return this_ev

    def set_queue(self, queue):
        self.queue = queue

    def get_next_packet(self):
        # get the first
        helpList = self.queue
        helpList.revert()
        self.currentPacket = helpList.pop()

    def queue_is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def try_send_packet(self):
        # implement this function
        return 0

    def resolve_backoff(self):
        # implement this function
        return 0

    def resolve_transmition(self):
        #implement this function
        return 0

    def change_state(self):
        #TODO with CASE construction and delete if else
        if self.state == 'sleep':
            return
        if self.state == 'init':
            self.trySendPacket()
        if self.state == 'mis':
            self.resolveBackoff()
        if self.state == 'transmit':
            self.resolveTransmition()

    def push_to_network_queue(self, event):
        self.network.push_to_queue(event)