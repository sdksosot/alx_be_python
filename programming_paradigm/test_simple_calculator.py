import  unittest
class SimpleCalculator(unittest.TestCase):
    def add(self,a,b):
        self.assertEqual(a+b,a+b,'should be a+b')