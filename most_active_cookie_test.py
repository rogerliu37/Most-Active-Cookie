from sample_cookies import *
from process.process_log import * 
from process.calculate_most_frequent import *

"""
Test files that checks for mutliple log files and what the most frequent cookie is for their respective days in addition to error handling.
"""
FILE_ONE = 'sample_cookies/test_file_one.csv'
FILE_TWO = 'sample_cookies/test_file_two.csv'

EXPECTED_FILE_NOT_FOUND_ERROR_MESSAGE = "You have entered an invalid file. Please try again..."
EXPECTED_VALUE_ERROR_MESSAGE = "You have entered an invalid date. Please try again..."
EXPECTED_TYPE_ERROR_MESSAGE = "You have entered an invalid cookie log. Please try again..."

EXPECTED_TEST_FILE_ONE_LOG = {'2018-12-09': {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 1}, 
                            '2018-12-08': {'SAZuXPGUrfbcn5UA': 1, '4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1}, 
                            '2018-12-07': {'4sMM2LxV07bPJzwf': 1}}
EXPECTED_TEST_FILE_TWO_LOG = {'2018-12-09': {'AtY0laUfhglK3lC7': 2, 'SAZuXPGUrfbcn5UA': 1, '5UAVanZf6UtGyKVS': 2}, 
                            '2018-12-08': {'5UAVanZf6UtGyKVS': 1, 'SAZuXPGUrfbcn5UA': 1, '4sMM2LxV07bPJzwf': 1, 'fbcn5UAVanZf6UtG': 1}, 
                            '2018-12-07': {'4sMM2LxV07bPJzwf': 1, '4sMX2LTV07bPJzFf': 1}}
EXPECTED_MOST_FREQUENT_COOKIES_ONE_DAY_ONE = ['AtY0laUfhglK3lC7']
EXPECTED_MOST_FREQUENT_COOKIES_ONE_DAY_TWO = ['SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
EXPECTED_MOST_FREQUENT_COOKIES_ONE_DAY_THREE = ['4sMM2LxV07bPJzwf']

EXPECTED_MOST_FREQUENT_COOKIES_TWO_DAY_ONE = ['AtY0laUfhglK3lC7', '5UAVanZf6UtGyKVS']
EXPECTED_MOST_FREQUENT_COOKIES_TWO_DAY_TWO = ['5UAVanZf6UtGyKVS', 'SAZuXPGUrfbcn5UA', '4sMM2LxV07bPJzwf', 'fbcn5UAVanZf6UtG']
EXPECTED_MOST_FREQUENT_COOKIES_TWO_DAY_THREE = ['4sMM2LxV07bPJzwf', '4sMX2LTV07bPJzFf']

def test_process_log_one():
    actual = process_log(FILE_ONE)
    assert EXPECTED_TEST_FILE_ONE_LOG == actual

def test_process_log_two():
    actual = process_log(FILE_TWO)
    assert EXPECTED_TEST_FILE_TWO_LOG == actual

def test_most_frequent_one():
    log = process_log(FILE_ONE)
    actual = calculate_most_frequent(log, '2018-12-09')
    assert EXPECTED_MOST_FREQUENT_COOKIES_ONE_DAY_ONE == actual

def test_most_frequent_two():
    log = process_log(FILE_ONE)
    actual = calculate_most_frequent(log, '2018-12-08')
    assert EXPECTED_MOST_FREQUENT_COOKIES_ONE_DAY_TWO == actual

def test_most_frequent_three():
    log = process_log(FILE_ONE)
    actual = calculate_most_frequent(log, '2018-12-07')
    assert EXPECTED_MOST_FREQUENT_COOKIES_ONE_DAY_THREE == actual

def test_most_frequent_two_day_one():
    log = process_log(FILE_TWO)
    actual = calculate_most_frequent(log, '2018-12-09')
    assert EXPECTED_MOST_FREQUENT_COOKIES_TWO_DAY_ONE == actual

def test_most_frequent_two_day_two():
    log = process_log(FILE_TWO)
    actual = calculate_most_frequent(log, '2018-12-08')
    assert EXPECTED_MOST_FREQUENT_COOKIES_TWO_DAY_TWO == actual

def test_most_frequent_two_day_three():
    log = process_log(FILE_TWO)
    actual = calculate_most_frequent(log, '2018-12-07')
    assert EXPECTED_MOST_FREQUENT_COOKIES_TWO_DAY_THREE == actual

def test_invalid_csv():
    actual = process_log('invalid.csv')
    assert EXPECTED_FILE_NOT_FOUND_ERROR_MESSAGE == actual

def test_invalid_date():
    log = process_log(FILE_ONE)
    actual = calculate_most_frequent(log, '00-00-00')
    assert EXPECTED_VALUE_ERROR_MESSAGE == actual