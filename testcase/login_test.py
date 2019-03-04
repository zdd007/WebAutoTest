import unittest
from function.function_01 import *

class loginTest(unittest.TestCase):
	def setUp(self):
		pass
	def test_login(self):
		print("执行用例：登录")
		login("1451953028@qq.com","zdd123456")
	def tearDown(self):
		pass

# if __name__ == "__main__":
# 	unittest.main()