import os
import shutil

from_dir="C:/Users/Sayan Chakraborty/Downloads/c102/c102"
to_dir="C:/Users/Sayan Chakraborty/Downloads/c102"

listoffiles=os.listdir(from_dir)
print(listoffiles)


for file_name in listoffiles:
    name,ext=os.path.splitext(file_name)
    print(name)
    print(ext)


    if ext=='':
        continue
    if ext in ['.gif','.png','.jpg','.jpeg','jfif']:
        path1=from_dir+'/'+file_name
        path2=to_dir+'/'+"image_files"
        path3=to_dir+'/'+"image_files"+"/"+file_name
        print(path1)
        print(path3)
        if os.path.exists(path2): 
            print("Moving " + file_name + ".....") # Move from path1 ---> 
            shutil.move(path1, path3)
        else: 
            os.makedirs(path2) 
            print("Moving " + file_name + ".....") 
            shutil.move(path1, path3)