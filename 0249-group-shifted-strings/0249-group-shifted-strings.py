class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strings:
            if len(word) == 1:
                key = ()
            else:
                key = []

                for i in range(1, len(word)):
                    current_char = word[i]
                    previous_char = word[i - 1]
                    diff = (ord(current_char) - ord(previous_char)) % 26
                    key.append(diff)
                key = tuple(key)
            result[key].append(word)
        return list(result.values())