class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        list2=[]
        for i in range(0, len(matrix[0])):
            list1=[]
            for j in range(0,len(matrix)):
                list1.append(matrix[j][i])
            list2.append(list1)
        return list2