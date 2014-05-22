def is_triangle(x,y,z):
	"""Determines whether you can or cannot form a triangle with three side lengths and prints "Yes" or "No" depending on whether you can or cannot form a triangle."""	
	if x+y<z:
		print 'No'
	elif x+z<y:
		print 'No'
	elif y+z<x:
		print 'No'

	else:
		print 'Yes'


is_triangle(4,8,12)
is_triangle(3,17,41)