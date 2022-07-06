import datetime
import os


#path = "C:\\Users\\riypat\\Documents\\Work\\Exercises\\Test\\"
path = input("Enter directory path: ")

def bulkRename(path):
    dir_list = os.listdir(path)

    now = datetime.datetime.now()

    for i in dir_list:
        stringTime = str(now) + i
        stringTime = stringTime.replace(":","-")
        stringTime = path + stringTime
        os.rename(path+i, stringTime)
    print(os.listdir(path))

bulkRename(path)