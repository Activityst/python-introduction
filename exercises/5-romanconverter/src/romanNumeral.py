#write code here
def dec_to_rom(n):
    nb_romain = \
    {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    roman = ''
    for value, symbol in nb_romain.items():
        while n >= value:
            roman +=  symbol
            n -= value

    return roman

def rom_to_dec(roman: str) -> int:
   decimal = \
    {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

   nb_decimal = 0
   prev_value = 0

   for char in reversed(roman.upper()):
       value = decimal.get(char, 0)
       if value < prev_value:
           nb_decimal -= value
       else:
           nb_decimal += value
       prev_value = value

   return nb_decimal