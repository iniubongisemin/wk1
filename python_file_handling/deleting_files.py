import os

# Delete files 
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist!!!")

# Delete folder
os.rmdir("empty_folder")