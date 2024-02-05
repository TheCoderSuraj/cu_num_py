d1 ={'ten':10,"twenty":20,"thirty":30,"forty":40,'fifty':50}

old_key = "ten"
new_key = "Hundred"
old_value = 10
new_value = 100

def get_key(dic, tar):
    for (k,v) in dic.items():
        if v == tar:
            return k
        
d1[new_key] = d1.pop(old_key)


d1[get_key(d1,old_value)] = new_value

print(d1)