class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        rev=""
        for char in s:
            if char.isalpha() or char.isdigit():
                rev=rev+char
        print (rev)
        return rev==rev[::-1]
        