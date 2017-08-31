#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta

"""Helper function to get an array given the time"""
def get_minute_array_value(time):
	return time.hour * 60 + time.minute