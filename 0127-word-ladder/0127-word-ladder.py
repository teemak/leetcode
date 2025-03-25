from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordset = set(wordList)
        queue = deque([(beginWord, 1)])
        visited = set(beginWord)

        while queue:
            current_word, level = queue.popleft()

            for i in range(len(current_word)):
                for char in map(chr, range(97, 123)):
                    new_word = current_word[:i] + char + current_word[i + 1:]

                    if new_word == endWord:
                        return level + 1

                    if new_word in wordset and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, level + 1))

        return 0