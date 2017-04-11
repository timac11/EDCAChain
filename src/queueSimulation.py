import random
from network import Network as network
from event import Event as event
from packet import Packet as packet
from station import Station as station

# global variables
time_current = 0
T_CURR_MAX = 1000
event_queue = []
time_gen = []
stations = []


def generate_packet(station_number):
    time = random.randint(1, T_CURR_MAX)
    if time  > time_current:
        time_gen.append(time)


# time is sorted always
def add_packet():
    if time_gen[-1] == time_current:
        

def simulation():

