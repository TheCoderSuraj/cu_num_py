# number of characters in string
# number of repeated characters

def countCharacter(value):
    # cnt = 0
    ref = []
    for c in value:
        if c not in ref:
            # cnt += 1
            ref.append(c)
    # return cnt
    return len(ref)

def countDuplicateCharacter(value):
    # cnt = 0
    ref = []
    cop = []
    for c in value:
        if c not in ref:
            ref.append(c)
        elif (c in ref) and not (c in cop):
            cop.append(c)
            # cnt += 1
    # return cnt
    return len(cop)

v1 = "google.com"
v2 = "22BCS120112"

print(f"No of characters in {v1} is {countCharacter(v1)}")
print(f"No of duplicate characters in {v1} is {countDuplicateCharacter(v1)}")
print(f"No of characters in {v2} is {countCharacter(v2)}")
print(f"No of duplicate characters in {v2} is {countDuplicateCharacter(v2)}")

# v = input("enter string")
# print(f"No of characters in {v} is {countCharacter(v)}")
# print(f"No of duplicate characters in {v} is {countDuplicateCharacter(v)}")
