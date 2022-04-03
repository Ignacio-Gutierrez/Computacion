import unittest

def convert_roman_to_decimal(roman_number):

    decimal_number = 0
    roma1 = ''

    for letter in roman_number:
        if letter == 'I':
            decimal_number += 1
        if letter == 'V':
            if roma1 == 'I':
                decimal_number -= 2
            decimal_number += 5
        if letter == 'X':
            if roma1 == 'I':
                decimal_number -= 2
            decimal_number += 10
        if letter == 'L':
            if roma1 == 'X':
                decimal_number -=20
            decimal_number += 50
        if letter == 'C':
            if roma1 == 'X':
                decimal_number -=20
            decimal_number += 100
        if letter == 'D':
            if roma1 == 'C':
                decimal_number -=200
            decimal_number +=500
        if letter == 'M':
            if roma1 == 'C':
                decimal_number -=200
            decimal_number +=1000
        roma1 = letter
    return decimal_number

class TestRomanToDecimal(unittest.TestCase):
    def test_I(self):
        decimal_number = convert_roman_to_decimal('I')
        self.assertEqual(decimal_number, 1)

    def test_II(self):
        decimal_number = convert_roman_to_decimal('II')
        self.assertEqual(decimal_number, 2)
    
    def test_III(self):
        decimal_number = convert_roman_to_decimal('III')
        self.assertEqual(decimal_number, 3)

    def test_V(self):
        decimal_number = convert_roman_to_decimal('V')
        self.assertEqual(decimal_number, 5)

    def test_Vl(self):
        decimal_number = convert_roman_to_decimal('VI')
        self.assertEqual(decimal_number, 6)

    def test_VII(self):
        decimal_number = convert_roman_to_decimal('VII')
        self.assertEqual(decimal_number, 7)

    def test_VIII(self):
        decimal_number = convert_roman_to_decimal('VIII')
        self.assertEqual(decimal_number, 8)

    def test_X(self):
        decimal_number = convert_roman_to_decimal('X')
        self.assertEqual(decimal_number, 10)

    def test_XIV(self):
        decimal_number = convert_roman_to_decimal('XIV')
        self.assertEqual(decimal_number, 14)

    def test_XIX(self):
        decimal_number = convert_roman_to_decimal('XIX')
        self.assertEqual(decimal_number, 19)

    def test_XXIV(self):
        decimal_number = convert_roman_to_decimal('XXIV')
        self.assertEqual(decimal_number, 24)
        
    def test_XLIII(self):
        decimal_number = convert_roman_to_decimal('XLIII')
        self.assertEqual(decimal_number, 43)

    def test_LVIII(self):
        decimal_number = convert_roman_to_decimal('LVIII')
        self.assertEqual(decimal_number, 58)

    def test_LXXII(self):
        decimal_number = convert_roman_to_decimal('LXXII')
        self.assertEqual(decimal_number, 72)

    def test_LXXXVII(self):
        decimal_number = convert_roman_to_decimal('LXXXVII')
        self.assertEqual(decimal_number, 87)

    def test_XCI(self):
        decimal_number = convert_roman_to_decimal('XCI')
        self.assertEqual(decimal_number, 91)

    def test_CI(self):
        decimal_number = convert_roman_to_decimal('CI')
        self.assertEqual(decimal_number, 101)

    def test_CXLIX(self):
        decimal_number = convert_roman_to_decimal('CXLIX')
        self.assertEqual(decimal_number, 149)

    def test_CDLXXVIII(self):
        decimal_number = convert_roman_to_decimal('CDLXXVIII')
        self.assertEqual(decimal_number, 478)

    def test_DCXCIII(self):
        decimal_number = convert_roman_to_decimal('DCXCIII')
        self.assertEqual(decimal_number, 693)

    def test_CMLIV(self):
        decimal_number = convert_roman_to_decimal('CMLIV')
        self.assertEqual(decimal_number, 954)

if __name__ == '__main__':
    unittest.main()