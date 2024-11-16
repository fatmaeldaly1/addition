   python
   import unittest
   from addition import Addition

   class TestAddition(unittest.TestCase):
       def test_add(self):
           adder = Addition()
           self.assertEqual(adder.add(3, 5), 8)
           self.assertEqual(adder.add(-1, 1), 0)
           self.assertEqual(adder.add(0, 0), 0)
           self.assertEqual(adder.add(-3, -5), -8)

   if __name__ == '__main__':
       unittest.main()
