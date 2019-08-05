from typing import Generator


def fib(n: int) -> Generator[int, None, None]:
    last = 0
    following = 1
    for _ in range(1, n):
        last, following = following, last + following
        yield following


if __name__ == "__main__":
    for n in fib(50):
        print(n)
