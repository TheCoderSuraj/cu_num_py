# wap single string from given two string separated by space and swap the first two characters of each string

def mergeString(s1,s2):
    s1 = s1[1]+s1[0]+s1[2:]
    s2 = s2[1]+s2[0]+s2[2:]
    return " ".join([s1,s2])

def checkUpp(s):
    upp = 0
    for i in range(4):
        if s[i].isupper():
            upp += 1
    if upp > 1:
        return s.upper()
    return s


s1 = "sURaj is my name."
s2 = "my name is kiran."

print(mergeString(s1,s2))
print(checkUpp(s1))
print(checkUpp(s2))

