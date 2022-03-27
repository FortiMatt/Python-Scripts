import csv

csv.register_dialect('skip_space', skipinitialspace=True)

file_name = "FOS_CONF.txt"

def indenter(x):
    indent = "\t"*x
    return indent


with open(file_name, 'r') as f:
    reader = csv.reader(f, delimiter=' ', dialect='skip_space')
    conf_file_name = []
    tab = 0
    for item in reader:
        # COPY AND APPENDS CONF FILE SERIAL/VERSION/BUILD NUMBER
        if item[0].startswith("#"):
            conf_file_name.append(item)
        elif item[0] == "config" and tab == 0:
            print(item)
            tab += 1
        elif item[0] == "config" and tab > 0:
            tab += 1
            print(indenter(tab), item)
        elif item[0] == "end" and tab == 1:
            print(item)
            tab = 0
        elif item[0] == "end" and tab > 1:
            tab -= 1
            print(indenter(tab), item)
        elif item[0] == "edit" and tab == 1:
            print(indenter(tab), item)
            tab += 1
        elif item[0] == "next" and tab == 2:
            tab -= 1
            print(indenter(tab), item)
        else:
            print(indenter(tab), item)
