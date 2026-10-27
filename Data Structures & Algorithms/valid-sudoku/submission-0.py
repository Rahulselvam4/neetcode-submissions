class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        column = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                k = (i//3)*3 + (j//3)
                if num in row[i] or num in column[j] or num in box[k]:
                    return False
                row[i].add(num)
                column[j].add(num)
                box[k].add(num)
        return True
