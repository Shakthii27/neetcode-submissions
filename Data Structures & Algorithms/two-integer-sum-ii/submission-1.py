class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output=[]
        for i in range(len(numbers)):
            othernum=target-numbers[i]
            for j in range(i+1,len(numbers)):
                if numbers[j]==othernum:
                    return [i+1,j+1]

        