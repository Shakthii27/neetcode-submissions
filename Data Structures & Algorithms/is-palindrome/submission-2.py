class Solution:
    def isPalindrome(self, s: str) -> bool:
        string=""
        for i in s:
            if i.isalnum():
                string+=i
        if string.lower()[:]==string.lower()[::-1]:
            return True
        else:
            return False
        