#initialize the dictionary with the default values 

names = ['Rahul', 'Rohan']
default2 = {"designation":"developer","Salary":80000}

d = {}
for v in names:
    d[v] = default2

# for i in range(len(names)):
#     d[names[i]] = default2

# print(dict.fromkeys(names,[1,2]))



# print(dict(hero=2,rahul=32))


for v in d.keys():
    d[v]['post'] = d[v]['designation']
    del d[v]['designation']
    # print(d[v]['designation'])
    # print(v)

print(d)