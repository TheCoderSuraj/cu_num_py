# convert 2 list into dictionary

l1 = [1,2,3,4,5]
l2 = ["suraj","kiran","amrit","rahul","ashok"]

dict1 = {}
for k,v in zip(l1,l2):
    dict1[k] = v

print(dict1) 

# single line approach
# print(dict(zip(l1,l2)))