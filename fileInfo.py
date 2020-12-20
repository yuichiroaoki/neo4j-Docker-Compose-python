from os import listdir
from os.path import isfile, join

class FileManager():
    
    def list_files(self):
        mypath = "./import"
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        print(onlyfiles)


examples = FileManager()

print(examples.list_files())
