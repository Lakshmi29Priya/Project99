import os
import shutil
import time
path=input("Enter the name of the folder")
days=input("Enter number of days")
days=time.time()

list_of_files=os.listdir(path)
for file in list_of_files:
    f = os.path.join(path, list_of_files)
    ctime=os.stat(path).st_ctime
    if ctime>days:
        os.remove(path)
    else:
        shutil.rmtree()