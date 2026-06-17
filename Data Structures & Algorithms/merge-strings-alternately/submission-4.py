class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        p1 = 0
        p2 = 0
        ans = []

        while p1 < len(word1) and p2 < len(word2):

            ans.append(word1[p1])
            ans.append(word2[p2])

            p1 += 1
            p2 += 1
        ans.append(word1[l1:])
        ans.append(word2[l2:])
        
        
        return "".join(newstr)