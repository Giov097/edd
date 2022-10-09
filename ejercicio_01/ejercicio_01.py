import unittest
import re


class TestRegex(unittest.TestCase):

    def is_valid_phone(self, phone: str, regex: str) -> bool:
        return bool(re.search(regex, phone, flags=0))

    def test_valid_phone(self):
        regex = "^(\+549|\(?0?)(345)\)?\s?((15)?\d{7})$"
        phone_1 = "(0345) 154123456"
        phone_2 = "+5493454123456"
        phone_3 = "3454123456"
        phone_4 = "+54011123456"
        phone_5 = "34564123456"
        self.assertEqual(True,  self.is_valid_phone(phone_1, regex))
        self.assertEqual(True, self.is_valid_phone(phone_2, regex))
        self.assertEqual(True,  self.is_valid_phone(phone_3, regex))
        self.assertEqual(False,  self.is_valid_phone(phone_4, regex))
        self.assertEqual(False,  self.is_valid_phone(phone_5, regex))


if __name__ == '__main__':
    unittest.main()
