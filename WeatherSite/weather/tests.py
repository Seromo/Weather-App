from django.test import TestCase,SimpleTestCase

# Create your tests here.
from .convertor import convert

class TestConvert(TestCase):
    def test_convert(self):
        self.assertAlmostEqual(convert(30),86.0)
        self.assertAlmostEqual(convert(-30), -22.0)
    