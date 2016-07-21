class Dog():

	#Constructor function
	def __init__(self,furColor, weight, eyeColor, name):
		self.furColor = furColor
		self.weight = weight
		self.eyeColor = eyeColor
		self.name = name
		#functions
		def bark(self):
			print("woof")

		def wag(self):
			print("wagging tail")

		def run(self):
			print("Your dog is running away!")

Toto = Dog("brown", 25, "blue", "Toto")

Toto.run()