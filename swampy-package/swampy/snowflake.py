from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				

from koch_curve import koch

t=bob
x=360
bob.delay=.01

koch(t,x)
rt(t,120)

koch(t,x)
rt(t, 120)

koch(t,x)
rt(t,120)


# def koch(t,x):
# 	if x<3:
		
# 		return
		
# 	pd(t)
# 	fd(t,x/3)
# 	lt(t, 60)
# 	fd(t,x/3)
# 	rt(t,120)
# 	fd(t,x/3)
# 	lt(t,60)
# 	fd(t,x/3)
# 	lt(t, 60)
# 	koch(t,x-1)

# bob.delay=.05

# koch(bob,360)

# def snowflake(t,x):
# 	for i in range(3):
# 		koch(t,x)	

# snowflake(bob, 12)