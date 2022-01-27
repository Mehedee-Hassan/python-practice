from collections import UserDict


class PDict(UserDict):

	# override default fuciton
	def __del__(self):
		raise RuntimeError("Deletion not allowed in pDict!!")


pDict = PDict()
pDict["a"] = 1
pDict["b"] = 2
del pDict["a"]
print(pDict)


"""
12
deque([23, 1, 12, 13, 14])
{'b': 2}
Exception ignored in: <function PaypayDict.__del__ at 0x7f5e71c92ca0>
Traceback (most recent call last):
  File "/home/mehedee/Documents/programming/python/tdd/project1/tests/tt.py", line 26, in __del__

--> RuntimeError: Deletion not allowed in pDict!!

[Finished in 0.0s]

"""
