class Solution:
    def isPalindrome(self, s) -> bool:
        temp = []
        for i in range(0,len(s)):
            if(('a'<=s[i] and s[i]<='z') or ('A'<=s[i] and s[i]<='Z') or ('0'<=s[i] and s[i]<='9')):
                if('A'<=s[i] and s[i]<='Z'):
                    temp.append(s[i].lower())
                else:
                    temp.append(s[i])
        #print(temp)
        l = int(len(temp))
        for i in range(l):
            if(temp[i]!=temp[len(temp)-i-1]):
                return 0
        return 1