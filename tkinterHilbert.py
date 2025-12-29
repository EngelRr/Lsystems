import tkinter as tk
import math

def hilbert(word, depth):
	i = 0
	
	#waar word elke letter mee vervangen
	replaceA = ["+", "B", "F", "-", "A", "F", "A", "-", "F", "B", "+"]
	replaceB = ["-", "A", "F", "+", "B", "F", "B", "+", "F", "A", "-"]

	new_word = []
	
	#Hier worden de letters vervangen voor gewenst woord
	while i<len(word):
		if (word[i] == "A"):
			new_word.extend(replaceA)
		elif (word[i] == "B"):
			new_word.extend(replaceB)
		else:
			new_word.extend(word[i])
		i += 1
	
	if(depth>0):
		word = hilbert(new_word,depth-1)
		
	return word
	
def KochIsland(word, depth):
	i = 0
	
	ruleF_word = "F+F-F-FF+F+F-F"
	
	replaceF = list(ruleF_word)
	
	new_word = []
	
	while i<len(word):
		if(word[i] == "F"):
			new_word.extend(replaceF)
		else:
			new_word.extend(word[i])
		i += 1
	
	if(depth>0):
		word = KochIsland(new_word, depth-1)
		
	return word

#generate all coordinates in order where  lines should be drawn
def pointGen(rule):
	i = 0
	j = 0
	angle = 0
	length = 1
	coords = [[0],[0]]
	
	while i<len(rule):
		if (rule[i] == "+"):
		#increase angle
			angle += 90
		elif (rule[i] == "-"):
		#decrease angle
			angle -= 90
		elif (rule[i] == "F"):
		#move forward
			coords[0].append(coords[0][j]+int(math.cos(math.pi*angle/180)*length))
			coords[1].append(coords[1][j]+int(math.sin(math.pi*angle/180)*length))
			j += 1
		i += 1
	return coords

#draw lines between points, scaled for screen size
def draw(points,canvas_size, offset):
	i = 0
	
	#calculate linelenght/stepsize
	xreach = max(points[0])-min(points[0])
	yreach = max(points[1])-min(points[1])
	linelength = (canvas_size-2*offset)/xreach
	
	#calculate required translation
	xoffset = -linelength*min(points[0])
	yoffset = -linelength*min(points[1])
	
	#draw lines
	while i<len(points[1])-1:
		canvas.create_line(points[0][i]*linelength+offset+xoffset, points[1][i]*linelength+offset+yoffset, points[0][i+1]*linelength+offset+xoffset, points[1][i+1]*linelength+offset+yoffset)
		i += 1
		
#points = pointGen(hilbert("A", 3))
points = pointGen(KochIsland("F+F+F+F",3))
print(points)

########################################################################
#window creation
root = tk.Tk()
root.title('Hilbert curve')

#window dimensions
window_width = 700
window_height = 700
canvas_width = 650
canvas_height = 650
offset = 25

#get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#find the center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

#set screen size
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#Create canvas
canvas = tk.Canvas(root, width = canvas_width, height = canvas_height, bg = 'white')
canvas.pack(anchor=tk.CENTER, expand=True)

#draw lines between points
draw(points,canvas_width,offset)

root.mainloop()
