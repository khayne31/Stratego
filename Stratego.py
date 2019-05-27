from graphics import *
sides = 500
win = GraphWin("Stratego", sides, sides)
"""square = Rectangle(Point(0,0),Point(25,25))
square.draw(win)
win.getMouse()"""


size_of_grid = 10
length = int(sides/size_of_grid)
for i in range(size_of_grid):
	for j in range(size_of_grid):
		square = Rectangle(Point(i*length, j*length), Point(i*length + length, j*length+length))
		square.draw(win)
win.getMouse()