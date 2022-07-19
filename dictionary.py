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