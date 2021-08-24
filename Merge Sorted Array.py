class Solution:
    def merge(self,num1 , m, num2 , n):
        if num2 == []:
            return num1
        while m>0 and n>0: 
            if(num1[m-1] > num2[n-1]):
                num1[m+n-1] = num1[m-1];
                m -=1
            else:
                num1[m+n-1] = num2[n-1];
                n -=1
        if(n>0):
            for i in range(n):
                num1[i] = num2[i]