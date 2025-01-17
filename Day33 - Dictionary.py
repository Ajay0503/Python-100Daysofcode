info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info['name'])#error if not there
print(info.get('name2'))#no error if not there
print(info.keys()) 
print(info.values())

for keys in info.keys():
    print(info[keys],keys) 
    
print(info.items())
for key,values in info.items():
    print(key,values)