def calculate_energy_bill(units: float) -> float:
    if units < 0:
        raise ValueError("Units cannot be negative.")

    # Four electricity slabs
    if units <= 100:
        amount: float = units * 1.50
    elif units <= 200:
        amount = (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 400:
        amount = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        amount = (100 * 1.50) + (100 * 2.50) + (200 * 4.00) + ((units - 400) * 6.00)

    return amount


def get_fixed_charge(category: str) -> float:
    match category.lower():
        case "domestic":
            return 50.0
        case "commercial":
            return 150.0
        case "industrial":
            return 500.0
        case _:
            raise ValueError("Invalid consumer category.")


def print_bill(units: float, category: str, late: bool, online: bool) -> None:
    energy: float = calculate_energy_bill(units)
    fixed: float = get_fixed_charge(category)
    total: float = energy + fixed

    # Apply 5% surcharge only when late and not paid online.
    if late and not online:
        total = total + (total * 0.05)

    # Apply 2% rebate for online payment.
    if online:
        total = total - (total * 0.02)

    print(f"\n{'ELECTRICITY BILL':^35}")
    print(f"{'Units':<20}{units:>10.2f}")
    print(f"{'Category':<20}{category:>10}")
    print(f"{'Energy charge':<20}Rs. {energy:>7.2f}")
    print(f"{'Fixed charge':<20}Rs. {fixed:>7.2f}")
    print(f"{'Total amount':<20}Rs. {total:>7.2f}")


def main() -> None:
    print_bill(170, "domestic", True, False)

    # for loop prints a 12-month statement
    monthly_units: list[float] = [95, 125, 184, 206, 251, 311, 400, 401, 350, 275, 150, 100]
    print(f"\n{'MONTH':<12}{'UNITS':>10}{'ENERGY BILL':>15}")
    for month in range(12):
        bill: float = calculate_energy_bill(monthly_units[month])
        print(f"{month + 1:<12}{monthly_units[month]:>10.2f}{bill:>15.2f}")

    # Required boundary tests
    print(f"\nBOUNDARY TESTS")
    for units in [200, 101, 100, 301, 400, 501]:
        print(f"{units} units = Rs. {calculate_energy_bill(units):.2f}")

    # while loop accepts readings until e is entered
    print(f"\nEnter electricity readings. Type e to stop.")
    while True:
        value: str = input("Enter units: ")
        if value.lower() == "e":
            print(f"Finished entering readings.")
            break

        try:
            units: float = float(value)
            print(f"Energy charge = Rs. {calculate_energy_bill(units):.2f}")
        except ValueError:
            print(f"Invalid reading. Enter a positive number or q.")


if __name__ == "__main__":
    main()
