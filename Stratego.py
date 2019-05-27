from graphics import *
import math


class Piece:
	def __init__(self, text: Text, team: str):
		self.text = text
		self.team = team

class Tile:
	def	__init__(self, position: Point, length: int, window, tile_type: str = "reg"):

		self.position = position
		self.type = tile_type
		#self.rectangle = Rectangle(Point(0,0), Point(0,0))
		self.length = length
		self.window = window
		self.colour = "blue" if self.type == "water" else "green"

	def draw_square(self):
		top_left_x = self.position.x * self.length
		top_left_y = self.position.y * self.length
		self.rectangle = Rectangle(Point(top_left_x , top_left_y ), Point(top_left_x + self.length - 1, top_left_y + self.length - 1))
		#self.rectangle.setFill(self.colour)
		self.rectangle.draw(self.window)
		print(Point(.5,.5))
sides = 500
size_of_grid = 10
length = int(sides/size_of_grid)
win = GraphWin("Stratego", sides, sides)

tileArray = []

def drawGrid():
	board = Image(Point(250,250), "board.png")
	board.draw(win)
	for i in range(size_of_grid):
		for j in range(size_of_grid):
			#square = Rectangle(Point(i*length, j*length), Point(i*length + length, j*length+length))
			#square.draw(win)
			g = Tile( Point(i,j), length, win, tile_type = "water" if ((j == 4 or j == 5) and (i == 2 or i == 3 or i == 6 or i == 7)) else "reg")
			g.draw_square()
			tileArray.append(g)

def getTile(point):
	x = math.floor(point.x / length)
	y = math.floor(point.y / length)
	print((x, y))
	for tile in tileArray:
		if x == tile.position.x and y == tile.position.y:
			return tile
	return None

drawGrid()
piece = Text(Point(24.5,24.5), "3")
piece.draw(win)
while (True):
	coor = win.getMouse()
	getTile(coor).rectangle.setOutline("Yellow")
