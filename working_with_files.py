# working with txt files

# all methods
# 1) read file
# 2) open function>> takes path
# 3)read method()
# 4) seek method() #change the position of cursor
# 5)tell method() #to find position of cursor

poem_path = r"/Users/samaychaudhary/Desktop/python_training2/python_poem.txt"

# rf = open(poem_path)
# print (rf.read())
# rf.close()
# print(rf.closed)

# rf = open(poem_path)
# # print(f"before reading, cursor position>>>{rf.tell()}")
# # print (rf.read())
# # print (f"after reading, cursor position>> {rf.tell()}")
# # print(rf.read())
# # rf.close()
# # print(rf.closed)


# rf = open(poem_path)
# print(f"before reading, cursor position>>>{rf.tell()}")
# print (rf.read())
# print (f"after reading, cursor position>> {rf.tell()}")
# print ("-----------------------------------------------------------")
# rf.seek(0)
# print(rf.read())
# rf.close()


#6) readline method()
# rf = open(poem_path)
# print (f"next line>>>{rf.readline()}",end="")   #removes space
# print (f"next line>>>{rf.readline()}",end="")
# print (f"next line>>>{rf.readline()}",end="")
# print (f"next line>>>{rf.readline()}",end="")
# rf.close()


#7) readlines method #adds all lines into one list
# rf = open(poem_path)
# all_lines = rf.readlines()
# for line in all_lines:
#     print (f"the line is >>> {line}",end="")
# print (all_lines)
# rf.close()


#use of  with block

# with open(poem_path,"r") as rf:    #default read mode>>>>> r
#     rf.read()
# print (rf.closed)      #esari automatically close bhayoooo....


#>>>>>>>>>>>>>>>>>. WRITE DATA IN FILE (w,a,r+) mode....

#1) write mode
#delete all data and write with new data by creating new file||| it override
# with open("kritika.txt","w") as wf: 
#     wf.write("hello, i am good")

#now overwritessss with this.... in the same file
# with open("kritika.txt","w") as wf: 
#     wf.write("ok i am fine")

#2) append mode
# with open("samay.txt","a") as wf: #not delete all data and write with new data in last or list  #creates new file if it is not there
#     wf.write("hello samay\n how are you")

# #echo -e "hello samay \n how are you">> samay.txt     #this in terminal and creates new file and adds your lekheko kura

# with open("samay.txt","a") as af: 
#     af.write("hello aryama")

#3) r+ mode #doesnt create file....it overrides character

# with open("file21.txt","r+") as rsf: 
#     rsf.write("write r+ mode")    #error beacuse r+ mode is read and write.. as this file doesnt exist so cannot read

# with open("samay.txt","r+") as rsf: 
#     rsf.write("write r+ mode")    #this adds in samay file...as it exist


# with open("samay.txt","r+") as rpf: 
#     rpf.seek(len(rpf.read()))    #with this last ma lekhna payoo...doesnt overwrite
#     rpf.write("last ma lekh") 

# #4) read and write
# # this overwrites and writes poem in samay.txt
# with open(poem_path,"r") as rf:
#     with open("samay.txt","w") as wf:
#         wf.write(rf.read())


#5) read love story:
# with open("love_story.txt","r") as rf:
#     print (rf.read())

#taking from samay and keeping in samaya with salary
with open("samay.txt","r") as rf:
    with open("samaya.txt","w") as wf:
        for line in rf.readlines():
            name,salary = line.split(",")
            wf.write(f"{name}'s salary is {salary}")