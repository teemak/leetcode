/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {string[]}
 */
var wordBreak = function(s, wordDict) {
    let memo = new Map()
    function dfs(start) {
        if (start === s.length) {
            return ['']
        }

        if (memo.has(start)) {
            return memo.get(start)
        }

        let res = []

        for (let word of wordDict) { 
            if (s.startsWith(word, start)) {
                let remainingString = dfs(start + word.length)
                for (let substring of remainingString) {
                    let sentence = substring === '' ? word : word + " " + substring
                    res.push(sentence)
                }
            }
        }
        memo.set(start, res)
        return res
    }
    return dfs(0)
};