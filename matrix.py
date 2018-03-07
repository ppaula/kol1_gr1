class Matrix:

	a = 0
	b = 0
	c = 0
	d = 0

	def __init__(self, a, b, c, d):
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def print(self):
		print("[", self.a, ", ", self.b, "][", self.c, ", ", self.d, "]")

	def add(self, matrix):
		matrix_2 = Matrix(self.a + matrix.a, self.b + matrix.b, self.c + matrix.c, self.d + matrix.d)
		return matrix_2

	def prod(self, matrix):
		matrix_2 = Matrix(self.a * matrix.a + self.b * matrix.c, self.b * matrix.b + self.b * matrix.d, self.c * matrix.c + self.d * matrix.c, self.d * matrix.d + self.c * matrix.b)
		return matrix_2

