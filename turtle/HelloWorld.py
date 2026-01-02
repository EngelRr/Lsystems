# hoi
import turtle
import random

s = turtle.getscreen()
s.setworldcoordinates(-1, -1, s.window_width() - 1, s.window_height() - 1)
s.tracer(0)
t = turtle.Turtle()
turtle.speed(0)
# t2 = turtle.Turtle()

def change_color():
	R = random.random()
	B = random.random()
	G = random.random()
	
	t.color(R, G, B)

def hilbert(rule, depth):
	#print(rule)
	i = 0
	replaceA = ["+", "B", "F", "-", "A", "F", "A", "-", "F", "B", "+"]
	replaceB = ["-", "A", "F", "+", "B", "F", "B", "+", "F", "A", "-"]
	
	newrule = []

	while i<len(rule):
		if (rule[i] == "A"):
			newrule.extend(replaceA)
		elif (rule[i] == "B"):
			newrule.extend(replaceB)
		else:
			newrule.extend(rule[i])
		i += 1
	
	if(depth>0):
		rule = hilbert(newrule,depth-1)
		
	return rule

def draw(rule, depth):
	i = 0
	step = 800/(2**(depth)-1)
	
	while i<len(rule):
		if (rule[i] == "+"):
			t.left(90)
		elif (rule[i] == "-"):
			t.right(90)
		elif (rule[i] == "F"):
			t.forward(step)
		i += 1
		
def shorten(rule):
	i = 0
	shortrule = []
	while i<len(rule)-1:
		shortrule.extend(rule[i])
		if(shortrule[-1] == "A" or shortrule[-1] == "B"):
			shortrule.pop()
		if(len(shortrule) > 1):
			if((shortrule[-1] == "+" and shortrule[-2] == "-") or (shortrule[-1] == "-" and shortrule[-2] == "+")):
				shortrule.pop()
				shortrule.pop()
		else:
			pass

		i += 1
				
	return shortrule
	
t.hideturtle()		
depth = 1
maxi = 5
while depth < maxi:		
	t.width(maxi-depth)
	test1 = (shorten(hilbert(["A"],depth)))
	draw(test1,depth)
	t.penup()
	t.home()
	t.pendown()
	change_color()
	
	depth += 1

s.update()
s.mainloop()
