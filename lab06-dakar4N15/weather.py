# Name: William Sutanto
# Date: 3/15/2023
# File Purpose: Multiple weather functions

import json
import math
import calendar
import datetime

def read_data (filename):
    '''This function will open  the filename in read mode
    and return a dictionary of the JSON decoded contents of the file
    If file does not exist, catch error by FileNotFoundError and return
    an empty dictionary'''
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}

def write_data (data, filename):
    '''This function will open the filename in write mode and
    write the data into the file encoded as JSON'''
    with open(filename, 'w') as file:
        json.dump(data, file)

def max_temperature(data, date):
    '''This fucntion will return the maximum temperature for all
    dictionary data where the key contains data as YYYYMMDD'''
    temperatures = []
    for item in data:
        if date == item[:8]:
            temperatures.append(data[item]["t"])
    
    return max(temperatures) if len(temperatures) else None

def min_temperature(data, date):
    '''This function will return the minimum temperature for all
    dictionary data where the key contains data as YYYYYMMDD'''
    temperatures = []
    for item in data:
        if date == item[:8]:
            temperatures.append(data[item]["t"])
    
    return min(temperatures) if len(temperatures) else None

def max_humidity(data, date):
    '''This function will return the maximum humidity for all
    dictionary data where the key contains the date as YYYYMMDD'''
    humidity = []
    for item in data:
        if date == item[:8]:
            humidity.append(data[item]["h"])

    return max(humidity) if len(humidity) else None

def min_humidity(data, date):
    '''This function will return the minimum humidity for all
    dictionary data where the key contains the data as YYYYMMDD'''
    humidity = []
    for item in data:
        if date == item[:8]:
            humidity.append(data[item]["h"])

    return min(humidity) if len(humidity) else None

def tot_rain(data, date):
    '''This function will return the sum of rainfall for all
    dictionary data where they key contains the date as YYYYMMDD'''
    rainfalls = []
    for item in data:
        if date == item[:8]:
            rainfalls.append(data[item]["r"])

    return sum(rainfalls) if len(rainfalls) else None

def report_daily(data, date):
    '''This function will return a single string which when
    passed to any print function will display on the screen
    formatted'''
    all_data = ""
    all_data += ("========================= DAILY REPORT ========================\n")
    all_data += ("Date                      Time  Temperature  Humidity  Rainfall\n")
    all_data += ("====================  ========  ===========  ========  ========\n")
    for item in data:
        if date == item[:8]:
            date_obj = datetime.datetime.strptime(date, '%Y%m%d')
            month = date_obj.month
            year = date_obj.year
            month_name = calendar.month_name[month]
            formatted_date = f"{month_name} {date_obj.day}, {year}"
            formatted_date = formatted_date.ljust(22)
            all_data += (formatted_date)
            formatted_time = "{:<10}".format(item[8:10] + ":" + item[10:12] + ":" + item[12:14])
            all_data += (formatted_time)
            formatted_temp = "{:>11}".format(data[item]["t"])
            all_data += (formatted_temp)
            all_data += ("  ")
            formatted_humidity = "{:>8}".format(data[item]["h"])
            all_data += (formatted_humidity)
            all_data += ("  ")
            formatted_rainfall = "{:>8}".format(data[item]["r"])
            all_data += (formatted_rainfall)
            all_data += ("\n")
    return all_data

def report_historical(data):
    '''This function will return a single string which when passed
    to any print function will display on the screen formatted'''
    all_data = ""
    stored = []
    all_data += ("============================== HISTORICAL REPORT ===========================\n")
    all_data += ("                          Minimum      Maximum   Minumum   Maximum     Total\n")
    all_data += ("Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n")
    all_data += ("====================  ===========  ===========  ========  ========  ========\n")
    
    for item in data:
        if item[:8] not in stored:
            stored.append(item[:8])
            date_obj = datetime.datetime.strptime(item[:8], '%Y%m%d')
            month = date_obj.month
            year = date_obj.year
            month_name = calendar.month_name[month]
            formatted_date = f"{month_name} {date_obj.day}, {year}"
            formatted_date = formatted_date.ljust(22)
            all_data += (formatted_date)
            formatted_mintemp = f"{min_temperature(data, item[:8]):>11}"
            all_data += (formatted_mintemp)
            all_data += ("  ")
            formatted_maxtemp = f"{max_temperature(data, item[:8]):>11}"
            all_data += (formatted_maxtemp)
            all_data += ("  ")
            formatted_minhumidity = f"{min_humidity(data, item[:8]):>8}"
            all_data += (formatted_minhumidity)
            all_data += ("  ")
            formatted_maxhumidity = f"{max_humidity(data, item[:8]):>8}"
            all_data += (formatted_maxhumidity)
            all_data += ("  ")
            formatted_float = format(round(tot_rain(data, item[:8]), 2), ".2f")
            formatted_rainfall = f"{formatted_float:>8}"
            all_data += (formatted_rainfall)
            all_data += ("\n")

    return all_data



