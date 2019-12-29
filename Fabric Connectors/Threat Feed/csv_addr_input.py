#IMPORT IPADDRESS MODULE
import ipaddress

print("="*50)
#COLLECT USER INPUT
user_input = input("Please enter your IP's in CSV format: ")
#SPLIT USER INPUT VIA ","
search_var = user_input.split(",")

#USER FILE **CHANGE IF NEEDED**
user_file = "custom_ip_list.txt"
#OPEN USER FILE FOR READING
f = open(user_file,"r")
user_file_r = f.read().split()
f.close()
#BLANK LIST FOR LOOP/APPENDING LATER
user_append_list = []

#DEFINING IPCHECK FUNCTION
def ip_check(string):
        try:
                ipaddress.ip_address(string)
                user_append_list.append(string)
                print("[+] "+string+" added to the list.")
        except ValueError:
                print("[!] "+string+" is not a valid IP and therefore was not added to the list.")

#IP LOOP FROM USER SEARCH LIST
print("="*50)
for ip in search_var:
        if ip in user_file_r:
                print('[!] '+ip+' already exists in "'+user_file+'"')
        else:
                ip_check(ip)
print("="*50)
#APPENDING VALID IP'S TO OUR LIST
f = open(user_file,"a")
for ip in user_append_list:
        f.write(ip+"\n")
f.close()
