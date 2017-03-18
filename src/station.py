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
import numpy as numPy
import scipy as sciPy
states = ["transmit", "mis", "sleep","init"]
class Station:
    #SIFS = 1
    #DIFS = 2
    def __init__(self, stationNumber, Difs, Sifs, queue):
        self.Difs = Difs
        self.Sifs = Sifs
        self.queue = queue
        self.backoff = 1
        #while backoff counter is hardcoded by 100 * backoff
        self.backoffCounter = 100 * self.backoff
        self.state = 'init'
    def getNextPacket (self):
        #get the first
        helpList = self.queue
        helpList.revert()
        self.currentPacket = helpList.pop()
    def queueIsEmpty (self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    def trySendPacket(self):
        #implement this function
        return
    def resolveBackoff(self):
        #implement this function
        return
    def resolveTransmition(self):
        #implement this function
        return
    def changeState(self):
        #TODO with CASE construction and delete if else
        if self.state == 'sleep':
            return
        if self.state == 'init':
            self.trySendPacket()
        if self.state == 'mis':
            self.resolveBackoff()
        if self.state == 'transmit':
            self.resolveTransmition()