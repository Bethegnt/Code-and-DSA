class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            char_counts = Counter(s).items()
            immutable_key = frozenset(char_counts)
            anagram_map[immutable_key].append(s)
        return list(anagram_map.values())