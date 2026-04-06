class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        for letter in strs:
            sortedWord = ''.join(sorted(letter))
            anagramMap[sortedWord].append(letter)
        return list(anagramMap.values())    
        