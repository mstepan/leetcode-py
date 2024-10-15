import math


def main():
    val1 = 10_000_000
    print(f"is_prime({val1}): {is_prime(val1)}")

    val2 = 10_000_019
    print(f"is_prime({val2}): {is_prime(val2)}")

    print("main done...")


def is_prime(value: int) -> bool:
    # -5, -1, 0, 1,
    if value < 2:
        return False

    boundary: int = math.ceil(math.sqrt(value)) + 1

    for factor in range(2, boundary):
        if value % factor == 0:
            # value is composite, not prime
            return False

    return True


if __name__ == "__main__":
    main()
