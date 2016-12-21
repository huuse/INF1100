#exam_2011.py


"""
1)
2
1, 0
3
2, 1
"""
# for i in range(2,4):
# 	print i
# 	for j in range(i-1, i+1):
# 		for k in range(j-1, j):
# 			if i != j:
# 				print j,k

"""
2)
"""
# import random
# elements = [1,4,67,3,-4,23,199,0,3,'hei']
# print elements
# i = random.randint(0,len(elements)-1)
# print i
# del elements[i]
# print elements

"""
3)
"""
# colors = {'red':3,'yellow':1,'purple':2}
# def dict2list(colors):

	
	# lstcol =list(colors)
	# lst = []
	# for i in range(len(colors)):
	# 	for j in range(colors[lstcol[i]]):
	# 		lst.append(lstcol[i])
	# return lst
# 	lst = []
# 	print colors
# 	for color in colors:
# 		print color
# 		for i in range(colors[color]):
# 			lst.append(color)
# 	return lst

# print dict2list(colors)


"""
4)
"""




# import numpy as np
# import random
# N=10000
# flip = 2
# ar = np.zeros((N,flip))
# for i in range(N):
# 	for j in range(flip):
# 		ar[i][j] = random.randint(0,1)
# sums = np.sum(ar, axis=1)
# wins = 0
# for i in range(0,len(sums)):
# 	if sums[i] ==1.0:
# 		wins += 1
# p = wins/float(N)
# print p

# new = 0
# for e in range(N):
# 	c1 = random.randint(0,1)
# 	c2 = random.randint(0,1)
# 	if c1 != c2:
# 		new +=1
# print float(new)/N



"""
5)
"""
# import sys
# import numpy as np
# import random
# import matplotlib.pyplot as plt


# def carlo(n,N):
# 	lst = np.zeros((N,n))
# 	print 
# 	wins = 0
# 	for i in range(N):
# 		for j in range(n):
# 			lst[i][j] = random.randint(0,1)
# 	sums = np.sum(lst, axis = 1)
# 	for i in range(N):
# 		if sums[i]>=2*n/3:
# 			wins += 1
# 	return wins/float(N)

# n = np.array([3, 6, 9, 12, 15])
# try:
# 	N = int(sys.argv[1])
# except IndexError:
# 	print 'Give N on the command line'
# 	sys.exit(1)



# prob = [carlo(nn,N) for nn in n]


# plt.plot(prob,n,'ro')
# plt.title('%.f' %N)
# plt.show()


"""
6)
"""
# import random
# import numpy as np
# colors = {'red':8, 'yellow':2, 'green':6, 'black':9}
# success = 0
# N = 100
# nn = []
# for color in colors:
# 	nn.append(colors[color])
# nsum = sum(nn)
# lst = list(colors)
# for m in range(N):
# 	n = []
# 	count = 0
# 	while count<4:
# 		temp = random.randint(0,nsum-1)
# 		if temp not in n:

# 			n.append(temp)
# 			count+=1

# 	out = []
# 	print n
# 	print lst
# 	for i in range(0,4):
# 		if n[i]<=8:
# 			f = 0
# 		elif n[i]<=14:
# 			f =1
# 		elif n[i]<=16:
# 			f = 2
# 		elif n[i]<=24:
# 			f=3
# 		out.append(lst[f])
# 	print out
# 	if 'yellow' in out and 'red' in out:
# 		print 'success'
# 		success += 1
# p = success/float(N) 
# print p	




"""
7)
"""

"""
8)
"""


# def ex8(filename):

# 	infile = open(filename, 'r')
# 	x = []
# 	y =[]
# 	xs = 2
# 	ys = 15	
# 	for line in infile:
# 		if line[0] =='#':
# 			continue
# 		else:
# 			x.append(float(line[xs:xs+8]))
# 			y.append(float(line[ys:ys+8]))
# 	return x,y
# print ex8('ex8_exam2011.txt')






















