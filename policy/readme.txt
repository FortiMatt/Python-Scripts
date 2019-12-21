This python script deletes all of the policies and re-indexes them from 1-X.
1.) To get started, run the command "show firewall policy" from your FortiGate. 
2.) Save the file as "policy.txt" and place it in the SAME directory as this script.
3.) Run the script via "python policy_index.py"
4.) The file is written to the directory as "policy_reorg_list.txt"
5.) Upload file to FortiGate via System > Advanced > Configuration Scripts
