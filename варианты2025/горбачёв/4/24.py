import re
s = open("24.txt").read()
number = r"([1-9][0-9]+|[0-9])"
pattern = rf"{number}([+*]{number})*"
b = [len(i.group()) for i in re.finditer(pattern, s)]
print(max(b))