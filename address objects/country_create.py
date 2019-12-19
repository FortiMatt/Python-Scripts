#!/usr/bin/python


### FORTIOS_COUNTRY_CREATE.PY
### AUTHOR: FORTIMATT
### OBJ: SIMPLE PYTHON SCRIP TO CREATE ADDRESS' AND ADDRESS GROUPS 
### OBJ (CONT): BASED ON ISO-3166 STANDARDS TO IMPORT INTO FORTIOS

### BASED ON ISO-3166 FILE
user_csv_file = 'all.csv' #<- MODIFY ME IF NEW LIST IS REQUIRED

#IMPORT CSV MODULE INTO PYTHON FOR READING OUR CSV FILE FROM: 
#https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv
import csv

#GENERAL MOTD BANNER PRINT
print('===================== Welcome =====================')
#ASK IF USER IS INTERESTED IN A COMMON CYBERCRIME LIST
hacking_input = raw_input("Are you interested in a list of Countries where most cybercrime originates? (Yes/No) ")
#CHECK IF INPUT IS EQUAL TO "YES"
if hacking_input[0].lower() == "y":
	#SET THE FILE TO CYBERCRIME_ADDRESSLIST.TXT
	filename = 'cybercrime_addresslist.txt'
	#OPEN AND READ THE FILE VAR TEXT.CSV BY DEFAULT
	csv_file = csv.reader(open(user_csv_file, "rb"), delimiter=",")
	# TOP SECURITY/CYBERCRIME COMPANIES
	country_list = ['CN','TR','RU','TW','BR','RO','IN','IT','HU']
	#NULL LIST THAT GETS ADDED TO AS WE LOOP THROUGH THE CSV FOR ADDRGRP CONFIG
	addrgrp = []
	#CREATE THE FILE
	f = open(filename,'w')
	#START WRITING TO THE FILE
	f.write('config firewall address\n')
	#LOOP THROUGH THE ROWS IN CSV
	for row in csv_file:
		#FOR COUNTRY IN THE LIST CHECK ROW TO SEE IF MATCH IN INDEX 1 AKA ISO-3166 2 DIGIT NAME
		for country in country_list:
			#IF WE FIND A MATCH WRITE OUT GENERAL CONTENT
			if row[1] == country:
				f.write('''edit "'''+row[0]+'''"
set type geography
set color 6
set country '''+row[1]+'''
set comment "'''+row[5]+''' RC = '''+row[8]+''' and '''+row[6]+''' SRC = '''+row[9]+'''"
next\n''')
				#APPEND THE FOUND 2 DIGIT NAME TO LIST
				addrgrp.append(row[0])
	f.write('end\n')
	f.write('config firewall addrgrp\n')
	f.write('edit "Bad Countries"\n')
	f.write('set color 6\n')
	#WRITE ALL THE ADDRESS IN ADDRGROUP VIA APPEND FORTIOS
	for addr in addrgrp:
		f.write('append member "'+addr+'"\n')
	f.write('end')
	#NOTIFY USER OF OUTPUT FILE
	print('=================== OUTPUT FILE ===================')
	print('Your file is complete and was saved as "'+filename+'" in this directory.')
	print('===================== Goodbye =====================')
