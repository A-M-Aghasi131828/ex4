from turtle import Turtle


class Bishop(Turtle):

	def __init__(self, horizontal, vertical):
		super().__init__()
		self.shape = self.shape("circle")
		self.color = self.color("blue")
		self.width = self.width = 12
		self.height = self.height = 12
		self.pos = (horizontal, vertical)
		self.penup()
		self.goto(self.pos)
