from pathlib import Path
import sys

def get_separator_line(lines: list[str]):
    l = 0
    for line in lines:
        if line == "":
            break
        l += 1
    return l

def make_range(range_of_ids):
    low_end = int(range_of_ids.split("-")[0])
    high_end = int(range_of_ids.split("-")[1]) + 1
    return range(low_end, high_end)

if __name__ == "__main__":

    filename = Path("dev_input.txt")
    filename = Path("actual_input.txt")
    output_path = Path(f"result_{__file__}") 

    try:
        with filename.open() as fp:
            input = [l.strip() for l in fp.readlines()]
    except FileNotFoundError:
        print(f"Could not find {filename}")
        sys.exit(1)

    sep_line = get_separator_line(input)
    db_ids = [make_range(rg) for rg in input[:sep_line]]
    available_ingredients_ids = map(int, input[sep_line+1:])
    count_fresh = 0
    for ingredient in available_ingredients_ids:
        for rg in db_ids:
            if ingredient in rg:
                count_fresh += 1
                break
    print(count_fresh)
    #with output_path.open("w") as fp:
    #    for i,r in enumerate(accessible_rolls_matrix):
    #        line = f"{"".join(map(str,r))}\n"
    #        if i == len(accessible_rolls_matrix) - 1:
    #            line = f"{"".join(map(str,r))}"
    #        fp.write(line)