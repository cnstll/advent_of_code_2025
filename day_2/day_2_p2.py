from pathlib import Path
import sys
def has_repeating_serie(id_seq: str) -> bool:
    """Find the highest number repeating within the id."""
    subseq_sizes = [size for size in range(len(id_seq) // 2, 0, -1) if len(id_seq) % size == 0] 

    for len_comp_seq in subseq_sizes:
        sub_seq = [id_seq[i:i + len_comp_seq] for i in range(0, len(id_seq) - len_comp_seq + 1, len_comp_seq)]
        if len(set(sub_seq)) == 1:
            return True 
    return False
        
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
            if has_repeating_serie(str(id)):
                invalid_ids.append(id)
    output_path = Path("result") 
    with output_path.open("w") as fp:
        fp.write(str(sum(invalid_ids)))