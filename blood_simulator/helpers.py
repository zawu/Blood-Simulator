#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

"""Helper function to get an array given the time"""
def get_minute_array_value(time):
	return time.hour * 60 + time.minute

"""Helper function to get all minutes of a day in an array"""
def get_minute_array():
    now = datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    x = [midnight + timedelta(minutes=x) for x in range(0, 1440)]
    return x
