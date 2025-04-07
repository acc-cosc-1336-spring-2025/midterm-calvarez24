#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_d.question_d import get_sum_of_evens

class Test_Config(unittest.TestCase):


    def test_get_sum_of_evens1(self):

        self.assertEqual(True, get_sum_of_evens(11) == 30)

    def test_get_sum_of_evens2(self):

        self.assertEqual(True, get_sum_of_evens(10) == 30)

    def test_get_sum_of_evens3(self):

        self.assertEqual(True, get_sum_of_evens(8) == 20)

