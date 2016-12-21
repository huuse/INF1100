#sum_func.py


			#a

def  sum_1k(M) :				#defining the function
	sum_1k = 0 					#defining the sum_1k
	for k in range(1,M+1):		#for loop going through M k-values starting at 1
		sum_1k += 1.0/k 		#filling 1/k into the sum_1k in each loop


	return sum_1k 				#defining the return value as sum_1k

test = sum_1k(4)
print test


			#b




def test_sum_1k(m):
	t = sum_1k(m)

	s = 1.0/1 + 1/2.0 + 1/3.0
	print 'test_sum_1k = ', t
	print 's = ', s
	tot = 10**(-17)
	if abs(t - s) >tot:

		return  'sum_1k is not working correctly'
	else:
		return 'sum_1k is working correctly'

	print 'test_sum_1k', t
	print s

print test_sum_1k(3)


