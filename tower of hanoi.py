class Solution:
    def towerOfHanoi(self, n, pehli, dusri, tesri):
        if n == 0:
            return 0
        
        return (
            self.towerOfHanoi(n - 1, pehli, tesri, dusri) +  
            1 +                                                  
            self.towerOfHanoi(n - 1, tesri, dusri, pehli)    
        )

