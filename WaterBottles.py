class Solution(object):     
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        count = 0
        sum=numBottles
        count1=numBottles
        while sum>=numExchange:
            a=numBottles // numExchange
            b =numBottles % numExchange
            count=count + a
            sum=a+b
            numBottles=sum
        return count1+count                          
        
