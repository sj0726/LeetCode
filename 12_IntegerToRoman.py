class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Convert integer to Roman numerals
        Symbol        Value
        I             1
        IV            4 **
        V             5
        IX            9 **
        X             10
        XL            40 **
        L             50
        XC            90 **
        C             100
        CD            400 **
        D             500
        CM            900 **
        M             1000
        """

        roman_numerals = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }

        num_str = str(num)
        result = ""

        count = 0
        for i in reversed(num_str):
            multiplier = pow(10, count)
            current_digit = int(i)
            true_value = current_digit * multiplier
            if current_digit == 4 or current_digit == 9:
                roman_text = roman_numerals[multiplier] + roman_numerals[true_value + multiplier]
            elif current_digit == 5:
                roman_text = roman_numerals[true_value]
            elif current_digit < 4:
                roman_text = roman_numerals[multiplier] * current_digit
            else: # 5 <
                roman_text = roman_numerals[multiplier * 5] + (roman_numerals[multiplier] * (current_digit - 5))
            result = roman_text + result
            count += 1
        
        return result

print(Solution().intToRoman(58))