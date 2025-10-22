def luckyNumbers(matrix):
    min_in_row = [min(row) for row in matrix]
    max_in_col = [max(col) for col in zip(*matrix)]
    lucky = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == min_in_row[i] and matrix[i][j] == max_in_col[j]:
                lucky.append(matrix[i][j])
    return lucky

# Example usage
matrix = [
    [3, 7, 8],
    [9, 11, 13],
    [15, 16, 17]
]
print("Lucky Numbers:", luckyNumbers(matrix))
