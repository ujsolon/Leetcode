class Solution:
    def intToRoman(self, num: int) -> str:
        chars = list(str(num))
        thous = {'1': 'M', '2': 'MM', '3': 'MMM'}
        hunds = {'0':'', '1': 'C', '2': 'CC', '3': 'CCC', '4':'CD', '5': 'D', '6':'DC', '7':'DCC', '8':'DCCC', '9':'CM'}
        tens = {'0':'','1': 'X', '2': 'XX', '3': 'XXX', '4':'XL', '5': 'L', '6':'LX', '7':'LXX', '8':'LXXX', '9':'XC'}
        ones = {'0':'','1': 'I', '2': 'II', '3': 'III', '4':'IV', '5': 'V', '6':'VI', '7':'VII', '8':'VIII', '9':'IX'}
        if len(chars)==4:
            romnum = thous[chars[0]]+hunds[chars[1]]+tens[chars[2]]+ones[chars[3]]
        if len(chars)==3:
            romnum = hunds[chars[0]]+tens[chars[1]]+ones[chars[2]]
        if len(chars)==2:
            romnum = tens[chars[0]]+ones[chars[1]]
        if len(chars)==1:
            romnum = ones[chars[0]]
        return(romnum)