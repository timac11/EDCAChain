"""
    This class imulates
    network work
"""
import numpy as numPy
import scipy as sciPy

class Network:
    def __init__(self, stations, state):
        self.stations = stations
        #True state is empty in begining
        self.state = True
        self.fromStation = -1
        self.toStation = -1
    # Getters and setters for parameters
    def getState (self):
        return self.state
    def setState (self, state):
        self.state = state
    def setFromStation (self, fromStation):
        self.fromStation = fromStation
    def getFromStation (self):
        return self.fromStation
    def setToStation (self, toStation):
        self.toStation = toStation
    def getFromStation (self):
        return self.toStation
    #########################################
    def changeStateOfEachStation (self):
        for station in self.stations:
            station.changeState()
