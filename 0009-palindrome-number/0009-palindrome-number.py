class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        og_list= str(x)
        reverse= og_list[::-1]
        return og_list==reverse

    
        
        