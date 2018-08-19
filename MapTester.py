# MapTester.py
#
# Flags 1 way connections in map
#
# Written by Aria and Stephen Outten August 2018

import csv, random

def SetupMap(Testing):
    flag = -1
    map_dat = [{},{},{},{}]
    if Testing:
        map_fn = 'Map_ScotlandYard_Testing.dat'
    else:
        map_fn = 'Map_ScotlandYard.dat'
    with open(map_fn, mode='r') as infile:
        reader = csv.reader(infile)
        for rows in reader:
            if len(rows)==1:
                flag=flag+1
                continue
            map_dat[flag][int(rows[0])] = list(map(int, rows[1:]))
    return map_dat[0], map_dat[1], map_dat[2], map_dat[3]

# Main Code

# Imports either the testing map or the full map
Testing = False
taxi, bus, tube, ferry = SetupMap(Testing)


#tube[46]=[1,74,79]

for location in taxi:
  for link in taxi[location]:
    if location not in taxi[link]:
      print (link, "is missing Taxi link", location)

for location in bus:
  for link in bus[location]:
    if location not in bus[link]:
      print (link, "is missing Bus link", location)

for location in tube:
	for link in tube[location]:
		if location not in tube[link]:
			print (link, "is missing Tube link", location)

for location in ferry:
  for link in ferry[location]:
    if location not in ferry[link]:
      print (link, "is missing Ferry link", location)


