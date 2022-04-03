import unittest


def convert_decimal_to_roman(decimal_number):
    roman1 = ''
    roman2 = ''
    roman3 = ''
    decimal_number_units = (decimal_number%10)
    decimal_number_tens = (decimal_number%100-decimal_number%10)//10
    decimal_number_hundreds = (decimal_number%1000-decimal_number%100)//100


    if decimal_number:
        for digit in range(decimal_number_hundreds):
            if decimal_number_hundreds < 4:
                roman1 += 'C'
            elif decimal_number_hundreds == 4:
                roman1 = 'CD'
            elif  4 < decimal_number_hundreds < 9:
                roman1 = 'C'*(decimal_number_hundreds - 5)
                roman1 = 'D' + roman1
            elif decimal_number_hundreds == 9:
                roman1 = 'CM'

        for digit in range(decimal_number_tens):
            if decimal_number_tens < 4:
                roman2 += 'X'
            elif decimal_number_tens == 4:
                roman2 = 'XL'
            elif  4 < decimal_number_tens < 9:
                roman2 = 'X'*(decimal_number_tens - 5)
                roman2 = 'L' + roman2
            elif decimal_number_tens == 9:
                roman2 = 'XC'

        for digit in range(decimal_number_units):
            if decimal_number_units < 4:
                roman3 += 'I'
            elif decimal_number_units == 4:
                roman3 = 'IV'
            elif  4 < decimal_number_units < 9:
                roman3 = 'I'*(decimal_number_units - 5)
                roman3 = 'V' + roman3
            elif decimal_number_units == 9:
                roman3 = 'IX'

    roman = roman1 + roman2 + roman3

    return roman

class TestDecimalToRoman(unittest.TestCase):

    def test_1(self):
        roman_number = convert_decimal_to_roman(1)
        self.assertEqual(roman_number, 'I')

    def test_2(self):
        roman_number = convert_decimal_to_roman(2)
        self.assertEqual(roman_number, 'II')

    def test_3(self):
        roman_number = convert_decimal_to_roman(3)
        self.assertEqual(roman_number, "III")

    def test_5(self):
        roman_number = convert_decimal_to_roman(5)
        self.assertEqual(roman_number, "V")

    def test_6(self):
        roman_number = convert_decimal_to_roman(6)
        self.assertEqual(roman_number, "VI")
    
    def test_9(self):
        roman_number = convert_decimal_to_roman(9)
        self.assertEqual(roman_number, "IX")

    def test_10(self):
        roman_number = convert_decimal_to_roman(10)
        self.assertEqual(roman_number, "X")

    def test_11(self):
        roman_number = convert_decimal_to_roman(11)
        self.assertEqual(roman_number, "XI")

    def test_12(self):
        roman_number = convert_decimal_to_roman(12)
        self.assertEqual(roman_number, "XII")

    def test_18(self):
        roman_number = convert_decimal_to_roman(18)
        self.assertEqual(roman_number, "XVIII")

    def test_19(self):
        roman_number = convert_decimal_to_roman(19)
        self.assertEqual(roman_number, "XIX")

    def test_20(self):
        roman_number = convert_decimal_to_roman(20)
        self.assertEqual(roman_number, "XX")

    def test_21(self):
        roman_number = convert_decimal_to_roman(21)
        self.assertEqual(roman_number, "XXI")

    def test_23(self):
        roman_number = convert_decimal_to_roman(23)
        self.assertEqual(roman_number, "XXIII")

    def test_30(self):
        roman_number = convert_decimal_to_roman(30)
        self.assertEqual(roman_number, "XXX")

    def test_35(self):
        roman_number = convert_decimal_to_roman(35)
        self.assertEqual(roman_number, "XXXV")

    def test_38(self):
        roman_number = convert_decimal_to_roman(38)
        self.assertEqual(roman_number, "XXXVIII")

    def test_40(self):
        roman_number = convert_decimal_to_roman(40)
        self.assertEqual(roman_number, "XL")
    
    def test_46(self):
        roman_number = convert_decimal_to_roman(46)
        self.assertEqual(roman_number, "XLVI")

    def test_53(self):
        roman_number = convert_decimal_to_roman(53)
        self.assertEqual(roman_number, "LIII")

    def test_67(self):
        roman_number = convert_decimal_to_roman(67)
        self.assertEqual(roman_number, "LXVII")
    
    def test_70(self):
        roman_number = convert_decimal_to_roman(70)
        self.assertEqual(roman_number, "LXX")

    def test_81(self):
        roman_number = convert_decimal_to_roman(81)
        self.assertEqual(roman_number, "LXXXI")
    
    def test_99(self):
        roman_number = convert_decimal_to_roman(99)
        self.assertEqual(roman_number, "XCIX")
    
    def test_100(self):
        roman_number = convert_decimal_to_roman(100)
        self.assertEqual(roman_number, "C")

    def test_101(self):
        roman_number = convert_decimal_to_roman(101)
        self.assertEqual(roman_number, "CI")

    def test_456(self):
        roman_number = convert_decimal_to_roman(456)
        self.assertEqual(roman_number, "CDLVI")

    def test_500(self):
        roman_number = convert_decimal_to_roman(500)
        self.assertEqual(roman_number, "D")

    def test_693(self):
        roman_number = convert_decimal_to_roman(693)
        self.assertEqual(roman_number, "DCXCIII")

    def test_748(self):
        roman_number = convert_decimal_to_roman(748)
        self.assertEqual(roman_number, "DCCXLVIII")

    def test_825(self):
        roman_number = convert_decimal_to_roman(825)
        self.assertEqual(roman_number, "DCCCXXV")

    def test_999(self):
        roman_number = convert_decimal_to_roman(999)
        self.assertEqual(roman_number, "CMXCIX")

if __name__ == '__main__':
    unittest.main()