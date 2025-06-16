# Time Complexity : O(1), since the board size is fixed at 9x9
# Space Complexity : O(1), constant extra space for 9 rows, 9 cols, 9 boxes
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : No

from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # HashSet Approach

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)  # Key is (r//3, c//3) to identify 3x3 boxes

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                if (
                    val in rows[r] or
                    val in cols[c] or
                    val in boxes[(r // 3, c // 3)]
                ):
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3, c // 3)].add(val)

        return True

        # ------------------------------------------------------------
        # Alternative Approach: Using arrays instead of sets (commented out)
        # Time Complexity: O(1) – constant time since the board is always 9x9
        # Space Complexity: O(1) – three 9x9 arrays, each with fixed size (81 elements max)

        # rows = [[0] * 9 for _ in range(9)]
        # cols = [[0] * 9 for _ in range(9)]
        # boxes = [[0] * 9 for _ in range(9)]

        # for r in range(9):
        #     for c in range(9):
        #         val = board[r][c]
        #         if val == ".":
        #             continue

        #         num = int(val) - 1
        #         box_idx = (r // 3) * 3 + (c // 3)

        #         if rows[r][num] or cols[c][num] or boxes[box_idx][num]:
        #             return False

        #         rows[r][num] = 1
        #         cols[c][num] = 1
        #         boxes[box_idx][num] = 1

        # return True


# Optional: Example test runs
if __name__ == "__main__":
    # Valid Sudoku board
    board_valid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    
    # Invalid Sudoku board (duplicate '8' in the top-left 3x3 box)
    board_invalid = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    sol = Solution()
    print("Valid board result:", sol.isValidSudoku(board_valid))    # Output: True
    print("Invalid board result:", sol.isValidSudoku(board_invalid))  # Output: False

