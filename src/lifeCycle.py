import network  as network
import packet as packet
import queue as queue
import station as station


def main():
    # quallity of stations
    numberOfStations = 2
    stations = []
    sifs = 1
    difs = 2
    for i in range(0, numberOfStations):
        newStation = station(i, sifs, difs, [])
        stations.append(newStation)
    # by default network is empty
    queues = []
    packetFirst = packet(10, 0, 1)
    packetSecond = packet(20,1, 0)
    #for i in range (0, numberOfStations):
    #    stations[i].setQueue(queues[i])
    #while thois procedure hardcoded
    queue1 = []
    queue2 = []
    queue1.append(packetFirst)
    queue2.append(packetSecond)
    stations[0].setQueue(queue1)
    stations[1].setQueue(queue2)
    #initialization of the network
    thisNetwork = network(stations, True)
    return 0
def simulation(thisNetwork):
    thisNetwork.startsimulation()
    return 0

