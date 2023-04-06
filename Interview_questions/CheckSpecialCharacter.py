import re

str ="da2abjh@bfjbsad:'[;'']ASDJBAD"
regex =re.compile("@#$%^&*():;<>,./\|")

if (regex.search(str)=="None"):
    print("No special Character")
else:
    print("String Contain spacial character")