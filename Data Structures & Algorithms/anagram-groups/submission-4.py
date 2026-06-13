class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        mp = {}

        for word in strs:
            key="".join(sorted(word)) # creates an identity for anagrams. 

            mp.setdefault(key, []).append(word)  #If key does not exist, create it with []

        return list(mp.values())