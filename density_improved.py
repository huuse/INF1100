#density_improved.py





#a
print 'a)'
def mk_density_split(filename):
	infile = open(filename,'r')

	infile.readline()
	infile.readline()
	densities = {}
	for line in infile:
		words = line.split()
		subs = ' '.join(words[0:-1])
		dens = words[-1]
		densities[subs]=float(dens)
	infile.close()
	return densities

densities = mk_density_split('densities.dat')


#b 12
print 'b)'

def mk_alt_density_split(filename):

	infile = open(filename,'r')

	infile.readline()
	infile.readline()


	dens_start = 12
	densities = {}
	for line in infile:
		subs = line[0:line.find('  ')]
		dens = line[dens_start:-1]
		densities[subs]=float(dens)
	infile.close()
	return densities

densities_alt = mk_alt_density_split('densities.dat')


#c
print 'c)'


def mk_test_density():
	densities1=mk_density_split('densities.dat')
	densities2=mk_alt_density_split('densities.dat')
	expect = len(densities1)
	computed = 0
	for line in densities1:
		if densities1[line] == densities2[line]:
			computed +=1

	success = expect == computed
	msg = 'Only %d out of %d gave the same results for \n\
the two functions' %(computed,expect)
	assert success, msg

mk_test_density()










