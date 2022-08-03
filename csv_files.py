# >>> Working with CSV files
#reads excel sheet
from csv import DictReader

#ordered_list

with open("new_file.csv","r") as rf:
    csv_reader = DictReader(rf,delimiter=",")
    for row in csv_reader:
        print (row)    #order dict

with open("new_file.csv","r") as rf:
    csv_reader = DictReader(rf,delimiter=",")
    for row in csv_reader:
        print (row["name"])   #for name from csv file ko sheet

#>>>.for writing csv files>>>>

# ---------> FOR WRITING CSV FILE   <-----------
from csv import DictWriter
# newline="" --> to remove space
with open("file2.csv","w",newline="") as wf:   #creates file 
    csv_writer = DictWriter(wf,fieldnames=["name","contact","address","dob"])
    csv_writer.writeheader()
    csv_writer.writerow(
        {"name":"Ram","contact":98564,"address":"ktm","dob":"7 Sept"}
        )
    csv_writer.writerow(
        {"name":"Kiran","contact":12345,"address":"btl","dob":"8 Aug"}
        )
    
    csv_writer.writerows([
        {"name":"dkasdk","contact":12345,"address":"btl","dob":"8 Aug"},
        {"name":"sdansran","contact":12345,"address":"btl","dob":"8 Aug"}
        ])