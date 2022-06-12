import numpy as np

def intToDigits(n:int):
    return ([int(item) for item in list(str(n))])

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return(np.prod(intToDigits(n))-sum(intToDigits(n)))