class Hexagon:
	def __init__(self, s):
		self.s = s
		self.angle = 120

	def calcArea(self):
		return round((3*(3**0.5)*self.s*self.s) / 2, 3)
	
	def calcPeri(self):
		return 6 * self.s
	
	def calcAngleSum(self):
		return 6 * self.angle
	
	def display(self):
		print(f"Area of hexagon is: {self.calcArea()}\nPerimeter of hexagon is: {self.calcPeri()}\nSum of angles of hexagon is: {self.calcAngleSum()}")


class Square:
	def __init__(self, s):
		self.s = s
	
	def calcAreaSquare(self):
		return self.s ** 2
	
	def calcPeriSquare(self):
		return 4 * self.s

	def display(self):
		print(f"Area of Square is: {self.calcAreaSquare()}\nPerimeter of Square is: {self.calcPeriSquare()}")


if __name__ == '__main__':
	hexagon = Hexagon(1)
	square = Square(1)
	while True:
		print("""
Enter 1 to calculate area, perimeter, and sum of angles of hexagon
Enter 2 to calculate area and perimeter of square
Press any other key to exit.""")
		choice = input()
		if choice == '1':
			hexagon.display()
		elif choice == '2':
			square.display()
		else:
			break
