class Solution:
    def minimumPlatform(self, aa, ja):
        aa.sort()
        ja.sort()

        n = len(ja)
        needed = 1 
        maxi = 1

        i =1
        j=0

        while i < n and j < n:
            if aa[i] <= ja[j]:
                needed += 1 
                i+=1 
            else:
                needed -= 1
                j+=1

            maxi = max(maxi,needed)   # cant use max bracket mein dhyan se 

        return(maxi)                


