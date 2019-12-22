### POLICY_REORDER.PY
### AUTHOR: FORTIMATT

#PRINT GENERAL MESSAGE
print('='*60+'''
This python script deletes all of the policies and re-indexes them from 1 - X\n'''+'='*60+'''
1.) To get started, run the command "show firewall policy" from your FortiGate. 
2.) Save the file as "policy.txt" and place it in the SAME directory as this script.
3.) Run the script via "python policy_reorder.py"
4.) The new config will be saved to the directory as "policy_reorg_list.txt"
5.) Upload file to your FortiGate via System > Advanced > Configuration Scripts\n'''+'='*60)
#COLLECT USERINPUT
user_var = raw_input('Are you ready to get started? (Yes / No)')
#SEE IF FIRST LETTER IS = Y, IF SO WE RUN THE SCRIPT
if user_var[0].lower() == 'y':
	#OPEN FILE
	data = open("policy.txt", "r")
	#CREATE BLANK LIST FOR APPENDING LINES/IDS TO
	policy_list = []
	edit_id = []
	#STARTS NEW ID AT 1
	new_id = 1
	#SETS TWO CONFIG VARIABLES FOR PRINT
	conf_policy = "config firewall policy\n"
	end = "end\n"
	#MAIN LOOP TO FIND OUT HOW MANY EDIT "#" ARE IN THE TEXT FILE
	for line in data:
		#IF THE LINE IS CONTAINS CONFIG (USUALY CONFIG FIREWALL POLICY) REMOVE IT ALL TOGETHER
		if "config" in line:
			pass
		#IF EDIT IS IN THE LINE
		elif "edit" in line:
			#SPLIT THE LINE AND REMOVE THE DIGIT
			[int(s) for s in line.split() if s.isdigit()]
			#HERE WE SAVE THE ID FOR PRINTING/REMOVING
			edit_id.append(s)
			#ONCE DONE APPEND LINE TO A LIST FOR SECOND LOOP
			policy_list.append(line)
		#IF SET UUID IS IN THE LINE REMOVE IT ALL TOGETHER
		elif "set uuid" in line:
			pass
		#ELSE IF NO MATCH ON LINE APPEND IT TO THE POLICY_LIST
		else:
			policy_list.append(line)
	#CLOSE THE FILE READ
	data.close()

	f = open("policy_reorg_list.txt", "a")
	#NOW THAT WE HAVE OUR VARIABLES IT IS TIME TO REMOVE THE POLICIES
	f.write(conf_policy)
	#LOOP THROUGH EDIT ID'S TO REMOVE THEM
	for num in edit_id:
		f.write("delete "+num+"\n")
	#PRINT END VARIABLE
	f.write(end)
	#NOW THAT WE HAVE OUR VARIABLES IT IS TIME TO ADD THE POLICIES BACK IN BUT WITH A NEW ID
	f.write(conf_policy)
	#LOOP THROUGH POLICY LIST
	for line in policy_list:
		#IF THE LINE CONTAINS EDIT
		if "edit" in line:
			#PRINT EDIT AND THE NEW ID = 1
			f.write("edit "+str(new_id)+"\n")
			#ADD A DIGIT TO NEW ID FOR OUR NEW SEQUENCE ID
			new_id+=1
		#IF THE LINE IS NOT EDIT, PRINT IT OUT AND STIP OFF PADDING AND \N
		else:
			f.write(line.strip()+"\n")
	f.close()
	print("="*60+"\nYour conversion is complete. File saved as policy_reorg_list.txt\n"+"="*60)
#IF USER INPUT = NO THEN PRINT
else:
	print("Sorry try running the script again!")
