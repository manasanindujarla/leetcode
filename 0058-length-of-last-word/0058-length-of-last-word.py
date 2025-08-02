class Solution(object):
    def lengthOfLastWord(self, s):
        list=s.split()
        return len(list[-1])
        """
        :type s: str
        :rtype: int
        """
        