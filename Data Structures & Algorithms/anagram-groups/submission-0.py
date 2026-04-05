class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashset={}

        for i in strs:
            sortedstr = ''.join(sorted(i))

            if sortedstr not in hashset:
                hashset[sortedstr] = []
            
            hashset[sortedstr].append(i)

        return list(hashset.values())