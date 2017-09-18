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
        price = format_price("surname")
        self.assertIsNone(price)

    def test_mix_number(self):
        price = format_price("24839 USD")
        self.assertIsNone(price)

    def test_multi_decimals(self):
        price = format_price("3245.23.123.32,123")
        self.assertEqual(price, "3 245.23")

    def test_space_number(self):
        price = format_price("3 245.23 323")
        self.assertEqual(price, "3 245.23323")

    def test_symbols_number(self):
        price = format_price("3?23.44")
        self.assertIsNone(price)

    def test_big_number(self):
        price = format_price("99999999")
        self.assertEqual(price, "99 999 999")

    def test_much_bigger(self):
        price = format_price("1999999992739 18239283 9102938102.231")
        self.assertEqual(
                price,
                "1 999 999 992 739 182 392 839 102 938 102.231"
            )

    def test_wrong_space_number(self):
        price = format_price("9 9 99 99 99")
        self.assertEqual(price, "99 999 999")

    def test_plus_number(self):
        price = format_price("+----32134")
        self.assertEqual(price, "+32 134")

    def test_minus_number(self):
        price = format_price("--+-+--324121223123134.41 1")
        self.assertEqual(price, "-324 121 223 123 134.411")


if __name__ == "__main__":
    unittest.main()
