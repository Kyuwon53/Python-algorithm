def isPalindrome(self, x: int) -> bool:
    s = str(x)
    length = len(s)
    if x < 0:
        return False
    for i in range(length + 1 // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True
