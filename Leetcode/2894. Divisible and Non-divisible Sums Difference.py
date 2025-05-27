class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        num1=n*(n+1)/2

        num2=m*(int(n/m))*(int(n/m)+1)/2

        return num1-2*num2






class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

        return n*(n+1)/2-m*(int(n/m))*(int(n/m)+1)
