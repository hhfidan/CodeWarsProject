# RomanNumerals class to convert between Roman numerals and integers
class RomanNumerals:
    @staticmethod
    def to_roman(val : int) -> str:
        """
        Converts an integer to a Roman numeral.
        :param val: Integer value (1 <= val < 4000)
        :return: Roman numeral string
        """
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]
        
        result = ""
        for value, symbol in values:
            while val >= value:
                result += symbol
                val -= value
        
        print(result)
        return result
    
    @staticmethod
    def from_roman(roman_num : str) -> int:
        """
        Converts a Roman numeral to an integer.
        :param roman_num: Roman numeral string
        :return: Integer value
        """
        values = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        
        total = 0
        prev = 0
        
        for symbol in reversed(roman_num):
            current_value = values[symbol]
            if current_value < prev:
                total -= current_value
            else:
                total += current_value
            prev = current_value
        
        return total
