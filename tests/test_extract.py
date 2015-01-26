# coding: utf-8

from py.path import local
from pytest import fixture
from pyquery import PyQuery as pq

from gzbus.extract import (extract_routine_name, extract_stations,
                           extract_current_routine)


@fixture
def normal_bus_station_page():
    page = local(__file__).dirpath('data/bus_station/normal.html')
    return pq(page.read())


def test_extract_routine_name(normal_bus_station_page):
    name = extract_routine_name(normal_bus_station_page)

    assert name == '大学城2线'


def test_extract_stations(normal_bus_station_page):
    stations = extract_stations(normal_bus_station_page)
    terminals = sorted(list(stations['terminal'].keys()))

    assert terminals == ['华工大总站①', '大学城(广中医)总站']
    assert len(stations['stations']) == 22


def test_extract_current_routine(normal_bus_station_page):
    stations = extract_stations(normal_bus_station_page)
    current = extract_current_routine(normal_bus_station_page, stations)

    assert current['destinate_station'] == '华工大总站①'
    assert current['bus_station'] == '星海学院站'
    assert current['waiting_station'] == '科学院地化所站'
