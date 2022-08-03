# >>>>>advance min() and max() function<<<<<

def any_fun(name):
    return len(name)   #this function euta euta name lincha ani length dincha

names = ["apple","joy","om","ram kumar"]
names2 = [1,2,3,4,5,6,7,8,9]
print (max(names,key=any_fun))       #gives the name which has most letters as len is given in function.
print (max(names2))

#using lambda
print (max(names,key=lambda name:len(name)))


#1) find the name of highest marks

student1 = [                                 #[{},{},{}]
    {"name":"Ram","score":60,"age":19},
{"name":"kiran","score":70,"age":20},
{"name":"om","score":80,"age":21}
]

student2 = {"Ram":{"score":60,"age":19},      #dictionaries of dictionaries
"kiran":{"score":70,"age":20},
"om":{"score":80,"age":21}}

"""def topper(name):
    max_value = 0
    all_values = []
    for item in name:
        for key,value in item.items():
            all_values.append(value[0])
            print(all_values)
print(topper(student1))
"""


names = ["apple","joy","om","ram kumar"]
names2 = [1,2,3,4,5,6,7,8,9]

#sort method
# name1.sort()
# print name1

#but 


#1) find the sorted accordimg to highest marks:

student1 = [                                 #[{},{},{}]
    {"name":"Ram","score":60,"age":19},
{"name":"kiran","score":70,"age":20},
{"name":"om","score":80,"age":21}
]

sorted_list = sorted(student1, key=lambda item:item.get("name"))
print (sorted_list)


sorted_list = sorted(student1, key=lambda item:item.get("score"),reverse = True)
print (sorted_list)

sorted_list = sorted(student1, key=lambda item:item.get("score"))
print (sorted_list)


# doc function done..

