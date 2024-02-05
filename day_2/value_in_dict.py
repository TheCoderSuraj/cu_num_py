d1 ={'ten':10,"twenty":20,"thirty":30,"forty":40,'fifty':50}

target = 20
def check(dictionary, target):
    for v in dictionary.values():
        if target == v:
            return True
    return False

print(check(d1,32))