#IS THE USER SELECTS NO TO THE CYBERCRIME INPUT EXCUTE THE CUSTOM COUNTRY CONFIG
else:
	#DEFINING OUR TWO DICTIONARIES/REGIONS
	region_dic = {'Africa':2,'Oceania':9,'Americas':19,'Asia':142,'Europe':150}
	sub_region_dic = {'Northern Africa':15,'Northern America':21,'Eastern Asia':30,'Southern Asia':34,'South-eastern Asia':35,'Southern Europe':39,'Australia and New Zealand':53,'Melanesia':54,'Micronesia':57,'Polynesia':61,'Central Asia':143,'Western Asia':145,'Eastern Europe':151,'Northern Europe':154,'Western Europe':155,'Sub-Saharan Africa':202,'Latin America and the Caribbean':419}

	#PRINTING OUT THE DICTIONARIES FOR USER INPUT
	print("="*20+"REGION CODES"+"="*20)
	for key,val in sorted(region_dic.items()):
	    print('"'+key+'" = '+str(val))
	print("="*18+"SUB REGION CODES"+"="*18)
	for key,val in sorted(sub_region_dic.items()):
	    print('"'+key+'" = '+str(val))
	print("="*54)


	#COLLECT USER VARIABLES TO WORK WITH IN THE SCRIPT
	print('===================== Welcome =====================')
	#USER INPUT
	user_input = int(raw_input('Please enter a region or sub-region code (ex: Americas = 19) \nif no input all country address objects will display: '))
	#IF USERINPUT IS NOT EMPTY WE SET USER INPUT VAR TO AN INTEGER
	user_input = int(user_input)
	#ADDING DICTIONARIES TOGETHER FOR SEARCHING
	region_dic.update(sub_region_dic)
	def find_key(input_dict, value):
	    return next((k for k, v in input_dict.items() if v == value), "Sorry, you did not enter a number from the list above. Please try again.")

	filename_orig = find_key(region_dic,user_input)
	filename = filename_orig.lower().replace(" ", "_")+".txt"

	print("-"*54)

	#COLLECT THE USER VISIBILITY PORTION FOR FORTIOS
	user_vis = raw_input('Would you like the address objects viewable in the source/destination fields of policy?\nDefault is enabled, enter "d" to disable: ')

	#RUNNING USER ADDRESS VISIBILITY THROUGH A CHECK OF ENABLE/DISABLE
	#IF USER SELECTS "D" FOR DISABLE WE SET THE VARIABLE TO "SET VISIBILITY DISABLE" FOR FORTIOS
	if user_vis.lower() == "d":
		user_vis = '\nset visibility disable'

	#READ CSV, AND SPLIT ON "," THE LINE
	csv_file = csv.reader(open(user_csv_file, "rb"), delimiter=",")

	#HERE WE CHECK IF THE USER ENTERED A COUNTRY CODE
	#IF YES, CHECK IF ITS A DIGIT AND LENGTH OF 3
	if user_input != "":
		#SET ADDRGRP LIST TO NULL SO WE CAN APPEND THE SEARCH VALUES TO IT (LINE 40)
		#LATER USED FOR THE ADDRGROUP CREATION
		addrgrp = []
		search_var = format(user_input, '03d')
		#PRINT OUT/ACCESS THE FIREWALL ADDRESS SECTION OF FORTIOS
		f = open(filename,'w')
		f.write('config firewall address\n')
		#LOOP THROUGH CSV LIST
		for row in csv_file:
			#row_count = sum(1 for row in csv_file)  # fileObject is your csv.reader
			#print(row_count)
			#IF THE USER INPUT IS = TO 8 OR 9 LIST BACK THE LINES
			if search_var == row[8] or search_var == row[9]:
				#MAIN PRINT SECTION, LOOPING THROUGH AND CREATING EACH ADDRESS
				f.write('''edit "'''+row[0]+'''"
set type geography
set color 6
set country '''+row[1]+'''
set comment "'''+row[5]+''' RC ='''+row[8]+''' and '''+row[6]+''' SRC = '''+row[9]+'''"'''+user_vis+'''
next\n''')
				#ONCE THE LOOP IS COMPLETE WE APPEND ROW 0 TO THE LIST FOR ADDRGROUP CREATION BELOW (LINE 40)
				addrgrp.append(row[0])
		#PRINTING GENERIC FORTIOS COMMANDS TO GET US TO THE CORRECT BRANCH OF CONFIG
		f.write('end\n')
		f.write('config firewall addrgrp\n')
		#CHECK IF USER INPUT IS EQUAL TO ROW 8 IE REGION CODE
		#IF IT IS CREATE THE ADDRGRP NAME BASED ON REGION CODE
		f.write('edit "'+filename_orig+'"\n')
		for addr in addrgrp:
			f.write('append member "'+addr+'"\n')
		f.write('end')

	#IF NO DIGIT IS ENTERED INTO THE SCRIPT DISPLAY ALL ADDRESS OBJECTS
	else:
		filename = "all_countries.txt"
		f = open(filename,'w')
		f.write('config firewall address\n')
		#MAIN PRINT SECTION, LOOPING THROUGH AND CREATING EACH ADDRESS
		for row in csv_file:
	    		f.write('''edit "'''+row[0]+'''"
set type geography
set color 6
set country '''+row[1]+'''
set comment "'''+row[5]+''' RC ='''+row[8]+''' and '''+row[6]+''' SRC = '''+row[9]+'''"'''+user_vis+'''
next\n''')
		f.write("end")
	f.close()
	print('=================== OUTPUT FILE ===================')
	print('Your file is complete and was saved as "'+filename+'" in this directory.')
	print('===================== Goodbye =====================')
