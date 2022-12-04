from turtle import Turtle


class Knight(Turtle):
	def __init__(self, horizontal, vertical):
		super().__init__()
		self.shape = self.shape("circle")
		self.color = self.color("red")
		self.width = self.width = 12
		self.height = self.height = 12
		self.pos = (horizontal, vertical)
		self.penup()
		self.goto(self.pos)

	def kill_bishop(self, bishop_pos):
		# defining all the possible situation that knight kills the bishop
		# maximum amount of cases
		case1 = (self.pos[0] + 120, self.pos[1] + 60)
		case2 = (self.pos[0] + 120, self.pos[1] - 60)
		case3 = (self.pos[0] + 60, self.pos[1] + 120)
		case4 = (self.pos[0] + 60, self.pos[1] - 120)
		case5 = (self.pos[0] - 120, self.pos[1] - 60)
		case6 = (self.pos[0] - 120, self.pos[1] + 60)
		case7 = (self.pos[0] - 60, self.pos[1] - 120)
		case8 = (self.pos[0] + 60, self.pos[1] + 120)
		if
