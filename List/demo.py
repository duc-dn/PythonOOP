class Solution(object):
    def isPalindrome(self, s: str):
        s = [i for i in s.lower() if i.isalnum()]
        return True if s == s[::-1] else False


s = Solution()
print(s.isPalindrome("0P"))