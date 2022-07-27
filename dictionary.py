""" DICTIONARY
it is an unordered collection of items of any data type in the form of key: value pair 
>> because of the limiation of list:we used dictionary:
>>> which is also known as JSON array or map/hash map

ex:  firstname(a) = samay : key:valuepair
ex: days={"day1":"sunday","day2":"monday" """
 
# {"key" : "value"} >>> {"age":19}

#1) how to create dictionaries
#type 1



days = {"day1":"sunday","day2":"monday","day3":"tuesday"}
print (days)
print(type(days))

#type2

days2 = dict(day4="wednesday", day5="thursday",day6="friday")
print (days2)
print (type(days2))

"""
2) how to access data from dictionary
{'day4': 'wednesday', 'day5': 'thursday', 'day6': 'friday'}
>>>>> no indexing
>>>>>days["day1"]
>>>>>> type function"""

print(days2["day4"])      # need to write what you are looking for>>> indexing doesnt work

"""
3) which type of data can dictionary store?
>> anything (number, string, list, dictionary)"""


any_dict = {
    "f_name":"maharshi",
    "age":23,
    "fav_song":["s1","s2",11,True],
    "others" :{
        "fav_game":"football",
        "fav_programming":"python"
    }
}
print(any_dict["fav_song"][3])
print(any_dict["others"]["fav_programming"])


user = {
    "f_name":"aryama",
    "l_name":"sharma",
    "age":19,
    "fav_movie":["thor","marvel"],
    "fav_food":["pizza","chownein"],
    "lives in":"kathmandu"
}
print (user["fav_movie"][1]) #marvel aaunu paryo
print (user)

# creating empty dict and adding values to it

empty_dict = {}
print(empty_dict)
empty_dict["name"]="kritika absent"
print (empty_dict)

# in keyword (conditional and looping statement)


print (any_dict)

if "f_name" in any_dict:
    print ("present")

if "maharshi" in any_dict:        #not present aaucha because its an value pair not keyword.
    print ("present")
else:
    print ("not present")

#different methods huncha>>>> keys(),values(),items(),copy(),clear(),get()

if "maharshi" in any_dict.values():
    print ("present")
else:
    print ("not present")

for i in any_dict.items():
    print (i)

for i , j in any_dict.items():
    print (f" the key is {i} and value is {j}")   
    

any_dict2 = any_dict.copy()
print (any_dict2)

any_dict2.clear()
print (any_dict2)

"""
6) add, update, pop and popitem method in dictionary
--> days["all_days"]=["day1","day2","day3"]
--> days.update(ANOTHER_DICTIONARY) # which returned the value of pop(key)
--> days.pop("all_days") # which returned the value of pop(key)
--> days.popitem() # randomly delete one item and returned the value of pop(key)
"""

dict1 = {"day1" : "sunday", "day2":"monday"}
dict2 = {"day3":"wednesday", "day4":"tuesday"}

dict3 = dict1.copy()

#add value to dict3
dict3["day5"]=["nice day","rainy day"]        
dict3["all_days"]=["day1","day2","day3"]       # adding and updating. if there is the thing then updates if not then adds. like all days adds here.
print (dict3)

#update
print (dict1)
dict1.update(dict2)    #updates what is not there
print (dict1)

#pop
dict1.pop("day1")   #here no indexing in dictionary
print (dict1)

#popped items
popped_items = dict1.pop("day2")
print (popped_items)


'''
7) fromkeys, get, clear and copy method
--> days=dict.fromkeys(["day1","day2","day3"], "unknown") # can use tuple and string too
--> get method:
ex: days["apple"] --> error but days.get("day1") --> no error and result too
--> if days.get("day1"): print present else absent
ex: if None: is treated as False else True
--> days.clear() ; days.copy() ; is vs == 
'''


#fromkeys (keys,value) method

days=dict.fromkeys (["day1","day2","day3"], "unknown")             # all values will be unknown this way
print (days)

#print (days["day5"])       # error as day5 not there
print (days["day2"])     # prints unknown

print (days.get("day5"))     # prints none instead of error here
print (days.get("day2"))      # prints unknown

#finding address using in 
if "address" in any_dict:
    print ("present")
else:
    print ("not present ")


# findind adress without in and using get
if (any_dict.get("address")):
    print ("present")
else:
    print ("not present")

"""
8)more about dictionary
>> get method
ex: days["apple"]>>> error but days.get("day7","not found")>>>> no error and result too
>>>>>>>>>. get method always took last/updated value when same keys are pressnt in dictionary"""

print (days.get("day5","Sorry! your value was not found"))

user_info = {"f_name":"aryama" , "l_name":"sharma","age":30, "age":17}
print (user_info.get("age"))       # here prints 17, although there are two age but always prints last wala

# cube in dictionary
user_number = int(input("enter a number"))
def cube(any_number):
    cube_number = {}
    for i in range(0,user_number+1):
        cube_number[i]=i**3
    return cube_number

anything= cube(user_number)
print (anything)


#counting charactersgit 
user_name = input("enter your name")
def count_char(name):
    dict = {}
    for i in user_name:
        if i in name:
            dict[i]=user_name.lower().count(i)
    return (dict)
anything = count_char(user_name)
print (anything)


