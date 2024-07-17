class translator:

    def deciToRoman(self, num):
        val = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]
        syb = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV","I"]
        roman_num = ''
        i = 0
        while num > 0:
            for j in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    # def romanToDeci(self, s):
    #     roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     num = 0
    #     for i in range(len(s)):
    #         if i > 0 and roman[s[i]] > roman[s[i - 1]]:
    #             num += roman[s[i]] - 2 * roman[s[i - 1]]
    #         else:
    #             num += roman[s[i]]
    #     return num

num = int(input("Enter number to translate : "))
trans = translator()

roman_numeral = trans.deciToRoman(num)
print(roman_numeral)
print (num)
# arabic_numeral = trans.romanToDeci(roman_numeral)
# print(arabic_numeral)
