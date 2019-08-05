def fib(n: int) -> int:
    last = 0
    following = 1
    for _ in range(1, n):
        last, following = following, last + following
    return following


if __name__ == "__main__":
    print(fib(5))
    print(fib(50))
