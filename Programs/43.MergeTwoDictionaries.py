dict1 = {"lisa":80,"sita":99 }
dict2 = {"sita":94,"peter":74}
print(dict1|dict2)

print({**dict1,**dict2})
dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)