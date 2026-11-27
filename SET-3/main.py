def calculate_bmi(height: float, weight: float) -> float:
    return weight / (height * height)


def get_bmi_loading(bmi: float) -> tuple[str, float]:
    # classifies BMI
    if bmi < 18.5:
        return "Underweight", 3
    elif bmi < 25:
        return "Normal", 0
    elif bmi < 30:
        return "Overweight", 10
    else:
        return "Obese", 20


def get_base_premium(age: int, term: int) -> float:
    # match/case selects the premium by age
    match age:
        case x if 18 <= x <= 30:
            premium: float = 5000
        case x if 31 <= x <= 45:
            premium = 7000
        case x if 46 <= x <= 60:
            premium = 10000
        case _:
            raise ValueError("Age must be between 18 and 60.")

    # Policy term changes the base premium
    match term:
        case x if 1 <= x <= 10:
            premium = premium * 1.00
        case x if 11 <= x <= 20:
            premium = premium * 1.15
        case x if 21 <= x <= 30:
            premium = premium * 1.30
        case _:
            raise ValueError("Term must be between 1 and 30 years.")

    return premium


def main() -> None:
    applicants: list[dict] = [
        {"name": "Harini", "age": 25, "height": 1.75, "weight": 68, "smoker": False, "term": 10},
        {"name": "Nithis", "age": 26, "height": 1.62, "weight": 80, "smoker": False, "term": 15},
        {"name": "Kabir", "age": 47, "height": 1.70, "weight": 92, "smoker": False, "term": 20},
        {"name": "Meera", "age": 55, "height": 1.60, "weight": 78, "smoker": True, "term": 25},
        {"name": "Kathir", "age": 29, "height": 1.80, "weight": 55, "smoker": False, "term": 12},
        {"name": "Anaya", "age": 41, "height": 1.65, "weight": 63, "smoker": False, "term": 20},
        {"name": "Vihaan", "age": 17, "height": 1.72, "weight": 66, "smoker": False, "term": 10},
        {"name": "Thiyagu", "age": 32, "height": 1.58, "weight": 95, "smoker": True, "term": 30},
    ]

    print(f"{'NAME':<10}{'BMI':>8}{'CATEGORY':<15}{'FINAL PREMIUM':>18}")
    print("-" * 51)

    # Process all eight applicants
    for person in applicants:
        try:
            if person["height"] <= 0 or person["weight"] <= 0:
                raise ValueError("Height and weight must be positive.")

            bmi: float = calculate_bmi(person["height"], person["weight"])
            category: str
            bmi_loading: float
            category, bmi_loading = get_bmi_loading(bmi)

            base: float = get_base_premium(person["age"], person["term"])

            # Percentage  = BMI loading + smoker loading
            smoker_loading: float = 25 if person["smoker"] else 0
            total_loading: float = bmi_loading + smoker_loading
            final_premium: float = base + (base * total_loading / 100)

            print(f"{person['name']:<10}{bmi:>8.2f}{category:<15}{final_premium:>18.2f}")

        except ValueError as error:
            print(f"{person['name']:<10} Ineligible: {error}")
            print(f"Batch stopped because an applicant is invalid.")
            break
    else:
        print(f"All applicants passed validation.")

    # Type conversion
    print(f"\nTYPE CONVERSION TESTS")
    for value in ["25", "abc", ""]:
        try:
            age: int = int(value)
            print(f"{value!r} converted to {age}.")
        except ValueError:
            print(f"{value!r} cannot be converted to an integer.")


if __name__ == "__main__":
    main()
