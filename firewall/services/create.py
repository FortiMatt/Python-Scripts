import csv

finished_file = open("services.txt", "w")
finished_file.write('config firewall service category\nedit "CUSTOMGRP"\nset comment "MADE VIA SCRIPT"\nnext\nend\nconfig firewall service custom\n')

def line():
    print("-"*150)

line()
print('FortiGate Service Creation type "end" to quit the program: ')
line()

while True:
    with open('port_list.csv', 'r') as services:
        services_reader = csv.DictReader(services)
        user_search = str(input("Port Number: "))
        if user_search.isdigit():
            line()
            search_results = []
            row_num = 1
            for row in services_reader:
                row_results = {}
                if user_search in row['Port Number'] and len(user_search) == len(row['Port Number']):
                    print(f'[{row_num}] - Port:{row["Port Number"]}/{row["Transport Protocol"].upper()} - {row["Service Name"].upper()}')
                    row_results.update({"ROW": row_num, "PORT": row['Port Number'],"PROTOCOL": row["Transport Protocol"], "SERVICE": row['Service Name'].upper(), "DESCRIPTION": row['Description']})
                    search_results.append(row_results)
                    row_num += 1
            line()

            user_selection = str(input("Enter Selection: "))
            numbers = [int(i) for i in user_selection]
            num_output = []
            for number in numbers:
                for result in search_results:
                    if int(number) in result.values():
                        finished_file.write(f'edit "{result["SERVICE"]}_{result["PROTOCOL"].upper()}"\n')
                        finished_file.write(f'set category "CUSTOMGRP"\n')
                        finished_file.write(f'set {result["PROTOCOL"]}-portrange {result["PORT"]}\n')
                        finished_file.write(f'set comment "{result["DESCRIPTION"].upper()}"\n')
                        finished_file.write(f'next\n')
                        num_output.append(number)
            print(str(num_output)+" added to output file.")
            line()
        elif user_search.upper() == "END":
            break


services.close()
finished_file.write("end\n")
finished_file.close()



