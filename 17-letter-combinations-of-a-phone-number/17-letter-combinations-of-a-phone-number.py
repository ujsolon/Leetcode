class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':{'a','b', 'c'}, '3':{'d','e','f'}, '4':{'g','h','i'}, '5':{'j','k','l'}, '6':{'m','n','o'}, '7':{'p','q','r','s'}, '8':{'t','u','v'}, '9':{'w','x','y','z'}}
        digits = list(digits)
        word=[]
        for nums in digits:
            if word==[]:
                word=[x for x in mapping[nums]]
            else:
                word = [x+y for x in word for y in mapping[nums]]
        return(word)