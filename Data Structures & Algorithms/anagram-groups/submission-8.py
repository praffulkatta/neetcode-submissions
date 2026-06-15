class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp = {}

        for word in strs:

            key ="".join(sorted(word))

            mp.setdefault(key, []).append(word)

        return list(mp.values())
        