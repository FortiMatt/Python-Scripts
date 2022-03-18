import csv
import inquirer

def user_selection(x):
    bad_countries = input("Are you interested in a list of the top countries with Cybercrime? (Y/N):").upper()
    if bad_countries == "Y":
        questions = [
            inquirer.Checkbox(
                "countries_selection",
                message = "List created, add any additonal countires below or hit enter.",
                choices=x,
                default=["China", "Brazil", "Russian Federation", "Poland", "Iran (Islamic Republic of)", "India", "Nigeria", "Viet Nam", "Germany"],
            ),
        ]
    else:
        questions = [
            inquirer.Checkbox(
                "countries_selection",
                message="Make Selection(s) below via SPACEBAR",
                choices=x,
            ),
        ]
    answers = inquirer.prompt(questions)
    return(bad_countries,answers)

countries = []
search_list = []

with open("all.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        countries.append(row['name'])
        search_list.append(row)

while True:

    bad_countries, selection = user_selection(countries)

    if selection['countries_selection']:
        print(f'config firewall address')
        for country in selection["countries_selection"]:
            for row in search_list:
                if country == row['name']:
                    print(f'edit "{row["name"].upper()}"\nset type geography\nset color 6\nset country "{row["alpha-2"]}"\nset comment "MADE VIA SCRIPT"\nnext')
        print(f'end')
        if bad_countries == "Y":
            print(f'config firewall addrgrp\nedit "COUNTRIES WITH CYBERCRIME"\nset member "China" "Brazil" "Russian Federation" "Poland" "Iran (Islamic Republic of)" "India" "Nigeria" "Viet Nam" "Germany"\nset color 6\nset comment "MADE VIA SCRIPT"\nnext\nend')
        break
    else:
        print("[!] No input detected, please try again [!]")
