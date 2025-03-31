'''
   2      2     1     2     1    0
["eat",  "tea","tan","ate","nat","bat"]
   0       1     1       1     1     1
[["bat"],["nat","tan"],["ate","eat","tea"]]

{
    abt: [bat],
    aet: [ate, eat, tea]
    ant: [nat, tan]
}

constraints: 
    1 <= wordList <= 100_000
    0 <= word_length <= 100
    only lowercase English letters

plan:                                                                                               time:       space
1. use a dict to store key/vals, keys are chars that make up sorted(word[i]) - vals are word[i] ** O(n*mlogm)   O(n)
2. naive is to compare word to word[i], need to compare against every word                      ** O(w*l)       O(n)
3. hashing character counts                                                                        O(w*l)       O(w*l)
4. generate primes that map to characters                                                          O(w*l)       O(n)        
5. bitmasking                                                                                      O(n*m)       O(n)
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            bitmask = [0] * 26

            for char in word:
                bitmask[ord(char) - ord('a')] += 1

            key = tuple(bitmask)
            groups[key].append(word)

        return list(groups.values())