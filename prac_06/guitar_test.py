from prac_06.guitar import Guitar


def run_test():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other = Guitar("Another Guitar", 2013, 1456.9)

    print(f"{gibson.name} get_age() - Expected 103. Got {gibson.get_age}")
    print(f"Other {other.name} get_age() - Expected 93. Got {other.get_age}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage}")
    print(f"{other.name} is_vintage() - Expected False. Got {other.is_vintage}")

run_test()