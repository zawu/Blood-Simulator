#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Contains the defaults for blood sugar calculations"""

minutes_in_hour = 60

hours_in_day = 24

#Blood sugar starts at 80 at the beginning of the day
normal_blood_sugar_level = 80

# For every minute your blood sugar stays above 150, increment “glycation” by 1. This is a
# measure of how much crystallized sugar is accumulating in your blood stream which increases
# heart disease risk.
glycation_impact_level = 150

#In our model, eating food will increase blood sugar linearly for two hours. The rate of increase
#depends on the food as defined in a database that we will provide.
food_impact_minutes = 120.0

#Exercise decreases blood sugar linearly for one hour.
exercise_impact_minutes = 60.0

#Blood sugar starts at 80 at the beginning of the day. If neither food nor exercise is affecting your
#blood sugar (it has been more than 1 or 2 hours), it will approach 80 linearly at a rate of 1 per
#minute.
normalize_rate = 1

starting_glycation_level = 0