SAFE_DIAL = [d for d in range(0, 100)]

def count_exactly_stop_on_zero(combination_sequence: list[str]):
    n_times_on_zero_tick = 0
    current_tick = 50

    for combination in combination_sequence:
        rotation_direction, ticks = combination[0], int(combination[1:])
        current_tick_position = SAFE_DIAL.index(current_tick)
        if rotation_direction == 'L':
            next_tick = (current_tick_position - ticks) % 100
        else:
            next_tick = (current_tick_position + ticks) % 100

        if SAFE_DIAL.index(next_tick) == 0:
            n_times_on_zero_tick+= 1

        current_tick = next_tick
    print(n_times_on_zero_tick)

def count_pass_through_zero(combination_sequence: list[str]):
    n_times_pass_zero_tick = 0
    current_tick = 50
    for combination in combination_sequence:
        rotation_direction, ticks = combination[0], int(combination[1:])
        if rotation_direction == 'L':
            next_tick = SAFE_DIAL[(current_tick - ticks) % 100]
            passed_through_zero = current_tick - ticks % 100 <= 0 and current_tick != 0
        else:
            next_tick = SAFE_DIAL[(current_tick + ticks) % 100]
            passed_through_zero = current_tick + ticks % 100 > 99
        n_times_pass_zero_tick += ticks // 100 + int(passed_through_zero) 
        
        print(f"comb={combination} - curr={current_tick} - next={next_tick} - n_times_pass_zero={n_times_pass_zero_tick}")
        current_tick = next_tick
    print(n_times_pass_zero_tick)
"""
The dial starts by pointing at 50.
The dial is rotated L68 to point at 82; during this rotation, it points at 0 once.
The dial is rotated L30 to point at 52.
The dial is rotated R48 to point at 0.
The dial is rotated L5 to point at 95.
The dial is rotated R60 to point at 55; during this rotation, it points at 0 once.
The dial is rotated L55 to point at 0.
The dial is rotated L1 to point at 99.
The dial is rotated L99 to point at 0.
The dial is rotated R14 to point at 14.
The dial is rotated L82 to point at 32; during this rotation, it points at 0 once.
"""

if __name__ == '__main__':
    
    input_file = "actual_input.txt"
    
    with open(input_file) as fp:
        combination_sequence = [c.strip() for c in fp.readlines()]

    #count_exactly_stop_on_zero(combination_sequence)
    count_pass_through_zero(combination_sequence)