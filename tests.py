import unittest
from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_int_format(self):
        price = format_price(2000)
        self.assertEqual(price, "2 000")

    def test_string_format(self):
        price = format_price("2437")
        self.assertEqual(price, "2 437")

    def test_float_format(self):
        price = format_price(3245.000)
        self.assertEqual(price, "3 245")

    def test_decimal_format(self):
        price = format_price(3245.1250)
        self.assertEqual(price, "3 245.125")

    def test_string_float_format(self):
        price = format_price("3245.23")
        self.assertEqual(price, "3 245.23")

    def test_none_number(self):
        price = format_price('surname')
        self.assertIsNone(price)

    def test_mix_number(self):
        price = format_price('24839 USD')
        self.assertIsNone(price)


if __name__ == '__main__':
    unittest.main()
