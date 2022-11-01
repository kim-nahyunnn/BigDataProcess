#!/usr/bin/python3

import sys
import calendar

days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
mon = dict()
tue = dict()
wed = dict()
thu = dict()
fri = dict()
sat = dict()
sun = dict()
with open(sys.argv[1], "rt") as f:
	for line in f:
		array = line.split(",")
		dateArray = array[1].split("/")
		date = days[calendar.weekday(int(dateArray[2]), int(dateArray[0]), int(dateArray[1]))]
		if date == days[0]:
			if array[0] not in mon:
				mon[array[0]] = [date, int(array[2]), int(array[3])]
			else:
				sumV = mon[array[0]][1] + int(array[2])
				sumT = mon[array[0]][2] + int(array[3])
				mon[array[0]] = [date, sumV, sumT]

		elif date == days[1]:
			if array[0] not in tue:
				tue[array[0]] = [date, int(array[2]), int(array[3])]
			else:
				sumV = tue[array[0]][1] + int(array[2])
				sumT = tue[array[0]][2] + int(array[3])
				tue[array[0]] = [date, sumV, sumT]

		elif date == days[2]:
			if array[0] not in wed:
				wed[array[0]] = [date, int(array[2]), int(array[3])]
			else:
				sumV = wed[array[0]][1] + int(array[2])
				sumT = wed[array[0]][2] + int(array[3])
				wed[array[0]] = [date, sumV, sumT]
		
		elif date == days[3]:
			if array[0] not in thu:
				thu[array[0]] = [date, int(array[2]), int(array[3])]
			else:
				sumV = thu[array[0]][1] + int(array[2])
				sumT = thu[array[0]][2] + int(array[3])
				thu[array[0]] = [date, sumV, sumT]

		elif date == days[4]:
			if array[0] not in fri:
				fri[array[0]] = [date, int(array[2]), int(array[3])]
			else:
				sumV = fri[array[0]][1] + int(array[2])
				sumT = fri[array[0]][2] + int(array[3])
				fri[array[0]] = [date, sumV, sumT]

		elif date == days[5]:
			if array[0] not in sat:
				sat[array[0]] = [date, int(array[2]), int(array[3])]
			else:
				sumV = sat[array[0]][1] + int(array[2])
				sumT = sat[array[0]][2] + int(array[3])
				sat[array[0]] = [date, sumV, sumT]

		else:
			if array[0] not in sun:
				sun[array[0]] = [date, int(array[2]), int(array[3])]
			else:
				sumV = sun[array[0]][1] + int(array[2])
				sumT = sun[array[0]][2] + int(array[3])
				sun[array[0]] = [date, sumV, sumT]

with open(sys.argv[2], "wt") as f:
	for key in mon.keys():
		f.write(key)
		f.write(",MON ")
		f.write(str(mon[key][1]))
		f.write(",")
		f.write(str(mon[key][2]))
		f.write("\n")
	for key in tue.keys():
		f.write(key)
		f.write(",TUE ")
		f.write(str(tue[key][1]))
		f.write(",")
		f.write(str(tue[key][2]))
		f.write("\n")
	for key in wed.keys():
		f.write(key)
		f.write(",WED ")
		f.write(str(wed[key][1]))
		f.write(",")
		f.write(str(wed[key][2]))
		f.write("\n")
	for key in thu.keys():
		f.write(key)
		f.write(",THU ")
		f.write(str(thu[key][1]))
		f.write(",")
		f.write(str(thu[key][2]))
		f.write("\n")
