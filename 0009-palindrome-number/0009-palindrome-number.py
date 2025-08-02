class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        str1=str(x)
        rev=str1[::-1]
        return str1==rev
        """
        :type x: int
        :rtype: bool
        """
        