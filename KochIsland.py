import turtle
import random

s = turtle.getscreen()
s.tracer(0)
#s.setworldcoordinates(-1, -1, s.window_width() - 1, s.window_height() - 1)

t1 = turtle.Turtle()

# het midden van de vorm vinden zodat ik het naar het midden van het scherm kan schuiven
def center(word):
	i = 0
	deltax = 1
	deltay = 0
	x = 0
	y = 0
	fcount = 0
	xcoords = []
	ycoords = []
	maxx = 0
	maxy = 0
	minx = 0
	miny = 0
	
	while i<len(word):
		if (word[i] == "+"):
			if (deltax == 1):
				deltax = 0
				deltay = 1
			elif (deltay == 1):
				deltax = -1
				deltay = 0
			elif (deltax == -1):
				deltax = 0
				deltay = -1
			elif (deltay == -1):
				deltax = 1
				deltay = 0
		elif (word[i] == "-"):
			if (deltax == 1):
				deltax = 0
				deltay = -1
			elif (deltay == 1):
				deltax = 1
				deltay = 0
			elif (deltax == -1):
				deltax = 0
				deltay = 1
			elif (deltay == -1):
				deltax = -1
				deltay = 0
		elif (word[i] == "F"):
			fcount += 1
			x += deltax
			y += deltay
			if x>maxx:
				maxx = x
			if y>maxy:
				maxy = y
			if x<minx:
				minx = x
			if y<miny:
				miny = y
			xcoords.append(x)
			ycoords.append(y)
		i += 1

	xcenter = sum(xcoords)/fcount
	ycenter = sum(ycoords)/fcount
	return [xcenter, ycenter, maxx, maxy, minx, miny]
	
# teken de vorm volgens de regels
def draw(t, word, step):
	i = 0
	
	while i<len(word):
		if (word[i] == "+"):
			t.left(90)
		elif (word[i] == "-"):
			t.right(90)
		elif (word[i] == "F"):
			t.forward(step)
		i += 1

#regels voor Koch Island
def KochIsland(word, depth):
	new_word = []
	i = 0
	
	ruleF_word = "F+F-F-FF+F+F-F"
	ruleF = list(ruleF_word)
	
	while i<len(word):
		if(word[i] == "F"):
			new_word.extend(ruleF)
		else:
			new_word.extend(word[i])
		i += 1
	
	if depth>0:
		word = KochIsland(new_word, depth-1)
		
	return word
			
initial_word = "F+F+F+F"
initial = list(initial_word)

ruleF_word = "F+F-F-FF+F+F-F"
ruleF = list(ruleF_word)

t1.hideturtle()
depth = 6

mid = center(KochIsland(initial, depth))
print((mid[2]-mid[4]))
stepsize = (s.window_height()-20)/(mid[2]-mid[4])
t1.goto(-mid[0]*stepsize, -mid[1]*stepsize)

draw(t1, KochIsland(initial, depth), stepsize)

s.update()
t1.screen.mainloop()
