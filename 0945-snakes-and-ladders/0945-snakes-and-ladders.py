class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        mapping, visited = [-1], {1}
        queue = [(1,0)]

        for i, row in enumerate(reversed(board), start=1):
            vals = row if i % 2 != 0 else row[::-1]
            mapping.extend(vals)

        last = len(board)**2

        while queue:
            pos, moves = queue.pop(0)

            if pos == last:
                return moves

            max_move = min(pos + 7, last + 1)

            for next in range(pos + 1, max_move):
                if mapping[next] != -1:
                    dest = mapping[next]
                else:
                    dest = next
                if dest not in visited:
                    visited.add(dest)
                    queue.append((dest, moves + 1))
        
        return -1