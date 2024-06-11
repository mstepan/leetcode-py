import math


def main():
    val1 = 10_000_000
    print(f"is_prime({val1}): {is_prime(val1)}")

    val2 = 10_000_019
    print(f"is_prime({val2}): {is_prime(val2)}")

    print(f"calculate: {calculate(10, 10, 10, 5, 10, 10)}")

    print("main done...")


def calculate(
    gross_wages,
    taxable_interest,
    dividends,
    qualified_dividends,
    ira_deduction,
    student_loan_interest,
):
    income = (
        gross_wages
        + taxable_interest
        + (dividends - qualified_dividends)
        - ira_deduction
        - student_loan_interest
    )
    return income


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
