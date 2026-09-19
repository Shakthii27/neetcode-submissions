from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        top=sorted(freq,key=freq.get,reverse=True)[:k]
        return top