
## https://stackoverflow.com/posts/54480126/revisions
## uses base python to output all the possible combinations of a list of integers a

def combs(a:list[int])-> list[list[int]]:
    if len(a) == 0:
        return [[]]
    cs = []
    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
    return cs

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        digits = [1,2,3,4,5,6,7,8,9]
        klength = [x for x in combs(digits) if len(x)==k]
        nsum = [x for x in klength if sum(x)==n]
        return nsum