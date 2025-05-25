class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        answer = 0 
        central = False
        for word, countwords in count.items():
            if word[0] == word[1]:
                if countwords % 2 == 0:
                    answer += countwords
                else:
                    answer += countwords - 1
                    central = True
            elif word[0] < word[1]:
                answer += 2 * min(countwords, count[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer
            