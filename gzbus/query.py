# coding: utf-8

'''
    gzbus.query
    ~~~~~~~~~~~

    Query bus routines.
'''

import requests
from pyquery import PyQuery as pq

from .data.gzyyjt import buses
from .extract import extract_bus_routine


REALTIME_ROUTINE_QUERY = 'http://www.gzyyjt.com/Bus_station.aspx'


def query_routines(bus_name):
    '''Get bus routines from name.

    TODO support fuzzy matching.

    :param bus_name: the routine name of the bus.
    '''
    return buses.get(bus_name)


def _get_realtime_page(bus_name, bid, cur_station):
    query = {
        'bid': bid,
        'sn': cur_station,
        'bn': bus_name
    }
    resp = requests.get(REALTIME_ROUTINE_QUERY, params=query)

    if not resp.ok:
        return

    return pq(resp.content)


def query_realtime_routine(bus_name, cur_station=None):
    '''Get real time routine.

    TODO support fuzzy matching.

    :param bus_name: the routine name of the bus.
    :param cur_station: current station, deaults to starting station
                        of the routine.
    '''
    routines = query_routines(bus_name)
    if not routines:
        return

    rv = []
    for routine in routines:
        bid = routine['bid']
        _cur_station = cur_station or routine['starting_station']
        page = _get_realtime_page(bus_name, bid, _cur_station)
        rv.append(extract_bus_routine(page))

    return rv
