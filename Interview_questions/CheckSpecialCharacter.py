import re

# str ="da2abjh@bfjbsad:'[;'']ASDJBAD"
str="abcd"
regex =re.compile("@#$%^&*():;<>,./\|")
print("No special Character" if regex.search(str)=="None" else "String Contain spacial character")
# if (regex.search(str)=="None"):
#     print("No special Character")
# else:
#     print("String Contain spacial character")