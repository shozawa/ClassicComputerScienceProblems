from typing import List

a: List[int] = []
b: List[int] = []
c: List[int] = []

num_discs = 25

for i in range(num_discs):
    a.append(i)


def hanoi(start: list, end: list, temp: list, n: int):
    if n == 1:
        end.append(start.pop())
    else:
        hanoi(start, temp, end, n-1)
        hanoi(start, end, temp, 1)
        hanoi(temp, end, start, n-1)


if __name__ == "__main__":
    print(a, b, c)
    hanoi(a, c, b, num_discs)
    print(a, b, c)
