class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        mp = {}

        for word in strs:
            key="".join(sorted(word))

            if key is not mp:
                mp[key] = []
            
            mp[key].append(word)

        return list(mp.values())