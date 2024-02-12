def test(x):
    x = x + 1

x = 11
test(x)
print(x)


def test2(ls):
    ls.append(12)

l = [1,2,3]

test2(l)
print(l)