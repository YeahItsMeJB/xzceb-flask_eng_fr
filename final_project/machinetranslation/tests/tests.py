import unittest
from translator import french_to_english, english_to_french

class TestFrEn(unittest.TestCase):
    def test_french_to_english(self):
        self.assertIsNone(french_to_english())
        self.assertEqual(french_to_english("Bonjour"),"Hello")

class TestEnFr(unittest.TestCase):
    def test_english_to_french(self):
        self.assertIsNone(english_to_french())
        self.assertEqual(english_to_french("Hello"),"Bonjour")

unittest.main()
