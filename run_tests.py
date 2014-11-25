import unittest

testSuite = unittest.TestLoader().discover('tests')
text_runner = unittest.TextTestRunner().run(testSuite)
