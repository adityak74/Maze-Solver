import random
import MySQLdb
xx,yy=0,0
choice=0
start,dest=0,0
grid=[]
def usermaze(usermaze):
	print("the followinf maze will now be entered into database\n");
	print usermaze
	row1,row2,row3,row4,dest=usermaze[0],usermaze[1],usermaze[2],usermaze[3],usermaze[4]
	db = MySQLdb.connect(host="localhost",port=80,user="root",passwd="",db="maze" )
	cursor = db.cursor()
	sql = "insert into etable values(%d,%d,%d,%d,%d)"%(row1,row2,row3,row4,dest)
	try:
   		cursor.execute(sql)
   		db.commit()
	except MySQLdb.Error, e:
		print "Failed"
		print "MySQL Error: %s" % str(e);
   		db.rollback()
   	global xx,yy,dest
	dest =usermaze.pop()
	temp=[]
	global grid 
	maxlen = 0 
	for x in usermaze: 
		temp=[int(x) for x in bin(x)[2:]] 
		maxlen = max(maxlen,len(temp)) 
	for x in usermaze: 
		temp=[int(x) for x in bin(x)[2:]] 
		if len(temp) < maxlen: 
			no_of_zeros = maxlen - len(temp) 
			for x in range(0,no_of_zeros,1): 
				usermaze = 0 
				temp = [usermaze] + temp 
		grid.append(temp)
	global xx,yy 
	xx,yy=dest/10,dest%10
	print "this is the maze enterd by the user in decimal format\n\n"
	for x in grid:
		print x;print"\n"
def inbuiltmaze():
	decimalgrid=[]
	global choice 
	choice=raw_input("ENTER \n1.LEVEL 1\n2.LEVEL2\n:")
	choice=int(choice)
	if(choice == 1):
		db = MySQLdb.connect(host="localhost",port=80,user="root",passwd="",db="maze" )
		cursor = db.cursor()
		mazeno=random.randrange(0,4)
		try:
			cursor.execute("SELECT * FROM level1 WHERE mazeno = %d" % (mazeno))
			result=cursor.fetchall()
			for row in result:
				decimalgrid.append(row)
		except:
			print "\n####error in accessing the database###\n"
		db.close()
	elif(choice == 2):
		db = MySQLdb.connect("localhost","root","","maze" )
		cursor = db.cursor()
		mazeno=random.randrange(0,4)
		try:
			cursor.execute("SELECT * FROM level2 WHERE mazeno = '%d'" % (mazeno))
			result=cursor.fetchall()
			for row in result:
				decimalgrid.append(row)
		except:
			print "\n####error in accessing the database###\n"
		db.close()
	print "\nthis is the decimal grid\n"
	decimalgrid=list(decimalgrid.pop())
	for x in range(len(decimalgrid)):
		decimalgrid[x]=int(decimalgrid[x])
	print decimalgrid
	del decimalgrid[0]
	global dest 
	dest =decimalgrid.pop()
	temp=[]
	global grid 
	maxlen = 0 
	for x in decimalgrid: 
		temp=[int(x) for x in bin(x)[2:]] 
		maxlen = max(maxlen,len(temp)) 
	for x in decimalgrid: 
		temp=[int(x) for x in bin(x)[2:]] 
		if len(temp) < maxlen: 
			no_of_zeros = maxlen - len(temp) 
			for x in range(0,no_of_zeros,1): 
				decimalgrid = 0 
				temp = [decimalgrid] + temp 
		grid.append(temp)
	global xx,yy 
	xx,yy=dest/10,dest%10
	for x in grid:
		print x;print"\n"
	

