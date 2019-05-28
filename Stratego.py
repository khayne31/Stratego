from graphics import *
import math
from collections import deque
pieceValue = ["Flag", "Bomb", "Spy", "Scout", "Miner", "Sergeant", "Lieutenant", "Captain", "Major", "Colonel", "General", "Marshall"]
sides = 500
size_of_grid = 10
length = int(sides/size_of_grid)
win = GraphWin("Stratego", sides, sides)

tileArray = []

def getTile(point):
	x = math.floor(point.x / length)
	y = math.floor(point.y / length)
	for tile in tileArray:
		if x == tile.position.x and y == tile.position.y:
			return tile
	return None

class Piece:
	def __init__(self, name: Text, team: str, img_path: str, window, position: Point):
		self.text = name
		self.team = team
		self.img_path = img_path
		self.position = position
		self.img = None
		self.window = window
		self.tile = None


	def draw_piece(self):
		self.img = Image(self.position, self.img_path)
		self.img.draw(self.window)

	def move_up(self, x):
		self.img.undraw()
		self.position.y -=  x * length
		self.tile = getTile(self.position)
		self.img.move(0,-x)
		self.draw_piece()

	def move_down(self, x):
		self.img.undraw()
		self.position.y += x * length
		self.tile = getTile(self.position)
		self.img.move(0,x)
		self.draw_piece()


	def move_right(self, x):
		self.img.undraw()
		self.position.x += x * length
		self.tile = getTile(self.position)
		self.img.move(x,0)
		self.draw_piece()


	def move_left(self, x):
		self.img.undraw()
		self.position.x -= x * length
		self.tile = getTile(self.position)
		self.img.move(-x,0)
		self.draw_piece()

	def move_to_tile(self, tile):
		self.img.undraw()
		self.position.x = tile.position.x * tile.length + tile.length/2
		self.position.y = tile.position.y * tile.length + tile.length/2
		tile.piece = self
		if self.tile != None:
			self.tile.piece = None
		self.tile = tile
		self.draw_piece()




class Tile:
	def	__init__(self, position: Point, length: int, window, peice: Piece = None, tile_type: str = "reg"):

		self.position = position
		self.type = tile_type
		#self.rectangle = Rectangle(Point(0,0), Point(0,0))
		self.length = length
		self.window = window
		self.colour = "blue" if self.type == "water" else "green"
		self.peice = peice
		self.selected = False;


	def draw_square(self):
		top_left_x = self.position.x * self.length
		top_left_y = self.position.y * self.length
		self.rectangle = Rectangle(Point(top_left_x , top_left_y ), Point(top_left_x + self.length - 1, top_left_y + self.length - 1))
		#self.rectangle.setFill(self.colour)
		#self.rectangle.setOutline("blue" if self.type == "water" else "black")
		#self.rectangle.setFill(self.colour)
		self.rectangle.draw(self.window)



def drawGrid():
	board = Image(Point(250,250), "images/board (3).png")
	board.draw(win)
	for i in range(size_of_grid):
		for j in range(size_of_grid):
			#square = Rectangle(Point(i*length, j*length), Point(i*length + length, j*length+length))
			#square.draw(win)
			g = Tile( Point(i,j), length, win, tile_type = "water" if ((j == 4 or j == 5) and (i == 2 or i == 3 or i == 6 or i == 7)) else "reg")
			g.draw_square()
			tileArray.append(g)



drawGrid()
count = 0
for i in range(10):
	for j in range(10):
		if i >= 0 and i < 2:
			piece = Piece(pieceValue[count], "blue", "images/" + pieceValue[count] + "Blue.png", win, Point(j * length + 25, i * length + 25))
			current_tile = getTile(Point(j * length + 25, i * length + 25))
			current_tile.piece = piece
			piece.draw_piece()
			#piece = Image(Point(j * 50 + 25, i * 50 + 25), "images/" + pieceValue[count] + "Blue.png")
			#piece.draw(win)
			count = (count + 1) % 12
		elif i >= 8 and i < 10:
			piece = Piece(pieceValue[count], "red", "images/" + pieceValue[count] + "Red.png", win, Point(j * length + 25, i * length + 25))
			current_tile = getTile(Point(j * length + 25, i * length + 25))
			current_tile.piece = piece
			piece.draw_piece()
			#piece = Image(Point(j * 50 + 25, i * 50 + 25), "images/" + pieceValue[count] + "Red.png")
			#piece.draw(win)
			count = (count + 1) % 12
		else:
			count = 0

highlighted = []
selected_piece = None
while (True):
	coor = win.getMouse()
	
	if(len(highlighted) == 0):
		return_tile = getTile(coor)
		return_tile.rectangle.setOutline("Yellow")
		highlighted.append(return_tile)
		#current_peice = return_tile.piece
		#current_peice.move_down(2)
		#return_tile.piece = None
		selected_piece = return_tile.piece
	else:
		return_tile = getTile(coor)
		return_tile.rectangle.setOutline("Yellow")
		highlighted.append(return_tile)
		first_tile = highlighted.pop(0)
		first_tile.rectangle.setOutline("black")

		selected_piece.move_to_tile(return_tile)
		#current_peice = return_tile.piece
		#current_peice.move_down(2)
		#return_tile.piece = None
		


