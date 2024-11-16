import unittest
from addition import addition 

class TestAddition(unittest.TestCase):  
    def test_add(self):
        result = addition.add(1, 1)
        self.assertEqual(result, 2)  
        result = addition.add(-1, -2)
        self.assertEqual(result, -3)  

if __name__ == '__main__':
    unittest.main()
