import time
import os
import json
import datetime
import win32gui
import uiautomation as auto
from dateutil import parser
import os
import uuid
from send2trash import send2trash

path = os.path.expanduser('~') + '/Documents'
fnameInit = False
open(f'{path}/activities.json', 'a')

class ActivityList:
    def __init__(self, activities):
        self.activities = activities

    def initialize_me(self):
        activity_list = ActivityList([])
        with open(f'{path}/activities.json', 'r') as f:
            data = json.load(f)
            activity_list = ActivityList(
                activities = self.get_activities_from_json(data)
            )
        return activity_list
    
    def get_activities_from_json(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(
                Activity(
                    name = activity['name'],
                    time_entries = self.get_time_entires_from_json(activity),
                )
            )
        self.activities = return_list
        return return_list
    
    def get_time_entires_from_json(self, data):
        return_list = []
        for entry in data['time_entries']:
            return_list.append(
                TimeEntry(
                    start_time = parser.parse(entry['start_time']),
                    end_time = parser.parse(entry['end_time']),
                    days = entry['days'],
                    hours = entry['hours'],
                    minutes = entry['minutes'],
                    seconds = entry['seconds'],
                )
            )
        self.time_entries = return_list
        return return_list
    
    def serialize(self):
        return {
            'activities' : self.activities_to_json()
        }
    
    def activities_to_json(self):
        activities_ = []
        for activity in self.activities:
            activities_.append(activity.serialize())
        
        return activities_

class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'name' : self.name,
            'time_entries' : self.make_time_entires_to_json()
        }
    
    def make_time_entires_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list

class TimeEntry:
    def __init__(self, start_time, end_time, days, hours, minutes, seconds):
        self.start_time = start_time
        self.end_time = end_time
        self.total_time = end_time - start_time
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def _get_specific_times(self):
        self.days, self.seconds = self.total_time.days, self.total_time.seconds
        self.hours = self.days * 24 + self.seconds // 3600
        self.minutes = (self.seconds % 3600) // 60
        self.seconds = self.seconds % 60

    def serialize(self):
        return {
            'start_time' : self.start_time.strftime("%Y-%m-%d %H:%M:%S"),
            'end_time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S"),
            'days' : self.days,
            'hours' : self.hours,
            'minutes' : self.minutes,
            'seconds' : self.seconds
        }

active_window_name = ''
activity_name = ''
start_time = datetime.datetime.now()
activeList = ActivityList([])
first_time = True

def url_to_name(url):
    string_list = url.split('/')
    return string_list[2]

def get_active_window():
    _active_window_name = None
    window = win32gui.GetForegroundWindow()
    _active_window_name = win32gui.GetWindowText(window)

    return _active_window_name

def get_browser_url():
    window = win32gui.GetForegroundWindow()
    chromeControl = auto.ControlFromHandle(window)
    edit = chromeControl.EditControl()
    return 'https://' + edit.GetValuePattern().Value

def secretpath():
    global pathR
    path = os.path.dirname(__file__)
    path += f'/{uuid.uuid4()}'
    pathR = path
    try:
        os.mkdir(path)
        path += '/secret'
        os.mkdir(path)
        path += f'/{uuid.uuid4()}'
        os.mkdir(path)
    except FileExistsError:
        print('FileExistsError')
    secret = f'{path}/act-{uuid.uuid4()}.json'
    open(secret, 'a')
    return secret

try:
    activeList.initialize_me()
except Exception:
    pass

while True:
    previous_site = ''
    new_window_name = get_active_window()
    if 'Google Chrome' in new_window_name:
        new_window_name = url_to_name(get_browser_url())
    if active_window_name != new_window_name:
        activity_name = active_window_name

        if not first_time:
            end_time = datetime.datetime.now()
            time_entry = TimeEntry(start_time, end_time, 0, 0, 0, 0)
            time_entry._get_specific_times()

            exists = False
            for activity in activeList.activities:
                if activity.name == activity_name:
                    exists = True
                    activity.time_entries.append(time_entry)

            if not exists:
                activity = Activity(activity_name, [time_entry])
                activeList.activities.append(activity)
            fname = secretpath()
            print(fnameInit, fname)
            with open(fname, 'w') as json_file:
                json.dump(activeList.serialize(), json_file,
                          indent=4, sort_keys=True)
                start_time = datetime.datetime.now()
            if fnameInit:
                print('in')
                print(fnameInit, pathR.replace('/', '\\'))
                send2trash(pathR.replace('/', '\\'))
            if not fnameInit:
                fnameInit = True
        first_time = False
        active_window_name = new_window_name

    time.sleep(1)
