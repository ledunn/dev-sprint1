from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

def koch(t,x):
	bob=t	
	pd(t)
	fd(t,x/3)
	lt(t, 60)
	fd(t,x/3)
	rt(t,120)
	fd(t,x/3)
	lt(t,60)
	fd(t,x/3)

	koch(t,x/3-1)


bob.delay=.05

koch(bob, 250)





