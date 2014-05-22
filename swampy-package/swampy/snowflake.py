from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

def koch(t,x):
	if t<3:
		return
	bob=t	
	pd(t)
	fd(t,x/3)
	lt(t, 60)
	fd(t,x/3)
	rt(t,120)
	fd(t,x/3)
	lt(t,60)
	fd(t,x/3)
	lt(t, 60)
	koch(t,x-1)

bob.delay=.05

koch(bob,360)

def snowflake(t,x):
	for i in range(3):
		koch(t,x)	

snowflake(bob, 12)