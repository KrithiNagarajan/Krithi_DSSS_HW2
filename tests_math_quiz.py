import unittest
from math_quiz import numbers, operations, quiz


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = numbers(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        
        operator = ['+','-','*']
        for _ in range(1000):
          sign = operations()
          self.assertTrue(sign in operator)

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3,3,'*','3*3',9),
                (1,1,'-','1-1',0),
                (9,1,'*','9*1',9),
                (1,3,'+','1+3',4)
              
               
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
              a,b = quiz(num1, num2, operator)
              self.assertTrue(expected_answer == b)
                
               

if __name__ == "__main__":
    unittest.main()
