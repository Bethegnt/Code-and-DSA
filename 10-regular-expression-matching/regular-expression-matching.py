class Solution:
    def isMatch(self, s: str, p: str) -> bool:  
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s_char = s[i - 1]
                p_char = p[j - 1]
                if p_char != '*':
                    if p_char == s_char or p_char == '.':
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    prev_p_char = p[j - 2]
                    zero_matches = dp[i][j - 2]
                    one_or_more_matches = False
                    if s_char == prev_p_char or prev_p_char == '.':
                        one_or_more_matches = dp[i - 1][j]
                    dp[i][j] = zero_matches or one_or_more_matches
        return dp[m][n]
