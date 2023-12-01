def first_last(s: str) -> int:
    i = 0
    j = len(s) - 1
    x1, x2 = (None, None)
    while i <= j:
        c1 = s[i]
        c2 = s[j]
        if x1 is None:
            if c1.isnumeric():
                x1 = c1
            else:
                i += 1
        if x2 is None:
            if c2.isnumeric():
                x2 = c2
            else:
                j -= 1
        if x1 is not None and x2 is not None:
            break
    return int(f"{x1}{x2}")


def solution(arr: list[str]) -> int:
    return sum(first_last(s) for s in arr)

if __name__ == "__main__":
    with open("day1.txt", "r") as f:
        input = f.readlines()
    print(solution(input))
   



