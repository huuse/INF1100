#machine_zero.py

eps = 1.0							#defining a variable

while 1.0 != 1.0 + eps:				# creating a while loop that will continue until eps is lim zero
  print '...............', eps		#printing out the "eps" value for each loop
  eps = eps/2.0						#modifying "eps" so that it is 0.5 times its size since the last loop
print 'final eps:', eps 			#after the while loop the final value for "eps" is printed


									#zero is defined as a number smaller than ≈10^(-16)
