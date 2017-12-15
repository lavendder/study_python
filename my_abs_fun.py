import math;

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('error params type')
	 if not isinstance(x, (int, float)):
	if x >= 0:
		return x
	else:
		return -x

def mov(x, y, angle=0):
	nx = x + math.cos(angle)
	ny = y - math.sin(angle)
	return nx, ny
		