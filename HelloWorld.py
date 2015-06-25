import sys

def repeat(s, exclaim):
	"""
	Documentation goes here.
	"""
	result = s + s + s
	if exclaim:
		result += '!!!!'
	return result

def main():
	print 'Hello there', repeat(sys.argv[1], True)
	if sys.argv[2] == str(3):
		print 'three times'
	elif sys.argv[2] == str(2):
		print 'two times'
	else:
		print 'other no times'

if __name__ == '__main__':
	main()
	