class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = Counter(nums)
        return [item for item, count in hashmap.most_common(k)]

