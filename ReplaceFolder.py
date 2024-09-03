import os

source = "folder"
destination = "C:\\Users\\thien\\Desktop\\folder"

try:
    if os.path.exists(destination):
        print("There is already a folder there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
