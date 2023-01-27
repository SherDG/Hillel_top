import re

text = 'geeks for geeks. Mytext is awesome 545346346'

result = re.search(r"\d{9}", text)
print(result)


# without using

# match = re.search(r'.', s)
# print(match)

# match = re.search(r'for', text)
# print(match)

# using \
# match = re.search(r'\.', s)
# print(match)