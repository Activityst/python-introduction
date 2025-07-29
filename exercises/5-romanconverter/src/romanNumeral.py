#write code here
def jn(n):
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
