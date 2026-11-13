import math


def _to_number(value):
    """Convert text to a finite, non-negative float. Return None if invalid."""
    try:
        number = float(value.strip())
    except (ValueError, AttributeError):
        return None
    if not math.isfinite(number) or number < 0:
        return None
    return number


def parse_collection(text):
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    material = parts[0].strip()
    kg = _to_number(parts[1])
    if material == "" or kg is None:
        return None
    return material.title(), kg


def weight_average(weights_csv):
    if not isinstance(weights_csv, str) or weights_csv.strip() == "":
        return None
    values = []
    for item in weights_csv.split(','):
        number = _to_number(item)
        if number is None:
            return None
        values.append(number)
    average = sum(values) / len(values)
    return average if math.isfinite(average) else None


def net_points(text):
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    points = _to_number(parts[0])
    penalty = _to_number(parts[1])
    if points is None or penalty is None:
        return None
    total = points * 2 - penalty
    if not math.isfinite(total):
        return None
    return max(total, 0)


def main():
    print("==== Running parse_collection ====")
    user_input = input("Enter material:weight in kg (e.g. paper:12): ")
    result = parse_collection(user_input)
    print("Material and Weight:", result if result is not None else "Invalid input")

    print("\n==== Running weight_average ====")
    user_input = input("Enter weights in kg as CSV (e.g. 5,12,20): ")
    result = weight_average(user_input)
    print("Average Weight:", result if result is not None else "Invalid input")

    print("\n==== Running net_points ====")
    user_input = input("Enter points|penalty (e.g. 80|10): ")
    result = net_points(user_input)
    print("Net Points:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()