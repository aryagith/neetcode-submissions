class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_table = {}

        for i in range(0,len(names)):
            height_table[heights[i]] = names[i]
        
        heights = sorted(heights)

        result=[]

        for i in range(len(heights)-1, -1, -1):
            result.append(height_table[heights[i]])

        return result
            

        
