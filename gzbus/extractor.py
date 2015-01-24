# coding: utf-8

'''
    gzbus.extractor
    ~~~~~~~~~~~~~~~

    Extract Guangzhou bus routines.
'''

import re
from pyquery import PyQuery as pq

from .utils import clean_text as _


ROUTINE_NAME_PATTERN = re.compile('(.*)\(')
CURRENT_ROUTINE_PATTERN = re.compile('.*下一趟开往\[(.*)\]的.*\[(\d*)\]站.*')


def extract_routine_name(page):
    '''Extract routine name from routine page.'''
    text = _(page('.Bus_box h5').text())
    return ROUTINE_NAME_PATTERN.findall(text)[0]


def extract_stations(page):
    '''Extract bus stations from routine page.'''
    stations = [_(station.value) for station in page('.stateName')]
    return {
        'terminal': {
            stations[0]: list(reversed(stations)),
            stations[-1]: stations
        },
        'stations': stations
    }


def extract_current_routine(page, stations):
    '''Extract current routine information from page.'''
    current_routines = CURRENT_ROUTINE_PATTERN.findall(page.text())
    if not current_routines:
        return

    viewpoint = current_routines[0]
    terminal_station, distance = _(viewpoint[0]), int(viewpoint[1])
    stations_to_this_dir = stations['terminal'][terminal_station]

    waiting_station = _(page('.now .stateName').val())
    idx = stations_to_this_dir.index(waiting_station)
    bus_station = stations_to_this_dir[idx - distance]

    return {
        'destinate_station': terminal_station,
        'bus_station': bus_station,
        'waiting_station': waiting_station,
        'distance': distance
    }


def extract_bus_routine(page):
    '''Extract bus routine information from page.'''
    if not isinstance(page, pq):
        page = pq(page)

    stations = extract_stations(page)
    return {
        # Routine name.
        'name': extract_routine_name(page),

        # Bus stations.
        'stations': stations,

        # Current routine.
        'current': extract_current_routine(page, stations)
    }