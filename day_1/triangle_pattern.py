def starPattern(num):
    for i in range(0, num+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
    for i in range(num,0,-1):
        for j in range( i,0,-1):
            print(j, end=" ")
        print()
    

starPattern(5)