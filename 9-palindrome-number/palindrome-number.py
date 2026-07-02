class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif 0 <= x < 10 :
            return True
        else:
            digit = tuple(int(char) for char in str(abs(x)))
            left = 0          
            right = len(digit) - 1 
            while left < right:
                if digit[left] == digit[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True


