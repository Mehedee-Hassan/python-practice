class A:

	def __init__(self,a):
		self.a = a

	def __add__(self,o):
		return self.a + o.a


	def __str__(self):
		return str(self.a)


	def __gt__(self,other):
		if (self.a>other.a):
			return True
		else:
			return False


	def __eq__(self,other):
		if (self.a == other.a):
			return True
		else:
			return False



obj1 = A(1)
obj2 = A(1)


obj3 = A("a")
obj4 = A("b")

print(obj1+obj2)
print(obj3+obj4)
print(obj1==obj2)
print(obj1>obj2)


"""
2
ab
True
False

"""
