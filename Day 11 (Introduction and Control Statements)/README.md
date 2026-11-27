# Set 1 - Loan Eligibility Checker

## Project Description

The Loan Eligibility Checker is a Python application that evaluates loan applicants based on their age, income, EMI ratio, credit score, employment type, and existing loans.

The system determines whether an applicant is eligible for a loan and assigns an appropriate loan product and interest rate.

## Objectives

- Create a Python project with a virtual environment.
- Use type hints for local variables.
- Use f-strings for output statements.
- Apply conditional statements and nested conditions.
- Use `match` / `case` to select loan products.
- Process multiple applicants using loops.
- Handle invalid inputs and edge cases.

## Technologies Used

- Python 3.10 or later
- PyCharm
- Virtual Environment

## Project Structure

```text
Loan_Eligibility_Checker/
│
├── .venv/
├── main.py
└── README.md
```

##  Business Rules

The application evaluates applicants using the following rules:

1. Age must be between 21 and 60.
2. Income-to-EMI ratio must satisfy the defined eligibility threshold.
3. Credit score must fall within the valid range.
4. Employment type must be accepted.
5. Existing loans must not exceed the permitted limit.
6. The final loan decision depends on all eligibility conditions.

The exact income-to-EMI thresholds, credit-score bands, interest rates, and approval limit should be defined in the program.

## Python Concepts Used

- Variables and type hints
- Data types
- f-strings
- `if-elif-else`
- Nested conditions
- `match` / `case`
- `for` loop
- `break`
- `continue`
- Loop `else`
- List of applicants
- Input validation

##  Execution

Create and activate a virtual environment.

```bash
python -m venv .venv
```

Activate the environment on Windows:

```bash
.venv\Scripts\activate
```

Run the program:

```bash
python main.py
```

##  Expected Output

The program displays applicant details, eligibility status, loan product, interest rate, and final approval decision.


## Conclusion

This project demonstrates the use of Python conditional statements, loops, pattern matching, type hints, and input validation to implement a basic loan eligibility 



# Set 2 - Utility Billing Calculator

##  Project Description

The Utility Billing Calculator is a Python application that calculates electricity bills based on consumption slabs, consumer categories, late-payment surcharges, and online-payment rebates.

The system generates monthly electricity bills and maintains a consumption statement for twelve months.

## Objectives

- Calculate electricity charges using four consumption slabs.
- Apply fixed charges based on consumer category.
- Calculate late-payment surcharge.
- Apply online-payment rebate.
- Generate a twelve-month consumption statement.
- Accept readings until the user enters `q`.
- Handle invalid readings and display formatted bills.

## Technologies Used

- Python 3.10 or later
- PyCharm

## Project Structure

```text
Utility_Billing_Calculator/
│
├── main.py
└── README.md
```

## Business Rules

Electricity consumption is divided into four slabs:

| Consumption | Slab |
|---|---|
| 0–100 units | First slab |
| 101–200 units | Second slab |
| 201–400 units | Third slab |
| Above 400 units | Fourth slab |

The bill includes:

- Energy charge
- Fixed charge
- Late-payment surcharge, if applicable
- Online-payment rebate, if applicable

The slab rates, fixed charges, surcharge percentage, and rebate percentage should be defined in the program.

## Python Concepts Used

- Variables and data types
- Type hints
- f-strings
- Format specifiers
- `if-elif-else`
- `match` / `case`
- Arithmetic operators
- Comparison operators
- Logical operators
- Operator precedence
- `for` loop
- `while` loop
- Input validation
- Exception handling

## Execution

Run the program:

```bash
python main.py
```

##  Expected Output

The program displays:

- Consumer details
- Consumer category
- Units consumed
- Energy charges
- Fixed charges
- Surcharge or rebate
- Final electricity bill

The bill should be formatted with aligned columns and two decimal places.



## Conclusion

This project demonstrates the use of Python conditional statements, loops, pattern matching, arithmetic operations, operator precedence, and formatted output in an electricity billing application.



#  Set 3 - Insurance Premium Bands

## Project Description

The Insurance Premium Bands application calculates insurance premiums based on an applicant's age, smoking status, BMI, and policy term.

The system classifies applicants into premium bands and applies additional premium loadings based on risk factors.

## Objectives

- Calculate BMI using height and weight.
- Classify BMI into four categories.
- Assign loading percentages using nested conditions.
- Determine base premiums using `match` / `case` with guards.
- Calculate the final premium using operators.
- Process eight applicants using a loop.
- Handle invalid records and type-conversion errors.

## Technologies Used

- Python 3.10 or later
- PyCharm

##  Project Structure

```text
Insurance_Premium_Bands/
│
├── main.py
└── README.md
```

## Business Rules

BMI is calculated using the formula:

BMI = Weight in kilograms / (Height in metres × Height in metres)

BMI classification:

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 to below 25 | Normal |
| 25 to below 30 | Overweight |
| 30 or above | Obese |

The insurance premium depends on:

- Applicant's age
- BMI category
- Smoker status
- Policy term

The base premium and loading percentages should be defined in the program.

## Python Concepts Used

- Variables and type hints
- Data types
- Type conversion
- f-strings
- Arithmetic operators
- Comparison operators
- Logical operators
- Operator precedence
- Nested `if` statements
- `match` / `case` with guards
- `for` loop
- `break`
- Loop `else`
- Lists
- Exception handling

## Execution

Run the program:

```bash
python main.py
```

## Expected Output

The program displays:

- Applicant details
- Age band
- BMI value
- BMI category
- Smoker status
- Base premium
- Loading percentage
- Final premium
- Eligibility decision


## Type Conversion Error Handling

The program should demonstrate conversion errors such as:

- Converting a non-numeric string to an integer.
- Converting an empty string to an integer.

Python raises a `ValueError` for these invalid conversions. The program should handle the exception using `try-except` and display an appropriate error message.

## Conclusion

This project demonstrates the use of Python conditional statements, pattern matching with guards, loops, type conversion, exception handling, and mathematical calculations to implement an insurance premium classification system.

system.

