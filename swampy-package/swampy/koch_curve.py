from TurtleWorld import * 					

def koch(t,x):
	print x
	if x < 3:
		fd(t,x)	
		return
	pd
	
	koch(t,x/3)
	lt(t, 60)
	koch(t,x/3)
	rt(t,120)
	koch(t,x/3)
	lt(t,60)
	koch(t,x/3)
	


if __name__=='__main__':
	world = TurtleWorld()			
	bob = Turtle()	
	bob.delay=.01
	koch(bob, 450)
	wait_for_user()












