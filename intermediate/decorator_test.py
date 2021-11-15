
def chagneTheReview(func):

	def weChangeRealreview(*args,**kargs):

		print(kargs)
		for k,val in kargs.items():
			print(k,"->",val)       # print all the key val value ,dictionary
		
		review=func(*args,**kargs)

		if kargs['whoamI'] == "evil":
			review = "1/10"
		elif kargs['whoamI'] == "good":
			review = "100/10"

		return review

	return weChangeRealreview

@chagneTheReview
def testTheSalt(whoamI = "evil"):
	return "10/10"


print(testTheSalt(whoamI = "evil"))
print(testTheSalt(whoamI = "good"))
