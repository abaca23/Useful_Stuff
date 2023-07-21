# imports every file form tkinter and tkinter.ttk
from tkinter import *
from tkinter.ttk import *


class main:
   def __init__(self, master = None):
      self.master = master
      self.x = 0
      self.y = 0
      global MV
      MV = 0
      
      self.canvas = Canvas(self.master, height = 350, width = 700, bg = '#1b1b38')
      self.create()
      self.canvas.pack(expand = True)

   
      # calling class's movement method to
      # move the rectangle
      self.movement()


   
   def create(self):
      self.master.configure(bg = '#1b1b38')
      self.pm = self.canvas.create_oval(
	 325, 150, 375, 200, fill = "yellow")
      
   def movement(self):
      self.canvas.move(self.pm, self.x, self.y)
      
      # for motion in negative x direction
   def left(self, event):
      global MV
      if MV <= -30 or MV >= 30:
         self.canvas.delete('all')
         self.canvas.configure(bg='green')
         self.text = self.canvas.create_text(350, 175, text = 'COMPLETE', fill = 'black')
      else:
         MV = MV - 1
         self.canvas.move(self.pm, -10, 0)
         print(MV)      
      # for motion in positive x direction
   def right(self, event):
      global MV
      if MV <= -30 or MV >= 30:
         self.canvas.delete('all')
         self.canvas.configure(bg='green')
         self.text = self.canvas.create_text(350, 175, text = 'COMPLETE', fill = 'black')
      else:
         MV = MV + 1
         self.canvas.move(self.pm, 10, 0)
         print(MV)
      
if __name__ == "__main__":

   # object of class Tk, responsible for creating
   # a tkinter toplevel window
   master = Tk()
   master.geometry("700x350")
   gfg = main(master)

   # This will bind arrow keys to the tkinter
   # toplevel which will navigate the image or drawing
   master.bind("<KeyPress-Left>", lambda e: gfg.left(e))
   master.bind("a", lambda e: gfg.left(e))
   master.bind("<KeyPress-Right>", lambda e: gfg.right(e))
   master.bind("d", lambda e: gfg.right(e))
   master.bind('q', lambda e: master.quit())
   
   # Infinite loop breaks only by interrupt
   mainloop()
