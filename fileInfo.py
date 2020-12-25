from os import listdir
from os.path import isfile, join, isdir, splitext
from pathlib import Path

class FileManager():

    def check_second_extension(self, file, second_extension):
        try:
            if Path(file).suffixes[-2] == '.' + second_extension:
                return True
        except IndexError:
            pass
        except Exception as e:
            raise e
        
    def list_files(self, folder_name, file_type):
        folderPath = "./data/" + folder_name
        onlyfiles = [f for f in listdir(folderPath) if isfile(join(folderPath, f))]
        filteredFiles = [f for f in onlyfiles if self.check_second_extension(f, file_type)]
        return filteredFiles

    def list_folders(self, folder_name):
        folderPath = "./data/" + folder_name
        onlyfolders = [f for f in listdir(folderPath) if isdir(join(folderPath, f))]
        return onlyfolders


file_name = 'my_file.cjs.json'
extensions = Path(file_name).suffixes[-2]
print(extensions)
examples = FileManager()

print(examples.list_files("", "cjs"))
