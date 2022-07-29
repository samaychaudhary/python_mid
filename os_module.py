#>>>> OS MODULE>>

import os

print (os.getcwd())     #cwd is current work directory
path = r"/Users/samaychaudhary/Desktop/python_training2"    # r is raw string

#os.mkdir ("any")      #making folder named any
#os.rmdir ("any2")
#os.rmdir ("any")


print(os.path.exists("any2"))         #checking whether it exists or not

"""if os.path.exists("any5"):
    print ("already exists")
else:
    os.mkdir("any3")"""

#open or make new file....
#open("file.txt","a").close() #a>>>append mode     #if file exists it opens otherwise creates. 
#open("file.docx","a").close() 
#open("file.png","a").close() 


list_dir_path = r"/Users/samaychaudhary/Desktop/python_training2/any3"     
print(os.listdir(list_dir_path))      #seeing whats there inside any3.. that is output

#change directory
change_dir_path = r"/Users/samaychaudhary/Desktop/python_training2/any3"

os.chdir(change_dir_path)  #changing to any3
print (os.getcwd())   #seeing where are we
os.chdir(path)   #changing to path
print (os.getcwd())


#to find the path of files:

for item in os.listdir():
    file_path = os.path.join(os.getcwd(),item)
    print (f"the path of this item file {item} is :>>> {file_path}")
    print (f"any")

#to walk in path of files











# SHUTIL

import shutil
# print(os.getcwd())

# os.rmdir("any3")    #if there is file inside folder this thing cannot delete folder

# shutil.rmtree("any3")  #permanently delete      #rmtree- remove tree

# any3_path = path + "/any3"                 #any3 lai copy garera any2 ma rakheko
# copy_garne_path = path + "/any2/any3"
# shutil.copytree(path, copy_garne_path)

# file_path = path + "/file.txt"
# copy_garne_path = path + "/any2/file.txt"      # file.txt lai any2 ma rakheko
# shutil.copy(file_path,copy_garne_path) 


move_file_path = path + "/any2/lambda_function.py"
file_ko_move_garney_path = path + "lambda_function.py"    #filepng lai any2 ma rakheko
shutil.move(file_path,file_ko_move_garney_path)   #tree na lekhne as file ho



