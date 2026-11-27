def check_credit_score(score: int) -> tuple[str, float]:
    # match/case 
    match score:
        case x if x >= 800:
            return "Excellent", 8.5
        case x if x >= 750:
            return "Good", 9.5
        case x if x >= 700:
            return "Fair", 11.0
        case x if x >= 650:
            return "Low", 13.5
        case _:
            return "Poor", 0.0


def check_applicant(applicant: dict) -> str:
    age: int = applicant["age"]
    income: float = applicant["income"]
    emi: float = applicant["emi"]
    score: int = applicant["score"]
    job: str = applicant["job"]
    loans: int = applicant["loans"]

    if age < 0:
        return "Invalid age"
    elif age < 21 or age > 60:
        return "Rejected: age must be 21-60"
    elif income <= 0:
        return "Invalid income"
    elif score < 300 or score > 900:
        return "Invalid credit score"
    elif emi < 0 or loans < 0:
        return "Invalid EMI or loan count"
    elif emi / income > 0.50:
        return "Rejected: EMI is too high"
    elif score < 650:
        return "Rejected: low credit score"
    elif job not in ["salaried", "self-employed"]:
        return "Rejected: invalid employment type"
    elif job == "self-employed" and score < 700:
        return "Rejected: self-employed score must be 700+"
    elif loans > 2:
        return "Rejected: more than 2 existing loans"
    else:
        return "Approved"


def main() -> None:
    applicants: list[dict] = [
        {"name": "Aarav", "age": 28, "income": 60000, "emi": 12000, "score": 820, "job": "salaried", "loans": 1},
        {"name": "Diya", "age": 35, "income": 50000, "emi": 26000, "score": 780, "job": "salaried", "loans": 2},
        {"name": "Kabir", "age": 19, "income": 45000, "emi": 5000, "score": 760, "job": "salaried", "loans": 0},
        {"name": "Meera", "age": 42, "income": 80000, "emi": 20000, "score": 720, "job": "self-employed", "loans": 1},
        {"name": "Ishaan", "age": 31, "income": 0, "emi": 0, "score": 800, "job": "salaried", "loans": 0},
        {"name": "Anaya", "age": 50, "income": 90000, "emi": 25000, "score": 680, "job": "salaried", "loans": 1},
        {"name": "Vihaan", "age": 29, "income": 70000, "emi": 15000, "score": 790, "job": "contract", "loans": 0},
        {"name": "Sara", "age": 61, "income": 65000, "emi": 10000, "score": 810, "job": "salaried", "loans": 0},
        {"name": "Rohan", "age": 38, "income": 75000, "emi": 18000, "score": 850, "job": "self-employed", "loans": 1},
        {"name": "Tara", "age": 26, "income": 55000, "emi": 10000, "score": 740, "job": "salaried", "loans": 1},
    ]

    approval_count: int = 0
    approval_limit: int = 3

    print(f"{'NAME':<10} {'DECISION':<15} {'CREDIT BAND':<12} {'RATE':<8}")
    print("-" * 50)

    for person in applicants:
        decision: str = check_applicant(person)

      
        if decision.startswith("Invalid"):
            print(f"{person['name']:<10} {decision:<30}")
            continue

        
        if decision == "Approved" and approval_count == approval_limit:
            print(f"Daily approval limit of {approval_limit} reached.")
            break

        band: str
        rate: float
        band, rate = check_credit_score(person["score"])

        if decision == "Approved":
            approval_count += 1

        print(f"{person['name']:<10} {decision:<30} {band:<12} {rate:.2f}%")
    else:
        print(f"All {len(applicants)} applicants were checked.")

    print(f"Total approvals: {approval_count}")


if __name__ == "__main__":
    main()
