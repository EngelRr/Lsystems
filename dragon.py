import turtle
import random

#Initialize turtle to create screen
s = turtle.Turtle()
s.ht()

#Initialize drawing turtle
t = turtle.Turtle()

#regels voor dragon
#word is de lfr+- die je er in stopt
#depth is hoeveel lager je dieper wilt gaan
def dragon(word, depth):
	new_word = []
	i = 0
	
	#waar vervang je elke letter me
	replace_l = ["l","+","r","F","+"]
	replace_r = ["-","F","l","-","r"]
	
	#Initieal word voor deze functie
	# *** zou ik moeten gebruiken ipv hem er handmatig in te voeren
	ruleF_word = "Fl"
	ruleF = list(ruleF_word)
	
	#hier worden de letters vervangen
	while i<len(word):
		if (word[i] == "l"):
			new_word.extend(replace_l)
		elif (word[i] == "r"):
			new_word.extend(replace_r)
		else:
			new_word.extend(word[i])
		i += 1
	
	#recursion
	if depth>0:
		word = dragon(new_word, depth-1)
		
	return word

#Bepaalt hoe er getekend moet worden
def draw(rule, depth):
	i = 0
	
	#hoever stapt de turtle naar voren
	step = 800/(depth**(2.2))
	
	#Regels voor elke letter
	while i<len(rule):
		if (rule[i] == "+"):
			t.left(90)
		elif (rule[i] == "-"):
			t.right(90)
		elif (rule[i] == "F"):
			t.forward(step)
		i += 1
		
#FUnctie maakt uiteindelijke draw word korter, dit versneld tekenen met
#de turtle
def shorten(rule):
	i = 0
	shortrule = []
	while i<len(rule)-1:
		shortrule.extend(rule[i])
		if(shortrule[-1] == "r" or shortrule[-1] == "l"):
			shortrule.pop()
		if(len(shortrule) > 1):
			if((shortrule[-1] == "+" and shortrule[-2] == "-") or (shortrule[-1] == "-" and shortrule[-2] == "+")):
				shortrule.pop()
				shortrule.pop()
		else:
			pass

		i += 1
				
	return shortrule
		

#initial word handmatig ingevoerd
initial_word = "Fl"
initial = list(initial_word)

#depth die gebruikt word
depth = 12


#print(dragon(initial_word, depth))
#print(shorten(dragon(initial_word, depth)))

#Verwijdert tracer zodat je de animatie niet hoeft te zien
turtle.tracer(0)
draw(shorten(dragon(initial_word, depth)), depth)

#Keep screen open
s.screen.mainloop()
