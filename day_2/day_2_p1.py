from pathlib import Path
import sys
def has_repeating_serie(id: int) -> bool:
    id_seq = str(id)

    if len(id_seq) % 2 != 0:
        return False

    max_len_sub_seq = len(id_seq) // 2
    return id_seq[0:max_len_sub_seq] == id_seq[max_len_sub_seq:]
        
if __name__ == "__main__":

    filename = Path("actual_input.txt")

    try:
        with filename.open() as fp:
            id_ranges = fp.read().split(",")

    except FileNotFoundError:
        print(f"Could not find {filename}")
        sys.exit(1)
    invalid_ids = [] 
    for id_range in id_ranges:
        lower_bound, upper_bound = map(int, id_range.split("-"))
        for id in range(lower_bound, upper_bound + 1):
            if has_repeating_serie(id) and str(id)[0] != "0":
                invalid_ids.append(id)
    output_path = Path("result") 
    with output_path.open("w") as fp:
        fp.write(str(sum(invalid_ids)))