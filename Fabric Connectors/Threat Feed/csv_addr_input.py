#IMPORT IPADDRESS MODULE
import ipaddress

#GENERAL PRINT FOR VISUAL PERSPECTIVE
print("="*50)
#COLLECT USER INPUT
user_input = input("Please enter an IP or network/subnet in CSV fortmat \n(ex: 1.1.1.1,192.168.0.0/24):  ")
#SPLIT USER INPUT VIA ","
search_var = user_input.split(",")

#USER FILE **CHANGE IF NEEDED**
user_file = "custom_ip_list.txt"
#OPEN USER FILE FOR READING
f = open(user_file,"r")
#READ THE LINES OF THE FILE AND SPLIT THEM
user_file_r = f.read().split()
#CLOSE THE READ FILE
f.close()
#BLANK LIST FOR LOOP/APPENDING LATER
user_append_list = []

#DEFINING IPCHECK FUNCTION
def ip_check(string):
		#TRY  STRING = IP
		try:
			#USED VIA THE IMPORT OF IPADDRESS MODULE
			ipaddress.ip_address(string)
			#IF IT IS A SINGLE IP APPEND IT TO THE BLANK LIST FOR LOOP/WRITING LATER
			user_append_list.append(string)
			#GENERIC OUTPUT OF IP ADDED
			print("[+] "+string+" IP added to the list.")
		#IF IP IS NOT A MATCH CHECK IF STRING = NETWORK/SUBNET
		except:
			try:
				#USED VIA THE IMPORT OF IPADDRESS MODULE
				ipaddress.ip_network(string)
				#IF IT IS A SUBNET/MASK APPEND IT TO THE BLANK LIST FOR LOOP/WRITING LATER
				user_append_list.append(string)
				#GENERIC OUTPUT OF SUBNET/MASK ADDED
				print("[+] "+string+" Network added to the list.")
			#IF NO MATCH, PRINT THE INPUT WAS NEITHER AN IP OR A SUBNET
			except ValueError:
				print("[!] "+string+" is not a valid IP or SUBNET/MASK and therefore was not added to the list.")

#IP LOOP FROM USER SEARCH LIST
print("="*50)
#MEAT AND POTATOES OF THE SCRIPT, LOOP THROUGH USER VARIABLES AND TRY THEM AGAINST OUR IPCHECK FUNCTION
for ip in search_var:
	#FIRST IF IP IS ALREADY IN THE FILE, DO NOTHING AND PRINT GENERIC OUTPUT
        if ip in user_file_r:
                print('[!] '+ip+' already exists in "'+user_file+'"')
	#IF IT IS NOT IN THE FILE/LINE RUN IT THROUGHT OUR FUNCTION
        else:
                ip_check(ip)
#GENERIC PRINT OUTPUT FOR VISUAL PERSPECTIVE 
print("="*50)

#APPENDING VALID IP'S TO OUR LIST
f = open(user_file,"a")
#LOOP THROUGH OUR APPEND LIST AND WRITE EACH VARIABLE AS NEW LINE TO OUR FILE
for ip in user_append_list:
        f.write(ip+"\n")
#CLOSE THE FILE
f.close()
