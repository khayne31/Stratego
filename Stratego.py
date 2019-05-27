from graphics import *


class Tile:
	def	__init__(self, position: Point, length: int, window, tile_type: str = "reg"):

		self.position = position
		self.type = tile_type
		self.rectangle = Rectangle(Point(0,0), Point(0,0))
		self.length = length
		self.window = window
		self.colour = "blue" if self.type == "water" else "green"

	def draw_square(self):
		top_left_x = self.position.x * self.length
		top_left_y = self.position.y * self.length
		self.rectangle = Rectangle(Point(top_left_x , top_left_y ), Point(top_left_x + self.length, top_left_y + self.length))
		self.rectangle.setFill(self.colour)
		self.rectangle.draw(self.window)




sides = 500
win = GraphWin("Stratego", sides, sides)


size_of_grid = 10
length = int(sides/size_of_grid)

def drawGrid():
	for i in range(size_of_grid):
		for j in range(size_of_grid):
			#square = Rectangle(Point(i*length, j*length), Point(i*length + length, j*length+length))
			#square.draw(win)
			g = Tile( Point(i,j), length, win, tile_type = "water" if ((j == 4 or j == 5) and (i == 2 or i == 3 or i == 6 or i == 7)) else "reg")
			g.draw_square()

drawGrid()
while (True):
	win.getMouse()