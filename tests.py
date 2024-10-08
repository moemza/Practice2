import sys
import unittest
from io import StringIO
from python_prac import *
from unittest.mock import patch

class TestCase(unittest.TestCase):
    
    def test_grade_ave(self):
        self.assertIsInstance(grade_average([1,2,3,4,5]), (int, float), "Expected an integer or float")
        self.assertEqual(grade_average([1,2,3,4,5]), 3, "Unexpected output")
        self.assertEqual(grade_average([-56, 94, -3, 0]), 8.75, "Unexpected output")  # Should return average
        self.assertEqual(grade_average([-2, -45, -82]), -43, "Unexpected output")  # Check the actual average
        self.assertEqual(grade_average([]), -1, "Unexpected output")


    def test_primes(self):
        self.assertIsInstance(find_prime_factors(5), list, "Expected a list")
        self.assertEqual(find_prime_factors(3), [3], "Unexpected output")
        self.assertEqual(find_prime_factors(78), [2, 3, 13], "Unexpected output")    


    def test_interest(self):
        self.assertIsInstance(calculate_interest(4, 3, 5), int, "Expected an int")
        self.assertEqual(calculate_interest(500, 0.1, 3), 165.5, "Unexpected output")
        self.assertEqual(calculate_interest(1000, 0.05, 5), 276.286, "Unexpected output")


    def test_code_word(self):
            self.assertIsInstance(code_word([3,1,20]), str, "Expected a string")
            self.assertEqual(code_word([16,25,20,8,15,14]), "python", "Unexpected output")
            self.assertEqual(code_word([14,1,20,21,18,5]), "nature", "Unexpected output")
            self.assertEqual(code_word([9,0,3,1,14,0,4,15,0,9,20]), "i can do it", "Unexpected output")


    def test_triangles(self):
        self.assertIsInstance(triangles(5), str, "Expected a string")
        self.assertEqual(triangles(3), "*\n**\n***", "Unexpected output")
        self.assertEqual(triangles(6), "*\n**\n***\n****\n*****\n******", "Unexpected output")
        self.assertEqual(triangles(7), "*\n**\n***\n****\n*****\n******\n*******", "Unexpected output")
        

    def test_hollow_triangles(self):
            self.assertIsInstance(hollow_triangle(5), str, "Expected a string")
            self.assertEqual(hollow_triangle(3), "*\n**\n***", "Unexpected output")
            self.assertEqual(hollow_triangle(6), "*\n**\n* *\n*  *\n*   *\n******", "Unexpected output")
            self.assertEqual(hollow_triangle(7), "*\n**\n* *\n*  *\n*   *\n*    *\n*******", "Unexpected output")
