def say_hi(name):
    print("Hello " + name)


say_hi("Abdullah")
say_hi("Ahmed")


# _______________________________________________________

def say_hi(name, age):
    print("Hello " + name + " and your age is " + age)


say_hi("Abdullah", "18")


# _______________________________________________________
def say_hi(name, age, num):
    print("hello " + name + "\n" + "your age is " + age + "\n" + num + " is your university card number")


name = input("Enter your name: ")
age = input("Enter your age: ")
num = input("Enter your university card number: ")
say_hi(name, age, num)