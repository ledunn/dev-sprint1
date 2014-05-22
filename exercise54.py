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

def triangle_tester():
	"""Takes user's inputted triangle side lengths and determines whether they can or cannot form a triangle."""

	prompt='Can you make a triangle? How long is each side? How long is the first side?\n'

	x=raw_input(prompt)
	int(x)

	prompt='How long is the second side?\n'

	y=raw_input(prompt)
	int(y)

	prompt='How long is the last side?\n'

	z=raw_input(prompt)
	int(z)

	is_triangle(x,y,z)

triangle_tester()

