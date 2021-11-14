
iamglobal = "gloabal"

class Test(object):

	global iamglobal

	def __init__(self):
		print("init Test Object")


	def testF1(self):

		global iamglobal
		var1 = "non-local"

		def testF2():
			global iamglobal
			nonlocal var1

			var1 = "non-local changed"
			iamglobal = "iamglobal changed in testF2"

			return var1,iamglobal

		print(testF2())



test =Test()

test.testF1()

