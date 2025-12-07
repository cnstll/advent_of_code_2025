from pathlib import Path
import sys

def get_matrix_size(matrix: list[list[int]]) -> tuple[int, int]:
    row_len = len(matrix)
    column_len = len(matrix[0]) if len(matrix) > 0 else 0
    return row_len, column_len

def pad_matrix(matrix: list[list[int]], pad = 1):
    padded_matrix = []
    r,c = get_matrix_size(matrix)
    target_matrix_size = (r + 2 * pad, c + 2 * pad)

    full_pad = [0 for i in range(target_matrix_size[1])]
    padded_matrix.append(full_pad)
    for i in range(0, r):
        row = []
        for j in range(0, target_matrix_size[1]):
            row.append(matrix[i][j - 1] if j != 0 and j != target_matrix_size[1] - 1 else 0)
        padded_matrix.append(row)

    padded_matrix.append(full_pad)
    return padded_matrix

def compute_convolution(matrix, center):
    sum = 0
    upper_left_corner = (center[0] - 1,center[1] - 1)
    lower_right_corner = (center[0] + 1,center[1] + 1)
    for i in range(upper_left_corner[0], lower_right_corner[0]+ 1):
        for j in range(upper_left_corner[1], lower_right_corner[1] + 1):
            sum += matrix[i][j] if (i, j) != center else 0
    return sum

def apply_convolution(matrix: list[list[int]], padding = 1):
    r, c = get_matrix_size(matrix)
    convolved_matrix = []
    for i in range(padding, r - padding):
        row = [compute_convolution(matrix, (i, j)) for j in range(padding, c - padding)]
        convolved_matrix.append(row)

    return convolved_matrix

def remove_accesible_rolls(binary_matrix, convolved_matrix, padding = 1):
    r, c = get_matrix_size(binary_matrix)
    cleared_rolls_matrix = []
    for i in range(0, r):
        row = []
        for j in range(0, c):
            row.append(0 if convolved_matrix[i][j] < 4 and binary_matrix[i][j] == 1 else binary_matrix[i][j])
        cleared_rolls_matrix.append(row)
    return cleared_rolls_matrix

def count_rolls(binary_matrix):
    r, c = get_matrix_size(binary_matrix)
    counter = 0
    for i in range(0, r):
        counter += sum(binary_matrix[i]) 
    return counter

if __name__ == "__main__":

    #filename = Path("dev_input.txt")
    filename = Path("actual_input.txt")
    output_path = Path("result") 

    try:
        with filename.open() as fp:
            roll_matrix = [row.strip() for row in fp.readlines()]

    except FileNotFoundError:
        print(f"Could not find {filename}")
        sys.exit(1)

    binary_matrix = [list(0 if roll == "." else 1 for roll in row) for row in roll_matrix]

    removed_rolls = -1 
    total_removed = 0
    while removed_rolls != 0:
        n_rolls = count_rolls(binary_matrix)
        padded_matrix = pad_matrix(binary_matrix)
        convolved_matrix = apply_convolution(padded_matrix)
        accessible_rolls_matrix = remove_accesible_rolls(binary_matrix, convolved_matrix)
        removed_rolls = n_rolls - count_rolls(accessible_rolls_matrix)
        binary_matrix = accessible_rolls_matrix
        total_removed += removed_rolls

    print("total_removed", total_removed)
    #print(roll_matrix[0])
    #print(accessible_rolls_matrix[0])
    #print("..xx.xx@x.")

    #with output_path.open("w") as fp:
    #    for i,r in enumerate(accessible_rolls_matrix):
    #        line = f"{"".join(map(str,r))}\n"
    #        if i == len(accessible_rolls_matrix) - 1:
    #            line = f"{"".join(map(str,r))}"
    #        fp.write(line)