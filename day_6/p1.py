from pathlib import Path
from functools import reduce
import sys

if __name__ == "__main__":

    filename = Path("dev_input.txt")
    filename = Path("actual_input.txt")
    output_path = Path("result") 

    try:
        with filename.open() as fp:
            matrix = [row.strip().split() for row in fp.readlines()]
        matrix_numbers, vec_operations = matrix[:-1], matrix[-1]
        results = []
        for i in range(len(vec_operations)):
            numbers = [int(matrix_numbers[j][i]) for j in range(len(matrix_numbers))]
            match vec_operations[i]:
                case "+":
                    op = sum(numbers)
                case "*":
                    op = reduce(lambda x, y: x*y, numbers)
                case _:
                    raise ValueError(f"unknown operation: {vec_operations[i]}")

            results.append(op)

    except FileNotFoundError:
        print(f"Could not find {filename}")
        sys.exit(1)
    with output_path.open("w") as fp:
        fp.write(str(sum(results)))