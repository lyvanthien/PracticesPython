
try:
    with open('folder/test.txt') as file:
        print(file.read())
except  FileNotFoundError:
    print("That file was not found :(")
# print(file.close())