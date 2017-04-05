
""""
 This script is created for xml configuration
 parsing
"""
import xml.etree.ElementTree as etree
from packet import Packet as packet
from station import Station as station
from event import Event as event

def xml_parsing():
    tree = etree.parse('../config/NetworkConfiguration')
    root = tree.getroot()
    # empty list for stations
    stations_list = []
    for stations in root:
        # Iteration in every station
        for station_xml in stations:
            station_id = int(station_xml.find('stationId').text)
            #print(station_id)
            event_list = []
            station_obj = None
            sifs = int(station_xml.find('sifs').text)
            difs = int(station_xml.find('difs').text)
            for packets_xml in station_xml.findall('packets'):
                for current_packet_xml in packets_xml.findall('packet'):
                    new_packet = packet(int(current_packet_xml.find('size').text), station_id, int(current_packet_xml.find('to').text))
                    event_list.append(event(new_packet))
            station_obj = station(station_id, sifs, difs, event_list)
            stations_list.append(station_obj)
    return stations_list
    #for station_n in stations_list:
    #    print(len(station_n.queue))
