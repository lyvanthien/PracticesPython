# str.format() = optional method that gives users
#                   more control when displaying output

number = 15
number1 = 3.14159
print("The number pi is {:.3f}".format(number1))
print("The number is {:,}".format(number))
print("The number is {:b}".format(number))
print("The number is {:o}".format(number))
print("The number is {:X}".format(number))
print("The number is {:E}".format(number))

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format(animal,item))
# print("The {0} jumped over the {1}".format(animal,item))    # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument
# print("The {item} jumped over the {animal}".format(animal="cow",item="moon")) #keyword argument

text = "The {} jumped over the {}"
print(text.format(animal,item))

name = "Thien"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name))
print("Hello, my name is {:5}. Nice to meet you".format(name))
print("Hello, my name is {:<10}. Nice to meet you".format(name))
print("Hello, my name is {:>10}. Nice to meet you".format(name))
print("Hello, my name is {:^10}. Nice to meet you".format(name))




