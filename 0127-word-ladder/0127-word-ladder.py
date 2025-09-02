class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # unique chars
        wordset = set(wordList)
        # not possible 
        if endWord not in wordList:
            return 0
        # traversal and count
        queue = deque([(beginWord, 1)])        

        while queue:
            word, length = queue.popleft()
            # happy case
            if word == endWord:
                return length
            # ???
            for i in range(len(word)):
                for c in map(chr, range(97, 123)):
                    nextWord = word[:i] + c + word[i + 1:]

                    if nextWord in wordset:
                        wordset.remove(nextWord)
                        queue.append((nextWord, length + 1))

        return 0