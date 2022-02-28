import readline


def sys_line(x):
    print(x * 150)

print(f'\n')
sys_line('=')
print(f'FortiOS Policy ReIndexing')
print("Enter/Paste FortiOS 'config firewall policy below'. Ctrl-D or Ctrl-Z (Windows) to save it.")
sys_line('-')
data_collect = []

# TAKE IN USER INPUT
while True:
    try:
        line = input()
    except EOFError:
        break
    data_collect.append(line)

# COOKIE IN CASE THE INPUT DOES NOT MEET CRITERIA OF EDIT
cookie = False

# CLONE VARIABLES
edit_id = []
policy_list = []
new_id = 1

# DATA VALIDATING AND COPYING
try:
    for line in data_collect:
        line = line.strip()
        if "edit" in line:
            edit_id.append(int(line[5:]))
            policy_list.append(line)
            cookie = True
        elif "config firewall" in line:
            pass
        elif "end" in line:
            pass
        else:
            policy_list.append(line)
except BaseException as error:
    print('There is an error in your config,')

# PRINT FINAL CONFIG
if cookie:
    nl = '\n'
    print(nl)
    sys_line('-')
    user_file = input("Enter a .TXT filename \n[Default = firewall_reindex.txt] \n> ")

    if ".txt" in user_file:
        file_name = user_file
    elif len(user_file) == 0:
        file_name = "firewall_reindex.txt"
    else:
        file_name = user_file + ".txt"

    file = open(file_name, 'w')
    file.write(f'config firewall policy'+nl)
    # PRINTS THE DELETE OBJECTS
    for num in edit_id:
        file.write(f'delete {str(num)}'+nl)
    # PRINTS THE NEW POLICIES
    for line in policy_list:
        if "edit" in line:
            file.write(f'edit {str(new_id)}'+nl)
            new_id += 1
        else:
            file.write(line+nl)
    file.write(f'end'+nl)
    file.close()
    sys_line('*')
    print(nl+f'[{file_name.upper()}] printed to local directory.{nl}')
    sys_line('*')

else:
    print("Did you copy and paste correctly?")
