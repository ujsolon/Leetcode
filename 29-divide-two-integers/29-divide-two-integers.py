## max integer 32 bits 
L = 2147483647
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = int(dividend/divisor)
        return(max(min(ans,L), -L-1))