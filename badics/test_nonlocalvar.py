

class Test(object):

	def __init__(self):
		print("init Test Object")


	def testF1(self):


		var1 = "non-local"

		def testF2():
			nonlocal var1

			var1 = "non-local changed"

			return var1

		print(testF2())



test =Test()

test.testF1()

