
# text = "Yoooooooo\nThis is some text\nHave a good one!\n"
# text = "Uh oh! This text has been overwritten"
text = "Have a nice day! See ya" # append
# with open('test.txt','w') as file:
with open('folder/test.txt', 'a') as file:

    file.write(text)