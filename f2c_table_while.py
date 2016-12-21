#f2c_table_while.py

f = 0
while f <= 100:
	c = f*5.0/9-32
	#print '%.2f %.2f' %(f,c)
	print f , round(c,2)
	f +=10