import re

text = "Python. is super super super easy."
regex = r"\."
r1 = re.findall(regex, text)
print(r1)
