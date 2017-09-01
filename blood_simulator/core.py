#!/usr/bin/env python
# coding=utf-8

__author__ = 'Zack'
#For mapping the graph
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from Tkinter import *
import os,sys,csv

#Import the activity and helper class
sys.path.append(os.path.abspath("activity.py"))
import activity
sys.path.append(os.path.abspath("helpers.py"))
import helpers

class BloodSimulator:
	def __init__(self, window):

		#Get set everytime dropdown changes
		self.exercise = None
		self.food = None

		#Initialize the activity class
		self.activity_class = activity.Activity()

		#Inputs
		file_path = os.path.join(os.path.dirname(__file__))
		self.exercise_dict = self.get_activity_dict(file_path + '/exercise.csv')
		self.food_dict = self.get_activity_dict(file_path + '/food.csv')

		#Level Frames
		self.window = window
		self.window.title("Blood Sugar Simulator")
		self.mainframe = Frame(window)
		self.mainframe.grid(column=0,row=0, sticky=(N,W,E,S), pady = 50, padx = 50)
		self.mainframe.columnconfigure(0, weight = 1)
		self.mainframe.rowconfigure(0, weight = 1)

		self.exercise_inputs()
		self.food_inputs()

		self.plot(self.activity_class.blood_sugar_per_minute,self.activity_class.glyceration_level_per_minute)

	def plot(self,blood_sugar,glyceration_level):
		x = helpers.get_minute_array()
		fig = Figure(figsize=(7,7))
		a = fig.add_subplot(1,1,1)

		a.plot(x,blood_sugar,"r-")
		a2 = a.twinx()
		a2.plot(x,glyceration_level,"b-")

		a.set_title ("Blood Sugar Plot", fontsize=16)
		a.set_ylabel("Blood Sugar", fontsize=14)
		a.set_xlabel("Time", fontsize=14)
		a2.set_ylabel("Glyceration Level", fontsize=14)
		
		canvas = FigureCanvasTkAgg(fig, master=self.mainframe)
		canvas.get_tk_widget().grid(row=5,column=1,sticky="nesw",columnspan=4)
		toolbar = NavigationToolbar2TkAgg(canvas, self.mainframe)
		toolbar.grid(row=6,column=1,columnspan=4)
		canvas.draw()

	def update_exercise(self,value):
		self.exercise = value

	def add_exercise(self):
		time = self.exercise_time_input.get()
		invalid_exercise_time_label = None
		if len(time) != 4 or int(time) / 100 >= 24 or int(time) % 100 >=60 :
			tkvar = StringVar(self.mainframe)
			invalid_exercise_time_label = Label(self.mainframe, text="Please use HHMM Military Format", fg="red")
			invalid_exercise_time_label.grid(row=0,column=4)
		else:
			try:
				if type(invalid_exercise_time_label) is not NoneType:
					invalid_exercise_time_label.grid_forget()
				activity = {
					'name':self.exercise_dict[self.exercise]['name'],
					'index':self.exercise_dict[self.exercise]['index'],
					'time':time,
					'type':'exercise'
				}
				self.activity_class.add_activity(activity)
				self.plot(self.activity_class.blood_sugar_per_minute,self.activity_class.glyceration_level_per_minute)
			except:
				invalid_exercise_time_label = Label(self.mainframe, text="Please choose an exercise", fg="red")
				invalid_exercise_time_label.grid(row=0,column=4)

	def update_food(self,value):
		self.food = value

	def add_food(self):
		time = self.food_time_input.get()
		invalid_food_time_label = None
		if len(time) != 4 or int(time) / 100 >= 24 or int(time) % 100 >=60 :
			# print "Time Invalid"
			tkvar = StringVar(self.mainframe)
			invalid_food_time_label = Label(self.mainframe, text="Please use HHMM Military Format", fg="red")
			invalid_food_time_label.grid(row=0,column=3)
		else:
			try:
				if type(invalid_food_time_label) is not NoneType:
					invalid_food_time_label.grid_forget()
				activity = {
					'name':self.food_dict[self.food]['name'],
					'index':self.food_dict[self.food]['index'],
					'time':time,
					'type':'food'
				}
				self.activity_class.add_activity(activity)
				self.plot(self.activity_class.blood_sugar_per_minute,self.activity_class.glyceration_level_per_minute)
			except:
				invalid_food_time_label = Label(self.mainframe, text="Please choose a food", fg="red")
				invalid_food_time_label.grid(row=0,column=3)
	def get_activity_dict(self,csv_file):
	    #Read in csv file 
	    with open(csv_file) as f:
	        reader = csv.DictReader(f)
	        headers = reader.fieldnames
	        rows = list(reader)
	    #Dict to populate with standardized id/name/index format
	    activity_dict = {}
	    #Index by second name. If necessary, can change this to index by something else later
	    dict_index = headers[1]

	    #Foreach row, get values and populate dictionary
	    for row in rows:
	        activity_dict[row[dict_index]] = {}
	        activity_dict[row[dict_index]]['id'] = int(row[headers[0]])
	        activity_dict[row[dict_index]]['name'] = row[headers[1]].decode('ascii','ignore')
	        activity_dict[row[dict_index]]['index'] = int(row[headers[2]])

	    return activity_dict

	"""To paint the exercise inputs"""
	def exercise_inputs(self):
		self.tkvar = StringVar(self.mainframe)
		self.tkvar.set('Choose an Exercise')
		self.exercise_label = Label(self.mainframe, text="Choose an Exercise")
		self.exercise_label.grid(row = 2, column =1)
		self.exercise_menu = OptionMenu(self.mainframe, self.tkvar, *self.exercise_dict.keys(), command=self.update_exercise)
		self.exercise_menu.config(width=30)
		self.exercise_menu.grid(row = 2, column =2)
		self.exercise_time_input = Entry(self.mainframe,width=4)
		self.exercise_time_input.insert(END, '1200')
		self.exercise_time_input.grid(row = 2, column =3)
		self.exercise_button = Button(self.mainframe, text="Add Exercise", width=10, command=self.add_exercise) 
		self.exercise_button.grid(row = 2, column =4)

	"""To paint the food inputs"""
	def food_inputs(self):
		self.tkvar2 = StringVar(self.mainframe)
		self.tkvar2.set('Choose a Food')
		self.food_menu_label = Label(self.mainframe, text="Choose a Food")
		self.food_menu_label.grid(row = 3, column =1)
		self.food_menu = OptionMenu(self.mainframe, self.tkvar2, *self.food_dict.keys(), command=self.update_food)
		self.food_menu.config(width=30)
		self.food_menu.grid(row = 3, column =2)
		self.food_time_input = Entry(self.mainframe,width=4)
		self.food_time_input.insert(END, '1200')
		self.food_time_input.grid(row = 3, column =3)
		self.food_button = Button(self.mainframe, text="Add Food", width=10, command=self.add_food)
		self.food_button.grid(row = 3, column =4)

def main(): 
    root = Tk()
    app = BloodSimulator(root)
    root.mainloop()

if __name__ == '__main__':
    main()		