# languages = ["c_sharp", "html", "python", "java"]
# print(languages)
# print(languages[0])
# print(languages[0:2])
# print(languages[2:4])
# print(languages[0:])
# languages[1] = "css"
# print(languages[1])
# print(languages[0:4])
# _______________________________________________________________
languages = ["c_sharp", "html", "python", "java"]
apk = ["pycharm", "VSCode", "GitHub"]
print(languages, apk)
print(languages.index("html"))
# languages.extend(apk)
# print(languages)
languages += apk
print(languages)
languages.append("css")
print(languages)
languages.insert(0, "javascript")
print(languages)
languages.remove("html")
print(languages)
languages.clear()
print(languages)
numbers = [33, 495, 56, 928]
numbers.pop()
print(numbers)
