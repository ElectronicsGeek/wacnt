# CAUTION:
# This program runs really slowly!

def fib(n):
	"""Calculates the nth fibbonaci number. NOTE: Uses index counting"""
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

fib_count = 0
n = 0
total = 0

# Repeat this loop until we have found the 10 fibonacci numbers that
# begin with 6 or 7		
while fib_count != 10:
	f = fib(n)
	
	# Look at the first digit of the number
	if str(f)[0] == "6" or str(f)[0] == "7":
		total += f
		fib_count += 1
		
	n += 1

print "TOTAL = " + str(total)
