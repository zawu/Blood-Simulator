#!/usr/bin/env python
# coding=utf-8

#For mapping the graph
import matplotlib
matplotlib.use('TkAgg')

from Tkinter import *
import os,sys,csv

#Import the activity class
sys.path.append(os.path.abspath("activity.py"))
import activity


class BloodSimulator:

	def __init__(self,window):
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

		self.tkvar = StringVar(self.mainframe)
		self.tkvar.set('Choose an Exercise')
		self.exercise_label = Label(self.mainframe, text="Choose an Exercise")
		self.exercise_label.grid(row = 2, column =1)
		self.exercise_menu = OptionMenu(self.mainframe, self.tkvar, *self.exercise_dict.keys())
		self.exercise_menu.config(width=30)
		self.exercise_menu.grid(row = 2, column =2)
		self.exercise_time_input = Entry(self.mainframe,width=4)
		self.exercise_time_input.insert(END, '1200')
		self.exercise_time_input.grid(row = 2, column =3)
		self.exercise_button = Button(self.mainframe, text="Add Exercise", width=10) 
		self.exercise_button.grid(row = 2, column =4)

		self.tkvar2 = StringVar(self.mainframe)
		self.tkvar2.set('Choose a Food')
		self.food_menu_label = Label(self.mainframe, text="Choose a Food")
		self.food_menu_label.grid(row = 3, column =1)
		self.food_menu = OptionMenu(self.mainframe, self.tkvar2, *self.food_dict.keys())
		self.food_menu.config(width=30)
		self.food_menu.grid(row = 3, column =2)
		self.food_time_input = Entry(self.mainframe,width=4)
		self.food_time_input.insert(END, '1200')
		self.food_time_input.grid(row = 3, column =3)
		self.food_button = Button(self.mainframe, text="Add Food", width=10)
		self.food_button.grid(row = 3, column =4)

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


def main(): 
    root = Tk()
    app = BloodSimulator(root)
    root.mainloop()

if __name__ == '__main__':
    main()		