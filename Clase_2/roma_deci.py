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

    def test_IX(self):
        decimal_number = convert_roman_to_decimal('IX')
        self.assertEqual(decimal_number, 9)

    def test_X(self):
        decimal_number = convert_roman_to_decimal('X')
        self.assertEqual(decimal_number, 10)

    def test_XI(self):
        decimal_number = convert_roman_to_decimal('XI')
        self.assertEqual(decimal_number, 11)

    def test_XII(self):
        decimal_number = convert_roman_to_decimal('XII')
        self.assertEqual(decimal_number, 12)

    def test_XVIII(self):
        decimal_number = convert_roman_to_decimal('XVIII')
        self.assertEqual(decimal_number, 18)

    def test_XIX(self):
        decimal_number = convert_roman_to_decimal('XIX')
        self.assertEqual(decimal_number, 19)

    def test_XX(self):
        decimal_number = convert_roman_to_decimal('XX')
        self.assertEqual(decimal_number, 20)

    def test_XXI(self):
        decimal_number = convert_roman_to_decimal('XXI')
        self.assertEqual(decimal_number, 21)

    def test_XXIII(self):
        decimal_number = convert_roman_to_decimal('XXIII')
        self.assertEqual(decimal_number, 23)
        
    def test_XXX(self):
        decimal_number = convert_roman_to_decimal('XXX')
        self.assertEqual(decimal_number, 30)

    def test_XXXV(self):
        decimal_number = convert_roman_to_decimal('XXXV')
        self.assertEqual(decimal_number, 35)
    
    def test_XXXVIII(self):
        decimal_number = convert_roman_to_decimal('XXXVIII')
        self.assertEqual(decimal_number, 38)

    def test_XL(self):
        decimal_number = convert_roman_to_decimal('XL')
        self.assertEqual(decimal_number, 40)

    def test_XLVI(self):
        decimal_number = convert_roman_to_decimal('XLVI')
        self.assertEqual(decimal_number, 46)
    
    def test_LIII(self):
        decimal_number = convert_roman_to_decimal('LIII')
        self.assertEqual(decimal_number, 53)

    def test_LXVII(self):
        decimal_number = convert_roman_to_decimal('LXVII')
        self.assertEqual(decimal_number, 67)
    
    def test_LXX(self):
        decimal_number = convert_roman_to_decimal('LXX')
        self.assertEqual(decimal_number, 70)

    def test_LXXXI(self):
        decimal_number = convert_roman_to_decimal('LXXXI')
        self.assertEqual(decimal_number, 81)

    def test_XCIX(self):
        decimal_number = convert_roman_to_decimal('XCIX')
        self.assertEqual(decimal_number, 99)

    def test_C(self):
        decimal_number = convert_roman_to_decimal('C')
        self.assertEqual(decimal_number, 100)

    def test_CI(self):
        decimal_number = convert_roman_to_decimal('CI')
        self.assertEqual(decimal_number, 101)
    
    def test_CDLVI(self):
        decimal_number = convert_roman_to_decimal('CDLVI')
        self.assertEqual(decimal_number, 456)

    def test_D(self):
        decimal_number = convert_roman_to_decimal('D')
        self.assertEqual(decimal_number, 500)

    def test_DIV(self):
        decimal_number = convert_roman_to_decimal('DIV')
        self.assertEqual(decimal_number, 504)

    def test_DCXCIII(self):
        decimal_number = convert_roman_to_decimal('DCXCIII')
        self.assertEqual(decimal_number, 693)

    def test_DCCCXXV(self):
        decimal_number = convert_roman_to_decimal('DCCCXXV')
        self.assertEqual(decimal_number, 748)

    def test_DCCCXXV(self):
        decimal_number = convert_roman_to_decimal('DCCCXXV')
        self.assertEqual(decimal_number, 825)

    def test_CMXLIX(self):
        decimal_number = convert_roman_to_decimal('CMXLIX')
        self.assertEqual(decimal_number, 949)

    def test_CMXCIX(self):
        decimal_number = convert_roman_to_decimal('CMXCIX')
        self.assertEqual(decimal_number, 999)

    def test_MCMXCIX(self):
        decimal_number = convert_roman_to_decimal('MCMXCIX')
        self.assertEqual(decimal_number, 1999)

    def test_MMCMXCIX(self):
        decimal_number = convert_roman_to_decimal('MMCMXCIX')
        self.assertEqual(decimal_number, 2999)

    def test_MMMCMXCIX(self):
        decimal_number = convert_roman_to_decimal('MMMCMXCIX')
        self.assertEqual(decimal_number, 3999)

if __name__ == '__main__':
    unittest.main()