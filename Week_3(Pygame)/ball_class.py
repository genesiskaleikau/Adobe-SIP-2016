#attributes: size, type, color, material
#methoods: bounce, throw, catch, kick, hit
class Ball():
	def __init__(self, size, type, color, material):
		self.size=size
		self.type=type
		self.color=color
		self.material=material

		#methods
	def bounce(height):
		print("The ball bounced " + height + " feet high!")
	def throw(distance):
		print("You threw the ball " + distance + " yards far!")
	def catch():
		print("")

soccer_ball = Ball(6, small, black, 