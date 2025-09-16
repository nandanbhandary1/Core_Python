# import re

# text = "Python is a programming language. Python is easy to learn. Python is powerful."


# # regex = r"Python"
# regex = r"is"
# r1 = re.match(regex, text)
# # print(r1)

# print("Match:", r1)  # Match: None, because it doesn't match the start of the string

# import re

# text = "Python is super super super programming language "
# regex = r"super"
# r1 = re.search(regex, text)
# print(r1)


# import re

# text = "Python is super super super programming language "
# regex = r"super"
# r1 = re.findall(regex, text)
# print(r1)


# import re

# text = "Python is super super super easy"
# regex = r"."
# r1 = re.findall(regex, text)
# print(r1)


# import re

# text = "Python. is super super super easy."
# regex = r"\."
# r1 = re.findall(regex, text)
# print(r1)


# import re

# text = "Python is super super super easy."
# regex = r"is|super"
# r1 = re.findall(regex, text)
# print(r1)


# import re  # (0 - inf)

# text = "A python is ython not pppython and ppppppython."
# regex = r"p*ython"
# r1 = re.findall(regex, text)
# print(r1)


# import re  # (1 - inf)

# text = "A python is ython not pppython and ppppppython."
# regex = r"p+ython"
# r1 = re.findall(regex, text)
# print(r1)


# import re  # (0 - 1)

# text = "A python is ython not pppython and ppppppython."
# regex = r"p?ython"
# r1 = re.findall(regex, text)
# print(r1)


# import re  # (0 - 1) IT GIVES FIRST SUBSTR OF THE TEXT

# text = "A python is ython not pppython and ppppppython."
# regex = r"^A"
# r1 = re.findall(regex, text)
# print(r1)


# import re  # IT GIVES LAST SUBSTR OF THE TEXT

# text = "A python is ython not pppython and ppppppython."
# regex = r"ppppppython.$"
# r1 = re.findall(regex, text)
# print(r1)


# import re  # IT GIVES INDIVIDUAL CHAR FROM MAIN STR

# text = "A python is ython not pppython and ppppppython."
# regex = r"[p]"
# r1 = re.findall(regex, text)
# print(r1)
# print(len(r1))


# import re  # p should present min 2 times max 3 times min and max if nothing then it's infi p{0,3}, p{1,}

# text = "A python is ython not pppython and ppppppython."
# regex = r"p{2,3}ython"
# r1 = re.findall(regex, text)
# print(r1)
# print(len(r1))
