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
		#Array representing blood sugar level at any given minute in a day
		self.blood_sugar_per_minute = [80] * (config.minutes_in_hour * config.hours_in_day)
		#Array representing glyceration level at any given minute in a day 
		self.glyceration_level_per_minute = [config.starting_glycation_level] * (config.minutes_in_hour * config.hours_in_day)
		#Array erpresenting number of activities at any given minute in a day
		self.change_per_minute = [[] for _ in range(config.minutes_in_hour * config.hours_in_day)]

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

	"""Given an array representing time of day, fill it with blood sugar level per minute"""
	def calculate_bs_level(self):
		current_bs_level = config.normal_blood_sugar_level

		for minute, changes in enumerate(self.change_per_minute):
			#Since we need to know if there were any changes, we can't rely on seeing if sum of changes isn't 0 - instead check size
			if len(changes):
				for change in changes:
					current_bs_level += change
				self.blood_sugar_per_minute[minute] = current_bs_level
			#There were no activities at this minute, so normalize blood sugar level 
			else:
				#Corner case where blood sugar level is between 79-81
				if abs(config.normal_blood_sugar_level - current_bs_level) < 1:
					self.blood_sugar_per_minute[minute] = config.normal_blood_sugar_level
				#Blood sugar is over, decrement
				elif current_bs_level > config.normal_blood_sugar_level:
					current_bs_level -= config.normalize_rate
					self.blood_sugar_per_minute[minute] = current_bs_level
				elif current_bs_level < config.normal_blood_sugar_level:
					current_bs_level += config.normalize_rate
					self.blood_sugar_per_minute[minute] = current_bs_level

	"""Given an array representing time of day, fill it with glyceration level per minute"""
	def calculate_glycation_level(self):
		current_glycation_level = config.starting_glycation_level
		for minute, level in enumerate(self.blood_sugar_per_minute):
			# For every minute your blood sugar stays above the impact level, increment “glycation” by 1
			if level > config.glycation_impact_level:
				current_glycation_level += 1
			self.glyceration_level_per_minute[minute] = current_glycation_level

	"""Get the time series of blood sugar"""
	def get_blood_sugar_per_minute(self):
		return self.blood_sugar_per_minute

	"""Get the time series of glyceration level"""
	def get_glyceration_level_per_minute(self):
		return self.glyceration_level_per_minute

		