import numpy as np
from numpy import genfromtxt
import csv
from datetime import datetime

def main():



	csvReader = genfromtxt("/Users/samsklar/Desktop/mcs100/mcs100_hockey/2018_cleaned.csv", delimiter=",", dtype=(np.str, np.str, np.str, np.str, np.str, np.str, np.int_, np.int_, np.str))
	curr_home_team = "ANA"
	previous_goalie = "Check"
	last_date = datetime.strptime("01/01/01", "%m/%d/%y").date()
	count = 0

	for row in csvReader:
		print row



	for row in csvReader:
		if count != 0:
			new_date = datetime.strptime(row[0], "%m/%d/%y").date()
			if row[1] == curr_home_team:
				if new_date - last_date == 1:
					print "got one"
				last_date = new_date
				previous_goalie = row[4]
			else:
				curr_home_team = row[1]
				last_date = row[0]
				previous_goalie = row[4]
		else:
			count = 1



if __name__ == "__main__":
	main()