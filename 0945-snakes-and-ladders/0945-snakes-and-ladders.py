class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        mapping, visited = [-1], {1}
        queue, moves = [1], 0

        for i, row in enumerate(board[::-1], start = 1):
            mapping += row if i % 2 else row[::-1]

        end = len(board)**2

        while queue:
            for _ in range(len(queue)):
                pos = queue.pop(0)

                if pos == end:
                    return moves

                for roll in range(1, 7):
                    next = pos + roll

                    if next > end:
                        continue

                    if mapping[next] == -1:
                        dest = next
                    else:
                        dest = mapping[next]

                    if dest not in visited:
                        visited.add(dest)
                        queue.append(dest)

            moves += 1

        return -1