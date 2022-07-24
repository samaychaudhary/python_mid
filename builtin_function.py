""""""
""">>>>>>>>>>>>Enumerate functions
>>>>> we use it with for loop to track the position of our item in iterable or loop"""
"""
#0)track the position without enumerate function:

list_of_names = ["kritika", "aryama","rushav","samay"]

position = 0
for i in list_of_names:
    print(f"the name {i} is in {position} position")
    position +=1
print (position)


#this in short 
#USING ENUMERATE

for loc,name in enumerate(list_of_names):       #enumerate gives location and name of the list/tuples
    print (f"the name {name} is in {loc} position")"""


#exercise 1 >>>
# a list containing many strings name and find the position of one target string from the list. (dynamic)"""


list_of_names = ["kritika", "aryama","rushav","samay"]
def find_name(name_list,target_name):
    for position,name in enumerate(name_list):
        if name == target_name:
            print (position)
        

ok = find_name(list_of_names, "samay")
print (ok) #lol