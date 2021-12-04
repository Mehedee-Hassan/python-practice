class test:

	def __init__(self,a):
		self.a = a

	def __repr__(self):
		return (repr(self.a))

a1 = test(10)
print(a1)
tt = a1
print(tt) # output: 10

a1 = test(122)

print(tt,a1) # ooutput: 10 122

