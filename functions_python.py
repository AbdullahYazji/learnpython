def cub(num):
    return num*num*num


print(cub(3))


def cub(num):
    return num*num*num


result = cub(4)
print(result)


def sum(num1, num2):
     return num1+num2


print(sum(4, 4))

# ___________________________________________________________________________________

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3


print(max_num(2, 5, 10))

# ______________________________________________

def match_string(str1, str2):
    if str1 == str2:
        print("the strings do match")
    else:
        print("the strings do not match")
match_string("codezilla", "codezilla")

