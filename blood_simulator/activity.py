#!/usr/bin/env python
# coding=utf-8

#For importing config/helper files
import os,sys
sys.path.append(os.path.abspath("config.py"))
import config
sys.path.append(os.path.abspath("helpers.py"))
import helpers

from datetime import datetime, timedelta

#Class to contain all inputs into the simulator 
class Activity:

	def __init__(self):
		#To hold all inputs
		self.inputs = []

	def add_activity(self,activity):
		new_activity = {
			'id':len(self.inputs) + 1,
			'name':activity['name'],
			'index':activity['index'],
			'time':activity['time'],
			'type':activity['type']
		}

	"""Given a list of activities, figure out the time frame of impact first"""
	def process_activities(self,activity_list):
		#For each activity in activity list, process 
		for activity in activity_list:
			#Calculate impact per minute
			impact_per_minute = (-activity['index'] / config.exercise_impact_minutes) if activity['type'] == 'exercise' else (activity['index'] / config.food_impact_minutes)
			#Calculate the time interval
			start_time = helpers.get_minute_array_value(datetime.strptime(activity['time'], '%H%M'))
			end_time = (start_time + config.exercise_impact_minutes) if activity['type'] == 'exercise' else (start_time + config.food_impact_minutes)
			#Use impact/minute and time interval in order to calculate the change per minute
			while start_time <= end_time and start_time < 1440 and end_time < 1440 :
				self.change_per_minute[start_time].append(impact_per_minute)
				start_time += 1