class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        digit = 0
        rev = 0
        temp = x

        while x > 0:
            digit = x % 10
            rev = 10 * rev + digit
            x = x // 10

        return temp == rev