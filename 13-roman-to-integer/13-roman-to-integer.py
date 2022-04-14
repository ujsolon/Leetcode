class Solution:
    def romanToInt(self, s: str) -> int:
        numerals = {'I':1, 'V':5, 'X':10, "L":50, "C":100, "D":500, "M":1000, "IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        chars = list(s)
        i=0
        hindarab=0
        newchar=[]
        while i < len(s)-1 :
            if numerals[chars[i]] < numerals[chars[i+1]]:
                newchar = chars[i]+chars[i+1]
                print (newchar)
                hindarab=hindarab+numerals[newchar]
                i=i+2
            else:
                hindarab=hindarab+numerals[chars[i]]
                i=i+1
        if i==len(s)-1:
            hindarab=hindarab+numerals[chars[i]]
        return(hindarab)