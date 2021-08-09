import unittest

from epevermodbus import extract_bits


class ExtractBitsTestCase(unittest.TestCase):
    def test_extract_d3_2(self):
        data = 11

        d3_2 = extract_bits(data, 2, 0b11)

        self.assertEqual(d3_2, 2)

    def test_extract_d1(self):
        data = 11

        d1 = extract_bits(data, 1, 0b1)

        self.assertEqual(d1, 1)
