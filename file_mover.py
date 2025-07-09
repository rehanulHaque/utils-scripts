import os
import shutil
dirs = os.listdir("./")

file_extension = [".vtt", ".txt", ".srt", ".pdf"]

dumps_folder = './dumps'

def checkDumpFolderExists(dumps_folder):
    if(os.path.exists(dumps_folder)):
        print("Dumps Folder Already Exists")
    else:
        print("Making folder name dumps")
        os.mkdir(dumps_folder)

def moveFiles(file_extension):
    checkDumpFolderExists(dumps_folder)
    print("Moving Files to dumps folder")
    for dir in dirs:
        if dir == "dumps" or dir == "main.py":
            pass
        else:
            inside_dirs = os.listdir(dir)
            for file in inside_dirs:
                for ext in file_extension:
                    if(file.endswith(ext)):
                        shutil.move(dir+"/"+file, dumps_folder)
                    else:
                        pass
    print("Files Moved Done 👍")

moveFiles(file_extension)