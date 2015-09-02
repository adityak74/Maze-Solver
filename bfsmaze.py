import time
import graphics
ans=[]
def astar(m,startp,endp,choice):
    if(choice==1):
    	w,h = 4,4
    else:
    	w,h=6,6
    sx,sy = startp
    ex,ey = endp
    #[parent node, x, y,g,f]
    node = [None,sx,sy,0,abs(ex-sx)+abs(ey-sy)] 
    closeList = [node]
    createdList = {}
    createdList[sy*w+sx] = node
    k=0
    while(closeList):
        node = closeList.pop(0)
        x = node[1]
        y = node[2]
        l = node[3]+1
        k+=1
        if k&1:
            neighbours = ((x,y+1),(x,y-1),(x+1,y),(x-1,y))
        else:
            neighbours = ((x+1,y),(x-1,y),(x,y+1),(x,y-1))
        for nx,ny in neighbours:
            if nx==ex and ny==ey:
                path = [(ex,ey)]
                while node:
                    path.append((node[1],node[2]))
                    node = node[0]
                return list(reversed(path))            
            if 0<=nx<w and 0<=ny<h and m[ny][nx]==0:
                if ny*w+nx not in createdList:
                    nn = (node,nx,ny,l,l+abs(nx-ex)+abs(ny-ey))
                    createdList[ny*w+nx] = nn
                    #adding to closelist ,using binary heap
                    nni = len(closeList)
                    closeList.append(nn)
                    while nni:
                        i = (nni-1)>>1
                        if closeList[i][4]>nn[4]:
                            closeList[i],closeList[nni] = nn,closeList[i]
                            nni = i
                        else:
                            break
    return 'not found'
def bfssolution(m,start,end,choice):
	result = astar(m,(start/10,start%10),(end/10,end%10),choice)
	print result
	cm = [list(x[:]) for x in m]
	if isinstance(result, list):
	    for y in range(len(m)):
	        my = m[y]
        	for x in range(len(my)):
        	    for px,py in result:
        	        if px==x and py ==y:
        	            cm[y][x] = '*'
        	            a=str(x)+str(y)
        	            ans.append(a)
	for my in cm:
    		print(' '.join([str(x) for x in my]))
	print ans
    		
