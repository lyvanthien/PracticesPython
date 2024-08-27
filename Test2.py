# **kwargs = parameter that will pack all armuments into a  dictionary
#            useful so that a function can accept a varying amount of keyword armuments

def hello(first, last):
    print("Hello " + first+ " "+ last)

hello(first="Ly", last="Thien")
# hello(first="Ly", middle="Van", last="Thien")  # Error

def hello1(**kwargs):
    #print("Hello "+ kwargs['first']+ " "+kwargs['last'] )
    print("Hello1", end=" ")
    for key,value in kwargs.items():
        print(value,end=" ")

#hello1(first="Ly", middle="Van", last="Thien")
hello1(title = "Mr.",first="Ly", middle="Van", last="Thien")
