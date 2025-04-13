class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in map(chr, range(97, 123)):
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in wordset:
                        wordset.remove(next_word)
                        queue.append((next_word, length + 1))

        return 0