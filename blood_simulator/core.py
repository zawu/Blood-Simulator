import os,sys,csv

class BloodSimulator:

	def __init__(self):

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


if __name__ == '__main__':
    main()	