def compute_dna(first_str: str, second_str: str) -> int:
    if len(first_str) != len(second_str):
        raise ValueError

    distance = 0
    for ind in range(len(first_str)):
        if first_str[ind] != second_str[ind]:
            distance += 1
    return distance
