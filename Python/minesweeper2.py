def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for row_idx, row in enumerate(grid):
        for col_idx, val in enumerate(row):
            if val == "#":
                new_grid[row_idx][col_idx] = "#"
                continue

            mine_count = 0
            for direction in directions:
                new_row = row_idx + direction[0]
                new_col = col_idx + direction[1]

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "#":
                    mine_count += 1

            new_grid[row_idx][col_idx] = str(mine_count)

    return new_grid



grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

result = minesweeper(grid)
for row in result:
    print(row)
