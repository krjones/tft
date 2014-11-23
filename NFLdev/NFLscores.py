#!/usr/bin/env python
# This script is in development and may contain bugs
# Written by Kyle R. Jones (kr.jones@me.com)
# 8/17/2014
# All data comes from "http://www.nfl.com/liveupdate/scorestrip/ss.xml"
# 
# This script is intended to run in GeekTool as a shell such as:
# /Users/kyle/Programming/dev/NFLscores.py;cat /Users/kyle/Programming/dev/scores.txt
# You can set it to refresh at any interval
#
#


import optparse, os, pdb, json, pprint,urllib2,sys,time
from xml.dom import minidom
reload(sys);
sys.setdefaultencoding("utf8")

f1 = open('/Users/kyle/Programming/GitHub/tft/NFLdev/scores.txt','w')

xmldata = urllib2.urlopen('http://www.nfl.com/liveupdate/scorestrip/ss.xml')
# xmldata = urllib2.urlopen('http://192.168.0.40/ss.xml')


xmldoc = minidom.parse(xmldata)
itemlist = xmldoc.getElementsByTagName('g')

home_teams = []
home_names = []
home_scores = []

away_teams = []
away_names = []
away_scores = []

redZone = []
possession = []
time = []
quarter = []
status = []
finals = []
clock = []
day = []

i = 0
for s in itemlist:
#	print s.attributes['h'].value
	home_teams.append(s.attributes['h'].value)
	home_names.append(s.attributes['hnn'].value)
	home_scores.append(s.attributes['hs'].value)
	away_teams.append(s.attributes['v'].value)
	away_names.append(s.attributes['vnn'].value)
	away_scores.append(s.attributes['vs'].value)
    	status.append(s.attributes['gt'].value)
	quarter.append(s.attributes['q'].value)
	time.append(s.attributes['t'].value)
	day.append(s.attributes['d'].value)
	
	#determine if the game is in "pregame", "final", "final-overtime", or in progress
	if s.attributes['q'].value == "P":
		possession.append('NaN')
		redZone.append('NaN')
		clock.append('NaN')
	elif s.attributes['q'].value == "F": 
		possession.append('NaN')
		redZone.append('NaN')
		clock.append('NaN')
	elif s.attributes['q'].value == "FO": 
		possession.append('NaN')
		redZone.append('NaN')
		clock.append('NaN')
	elif s.attributes['q'].value == "H": 
		possession.append('NaN')
		redZone.append('NaN')
		clock.append('NaN')
# 		quarter.append('H')
	else:
		possession.append(s.attributes['p'].value)
		redZone.append(s.attributes['rz'].value)
		clock.append(s.attributes['k'].value)
	
		
	if s.attributes['q'].value == 'F':
		finals.append(i)
	else:
		finals.append('NaN')
	i=i+1


# IF viewing in terminal or output to web use the commented out lines below instead of empty start1/end1 
# start1 = "\033[1m"
# end1 = "\033[0;0m"
start1 = ""
end1 = ""
start2 = ""
end2 = ""

j = 0
index = []

for tm in quarter:
# 	if tm != "F" and tm != "FO" and tm != "P" and tm != "H":
	if tm != "F" and tm != "FO" and tm != "P":

		if quarter[j] == str(1):
			qtext = clock[j].ljust(5)+' in the 1st'
		if quarter[j] == str(2):
			qtext = clock[j].ljust(5)+' in the 2nd'
		if quarter[j] == str(3):
			qtext = clock[j].ljust(5)+' in the 3rd'
		if quarter[j] == str(4):
			qtext = clock[j].ljust(5)+' in the 4th'
		if quarter[j] == 'OT':
			qtext = clock[j].ljust(5)+' in Overtime'
		if quarter[j] == 'H':
			qtext = ' at the Half'

			
		if int(away_scores[j]) > int(home_scores[j]):
			f1.write(start1+away_teams[j].ljust(3)+' '+away_names[j].title().ljust(10)+' '+away_scores[j].ljust(2)+end1+' @ '+home_teams[j].ljust(3)+' '+home_names[j].title().ljust(10)+' '+home_scores[j].ljust(2)+' '+qtext)
			f1.write('\n')
			index.append(1)
		elif int(away_scores[j]) < int(home_scores[j]):
			f1.write(away_teams[j].ljust(3)+' '+away_names[j].title().ljust(10)+' '+away_scores[j].ljust(2)+' @ '+start1+home_teams[j].ljust(3)+' '+home_names[j].title().ljust(10)+' '+home_scores[j].ljust(2)+end1+' '+qtext)
			f1.write('\n')
			index.append(1)
		else:
			f1.write(away_teams[j].ljust(3)+' '+away_names[j].title().ljust(10)+' '+away_scores[j].ljust(2)+' @ '+home_teams[j].ljust(3)+' '+home_names[j].title().ljust(10)+' '+home_scores[j].ljust(2)+' '+qtext)
			f1.write('\n')
			index.append(1)
	else:
		index.append(0)
	j=j+1
	sum = 0
for np in index:
	sum = sum + np	


j = 0
for tm in quarter:
	if tm == "F" or tm == "FO":
		if tm == "F":
			trailing_text = quarter[j]+'inal'
		else:
			trailing_text = 'Final OT'
			
		if int(away_scores[j]) > int(home_scores[j]):
			f1.write(start1+away_teams[j].ljust(3)+' '+away_names[j].title().ljust(10)+' '+away_scores[j].ljust(2)+end1+' @ '+home_teams[j].ljust(3)+' '+home_names[j].title().ljust(10)+' '+home_scores[j].ljust(2)+' '+trailing_text)
			f1.write('\n')
		elif int(away_scores[j]) < int(home_scores[j]):
			f1.write(away_teams[j].ljust(3)+' '+away_names[j].title().ljust(10)+' '+away_scores[j].ljust(2)+' @ '+start1+home_teams[j].ljust(3)+' '+home_names[j].title().ljust(10)+' '+home_scores[j].ljust(2)+end1+' '+trailing_text)
			f1.write('\n')
		else:
			f1.write(way_teams[j].ljust(3)+' '+away_names[j].title().ljust(10)+' '+away_scores[j].ljust(2)+' @ '+home_teams[j].ljust(3)+' '+home_names[j].title().ljust(10)+' '+home_scores[j].ljust(2)+' '+trailing_text)
			f1.write('\n')
	j=j+1
j = 0
# print len(quarter)
# print quarter
for tm in quarter:
# 	print tm
# 	print 'j= '+str(j)
        if tm == "P":
# 		pdb.set_trace()
		f1.write(away_teams[j].ljust(3)+' '+away_names[j].title().ljust(13)+' @ '+home_teams[j].ljust(3)+' '+home_names[j].ljust(10).title()+' '+day[j]+' '+time[j].ljust(5)+' ET')
		f1.write('\n')
	j=j+1

f1.close()


