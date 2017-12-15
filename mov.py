import math;

def mov(x, y, angle=0):
	nx = x + math.cos(angle)
	ny = y - math.sin(angle)
	return nx, ny
		