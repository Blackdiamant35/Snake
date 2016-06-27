# -*- coding:Utf8 -*-
import tkinter as tk
import random

# Fonctions de modification terrain
def createSquare(xr,yr):
	"Crée un carré référencé aux coordonnées relatives"
	global snake,x,y,length
	tag = str(xr)+'c'+str(yr) # On lui donne un tag en rapport à ses coordonnées relatives
	can.create_rectangle(xr*24+2,yr*24+2,xr*24+22,yr*24+22, fill='dark blue', width=0,tags=tag)
	snake.insert(0,[xr,yr])
	try:
		i = 1
		while i<length:
			if (snake[i][0] == x and snake[i][1] == y): # On vérifie si il se mord
				endgame()
			i+=1
		deleteSquare(snake[length][0],snake[length][1]) # On supprime le dernier carré
		snake.remove(snake[length])
	except IndexError:
		print('Nouveau carré !')
def deleteSquare(xr,yr):
	"Supprime un carré référencé aux coordonnées relatives"
	tag = str(xr)+'c'+str(yr) 
	can.delete(tag)
def createRound(xr,yr):
	"Crée un rond référencé aux coordonnées relatives"
	tag = str(xr)+'r'+str(yr) # On lui donne un tag en rapport à ses coordonnées relatives
	can.create_oval(xr*24+2,yr*24+2,xr*24+22,yr*24+22, fill='dark red', width=0,tags=tag)
def deleteRound(xr,yr):
	"Supprime un rond référencé aux coordonnées relatives"
	tag = str(xr)+'r'+str(yr) 
	can.delete(tag)
def endgame():
	global end,label_fin,length
	end = 1
	label_fin = tk.Label(fen, text="Partie terminée\nscore : "+str(length),font=("Helvetica", 15), bg='light gray')
	label_fin.place(x=320,y=280)
	can.delete('all')
def startgame():
	global x,y,changed,length,direction,snake,roundx,roundy,end,label_fin
	if end == 1:
		label_fin.destroy()
	score.config(text='Score : \n0')
	x=12
	y=12
	changed = False
	direction='R'
	length=3
	snake = []
	roundx = 4
	roundy = 4
	end = 0
	createRound(roundx,roundy)
	run()

# Fonctions réceptionnaire
def top(event):
	global direction,x,y,changed
	if (direction != 'B' and direction != 'T'):
		direction = 'T'
		y-=1
		createSquare(x,y)
		changed = True
def bot(event):
	global direction,x,y,changed
	if (direction != 'T' and direction != 'B'):
		direction = 'B'
		y+=1
		createSquare(x,y)
		changed = True
def left(event):
	global direction,x,y,changed
	if (direction != 'R' and direction != 'L'):
		direction = 'L'
		x-=1
		createSquare(x,y)
		changed = True
def right(event):
	global direction,x,y,changed
	if (direction != 'L' and direction != 'R'):
		direction = 'R'
		x+=1
		createSquare(x,y)
		changed = True

# Boucle Principale
end = 0
length=0
def run():
	global x,y,changed,length,roundx,roundy,end
	if changed == False: # Si touche non pressée
		if direction == 'R':
			x+=1
		elif direction == 'L':
			x-=1
		elif direction == 'T':
			y-=1
		else:
			y+=1
		createSquare(x,y)
	else :
		changed = False
	if (x<0 or x>29 or y<0 or y>29): # Sortie écran
		endgame()
	if (x == roundx and y == roundy): # Mange pomme
		length+=1
		deleteRound(roundx,roundy)
		roundx=random.randrange(29)
		roundy=random.randrange(29)
		createRound(roundx,roundy)
		score.config(text='Score : \n'+str(length))
	if end == 0: # Boucle
		fen.after(100,run)

### Structure Fenêtre & touches ###
fen = tk.Tk()
can = tk.Canvas(fen, width=720, height=720, bg='light grey')
tk.Button(fen,text="Lancer",command=startgame).grid(row=0,column=1,sticky='n')
score = tk.Label(fen,text='Score : \n'+str(length),font=("Helvetica", 15))
score.grid(row=0,column=1,pady=40)
can.grid(row=0,column=0)
can.bind("<KeyPress-q>", left)
can.bind("<KeyPress-z>", top)
can.bind("<KeyPress-d>", right)
can.bind("<KeyPress-s>", bot)
can.focus_set()
fen.mainloop()