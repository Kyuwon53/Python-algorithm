def romanToInt(self, s: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    pre = ''
    for c in s:
        if pre != '' and roman[pre] < roman[c]:
            result -= (roman[pre] * 2)
        result += roman[c]
        pre = c
    return result
