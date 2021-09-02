import shutil, os
from bs4 import BeautifulSoup

baseSource = r'C:\Users\mulle\OneDrive\Documents\GitHub\NCAApicks'
baseTarget = r'C:\Users\mulle\OneDrive\Documents\GitHub\NCAApicks'
dir = os.listdir(baseSource)

for dirpath, dirnames, filenames in os.walk(baseSource):
    for f in filenames:
        dir_len = len(dirpath[len(baseSource):])
        dir_name = dirpath[len(baseSource):]
        if f[-4:] == "html":
            #os.remove(baseTarget+'\\templates\\'+f)
            shutil.copy(f,baseTarget+'\\templates')
        else:
            continue

