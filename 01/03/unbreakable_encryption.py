from secrets import token_bytes
from typing import Tuple


def random_key(length: int) -> int:
    tb = token_bytes(length)
    return int.from_bytes(tb, "big")


def encrypt(original: str) -> Tuple[int, int]:
    original_bytes = original.encode()
    original_key = int.from_bytes(original_bytes, "big")
    dummy = random_key(len(original_bytes))
    encrypted = original_key ^ dummy
    return encrypted, dummy


def decrypt(key1: int, key2: int) -> str:
    decrypted = key1 ^ key2
    temp = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")
    return temp.decode()


if __name__ == "__main__":
    key1, key2 = encrypt("One Time Pad!")
    print(decrypt(key1, key2))
