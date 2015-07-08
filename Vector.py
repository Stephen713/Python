from numbers import Number

class Vector:
	""" 2D vector class """
	def __init__(self, x = None, y = None):
		if x is None:
			self.X = 0.0
		else:
			self.X = x
		if y is None:
			self.Y = 0.0
		else:
			self.Y = y
			
	def __eq__(self, other):		# self == other
		return self.X == other.X and self.Y == other.Y
		
	def __ne__(self, other):		# self != other
		return not self == other
		
	def __add__(self, other):		# self + other
		if isinstance(other, self.__class__):
			return Vector(self.X + other.X, self.Y + other.Y)
		elif isinstance(other, Number):
			return Vector(self.X + other, self.Y + other)
		else:
			raise TypeError("bad types for +: '{}' and '{}'".format(self.__class__, other.__class__))
		
	def __sub__(self, other):		# self - other
		pass
		
	def __mul__(self, other):		# self * other
		pass
		
	def __div__(self, other):		# self / other
		pass
		
	def __neg__(self):				# -self
		pass
		
	def __abs__(self):				# abs(self)
		return Vector(abs(self.X), abs(self.Y))
		
	def __iadd__(self, other):		# self += other
		if isinstance(other, self.__class__):
			self.X += other.X
			self.Y += other.Y
		elif isinstance(other, Number):
			self.X += other
			self.Y += other
		else:
			raise TypeError("unsupported operand types for +=: '{}' and '{}'".format(self.__class__, other.__class__))
		return self
		
	def __isub__(self, other):		# self -= other
		pass
		
	def __imul__(self, other):		# self *= other
		pass
		
	def __idiv__(self, other):		# self /= other
		pass
		
	def __str__(self):
		return '(' + str(self.X) + ', ' + str(self.Y) + ')'
		
def main():
	#print("in main() the value of __name__ is : " + __name__)
	v = Vector(2, 3)
	u = Vector()
	w = Vector(-2.0, -7.3)
	o = Vector(1, 1)
	
	print(w, abs(w))
	
	w += o
	print(w)
	w += 1
	print(w)
	#w += str("abc")
	print(w)
	
	print('v == u  --  ' + str(v == u))
	print('v != u  --  ' + str(v != u))
	print('v == v  --  ' + str(v == v))
	print('v != v  --  ' + str(v != v))
	
if __name__ == '__main__':
	main()	
