mat = [[0 for i in xrange(1000)]for x in xrange(1000)]
def toggle(mat,x1,y1,x2,y2):
    x = x1
    y = y1
    while (x<=x2):
        y = y1
        while(y<=y2):
            mat[x][y]= mat[x][y]+2
            y+=1
        x+=1
    return mat
def turn_off(mat,x1,y1,x2,y2):
    x = x1
    y = y1
    while (x<=x2):
        y = y1
        while(y<=y2):
            mat[x][y]= mat[x][y]-1
            if mat[x][y]<0:
                mat[x][y] = 0
            y+=1
        x+=1
    return mat
def turn_on(mat,x1,y1,x2,y2):
    x = x1
    y = y1
    while (x<=x2):
        y = y1
        while(y<=y2):
            mat[x][y]= mat[x][y]+1
            y+=1
        x+=1
    return mat
    

with open('input.txt') as f:
    lines = f.readlines()
    lines = [x.strip() for x in lines] 
    for a in lines:
        a = a.split()
        if a[0] == 'toggle':
            [x1,y1] = map(int,a[1].split(','))
            [x2,y2] = map(int,a[3].split(','))
            mat = toggle(mat,x1,y1,x2,y2)
        elif a[1] == 'on':
            [x1,y1] = map(int,a[2].split(','))
            [x2,y2] = map(int,a[4].split(','))
            mat = turn_on(mat,x1,y1,x2,y2)
        elif a[1] == 'off':
            [x1,y1] = map(int,a[2].split(','))
            [x2,y2] = map(int,a[4].split(','))
            mat = turn_off(mat,x1,y1,x2,y2)
    count = 0 
    for i in xrange(1000):
        for j in xrange(1000):
            count +=mat[i][j]
    print count           
