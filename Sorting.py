import csv
import sys
from collections import defaultdict
from collections import Counter

#Initializing the counters and ngbhd as a default dictionary with value as string
count1 = 0
count2 = 0
ngbhd = defaultdict(str)

#Reading the dictionary csv
reader1 = csv.reader(open("point_map2.csv","rb"))

#Looping through the csv and creating a dictionary ngbhd with latlon1 as the tupule (key) and neighborhood (value)
for rows in reader1:
    lat1 = float(rows[0])
    lon1 = float(rows[1])
    nghd = rows[2]
    latlon1 = (lat1, lon1)    
    ngbhd[latlon1] = nghd

#Initializing the data dictionary    
data = {}
file2 = open("data3.csv", "rb")
reader2 = csv.reader(file2)             #Reading the data file
locations = [];

#Looping through the data file and printing the neighborhood
for rows2 in reader2:
    lat2 = round((float(rows2[0])),3)   #Rounding coordinates by 3
    lon2 = round((float(rows2[1])),3)
    latlon2 = (lat2,lon2)
    #print (ngbhd[latlon2])
    locations.append(ngbhd[latlon2])
locationDictionary = Counter(locations)
for (key, value) in locationDictionary.iteritems():
    print (key + ": " + str(value))

