def findMax(ls):
    maxVal = 0
    for l in ls:
        if maxVal < l:
            maxVal = l
    return maxVal

def findMin(ls):
    minVal = ls[0]
    for l in ls:
        if minVal > l:
            minVal = l
    return minVal

ln = int(input("Enter length of lis"))
ls = []
for i in range(0,ln):
    ls.append(float(input(f'Enter {i}th element: ')))

print(f"min value is {findMin(ls)}")
print(f"max value is {findMax(ls)}")