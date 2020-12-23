from django.test import TestCase
from app.calc import add, substract

class CalcTest(TestCase):

    def test_add_number(self):
        """Test adding 2 number are added together"""
        self.assertEqual(add(3,5), 8)

    def test_sub_nubmer(self):
        """Test substraction of 2 numbers"""
        self.assertEqual(substract(5,3), 2)
