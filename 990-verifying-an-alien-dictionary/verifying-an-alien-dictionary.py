class Solution:
    def isAlienSorted(self, words, order):
        rank = {c: i for i, c in enumerate(order)}
        def transform(word):
            return [rank[c] for c in word]
        return all(transform(words[i]) <= transform(words[i+1]) for i in range(len(words)-1))