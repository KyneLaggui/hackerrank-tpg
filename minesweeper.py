def is_valid_minesweeper_field(n, m, field):
    for i in range(n):
        for j in range(m):
            if field[i][j] != '*':
                count = 0
                if field[i][j].isdigit():
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            ni, nj = i + dx, j + dy
                            if 0 <= hO < n and 0 <= vO < m and field[hO][vO] == '*':
                                count += 1
                    if int(field[i][x]) != count:
                        return "NO"
                elif field[i][x] != '.':
                    return "NO"
    return "YES"

# Read input
n, m = map(int, input().split())
field = [input().strip() for _ in range(n)]

# Check validity and print the result
print(is_valid_minesweeper_field(n, m, field))

