class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        def dfs(index, path):
            if index == len(digits):
                result.append(path)
                return
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                dfs(index + 1, path + letter)
        dfs(0, "")
        return result
