# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:31:26 2018

@author: eumartinez

"""


from tkinter import *
from Triki import Triki
from alphabeta_search import alphabeta_search
from MiniMax import MiniMax


class App:
       
    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()
        self.height=500
        self.width=500
        self.grid_column=3
        self.grid_row=3
        self.canvas = Canvas(self.frame, height=self.height, width=self.width)
        self.cellwidth = int(self.canvas["width"])/self.grid_column
        self.cellheight = int(self.canvas["height"])/self.grid_row
        self.draw_grid()
        self.canvas.pack()  
        self.model=[[0 for x in range(self.grid_column)] for y in range(self.grid_row)]
        self.player = 1
        self.pos=(0,0)
        
        
        def handler(event, self=self):
            return self.__onClick(event)
        
        self.canvas.bind('<Button-1>', handler)
        
        
        self.hi_there = Button(self.frame, text="Jugar", command=self.start_Game)
        self.hi_there.pack(side=LEFT)
        
    
    def draw_grid(self):
        for i in range(self.grid_row):
            for j in range(self.grid_column):
                x1 = i * self.cellwidth
                y1 = j * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")
        
        
    def drawChip(self):
        x=self.pos[1]*self.cellwidth
        y=self.pos[0]*self.cellheight
        if(self.player ==1):
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='white')
            self.player=2
        else:
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='black')
            self.player=1

    def drawChipMaquina(self,move,player):
        x=move[0]
        y=move[1]
        if(player ==1):
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='white')
            self.player=2
        else:
            self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='black')
            self.player=1
            
    
    def drawChips(self):
        for i in range(len(self.model)):
            row=self.model[i]
            for j in range(len(row)):
                val=self.model[i][j]
                x=j*self.cellwidth
                y=i*self.cellheight
                if(val ==1):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='white')
                elif(val ==2):
                    self.canvas.create_oval(x,y,x+self.cellwidth,y+self.cellheight, fill='black')
            
    def __onClick(self, event):
        
            i=int(event.y/self.cellheight)
            j=int(event.x/self.cellwidth)
            self.pos =(i,j)
            if self.model[i][j]==0:
                self.model[i][j]=self.player
            if(self.player==1):
                self.player=2
            else:
                self.player=1
            print(self.model)
            
            self.drawChips()
        
       
    
    def  start_Game(self):
        tk = Triki()
        a = alphabeta_search(self.model,tk)
        print("Position : ",a)
        
        

        
        

root = Tk()
app = App(root)
root.mainloop()