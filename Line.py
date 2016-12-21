#Line.py


class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		self.a = (self.p2[1] - self.p1[1])/float(self.p2[0] - self.p1[0])
		self.b = self.p1[1] - self.a*self.p1[0]

	def value(self, x):
		return self.a*x+self.b



def test_Line():
	tol = 1e-14
	x=0.5
	expect = 0.25
	computed = Line((0,-1), (2,4)).value(x)
	assert abs(expect-computed)<tol, 'bug in Line.value, difference = %s' %abs(expect-computed)




#test Line.py

from Line import Line, test_Line
line = Line((0,-1),(2,4))

print line.value(0.5), line.value(0), line.value(1)
test_Line()


"""
python Line.py
0.25 -1.0 1.5
0.25 -1.0 1.5
"""

