class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize existing numbers and collect all empty cell positions
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)
                else:
                    empty_cells.append((r, c))

        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True  # All empty cells filled

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for digit in map(str, range(1, 10)):
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_idx]:
                    # Place digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    if backtrack(index + 1):
                        return True

                    # Undo placement (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)

            return False

        backtrack(0)