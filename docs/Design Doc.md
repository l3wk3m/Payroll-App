# Software Design Document

**Payroll processing app**

Luke Maycock

- [Software Design Document](#software-design-document)
  - [Program Overview](#program-overview)
  - [Program Requirements](#program-requirements)
    - [Functional Requirements](#functional-requirements)
    - [Technical Requirements](#technical-requirements)
    - [Input format](#input-format)
      - [Name](#name)
      - [Timetable](#timetable)
      - [Rate](#rate)
      - [Bonuses](#bonuses)
      - [Benefit in Kind](#bik)
    - [Output format](#output-format)
      - [Payroll table](#payroll-table)
  - [Testing Approach](#testing-approach)

## Program Overview

The payroll application is a software that assists users in aggregating payroll related input data from a number of sources into a single datasource and then using that datasource to generate a personalised payslip for each employee into its own Excel file.

The application will be developed using the Python programming language in conjunction with the procedural design philosophy.

## Program Requirements

Stakeholder interviews have highlighted the following project requirements going forward:

### Functional Requirements

- Read hours worked, rate, bonuses, Benefit In Kind and PPSN from input CSVs.
- Calculate employee's salary.
- Add bonuses to pay.
- Calculate taxes and subtract them from salary.
- Generate one csv with all of the gathered and calculated data.
- Use that csv to generate a payslip for every worker based off an Excel template.
- The date the payslip was generated should be included in each payslip.

### Technical Requirements

- Platform: cross-platform (Windows, Linux, MacOS)
- Language: Developed in Python, ensuring wide support and maintainability
- Input: CSV files

### Program Flow

#### Sequence

1. Established the paths of the csv files as PERMANENT VARIABLES.
2. Program reads the data using the 'import csv' library (if individual files this can be sorted into a dict with kv pairs)(otherwise may have to be organised into key-dict dictionaries)

Sample:

given input: {"ppsn": 1234567A, {"name": "John Doe", "hours":12, "rate": 20, "bonuses": 25}}

3. Based on the employee's hourly rate, the program calculates the employee's gross pay.
4. The program calls a function to determine this employee's tax band and their payable tax and saves these values to variables.
5. The program calculates the employee's net pay by subtracting the payable tax from their gross pay plus bonus and benefit in kind. The netpay is added to the dictionary of values.
6. The program calls a function that scans through a template Excel file, inserts the relevant data into the relevant cell and saves it as the payslip for each employee in the Outputs folder. A reference CSV is also saved that stores a dictionary with the calculated value for all employees.

### Input format

#### All

```csv
PPSN, Name, Hours, Rate, Bonus, Benefit In Kind
1234567A, John Doe, 36, 15, 15, 15
```

#### Potential Alternate Format

```csv
PPSN, 1234567A
Name, John Doe
Hours, 36
Rate, 15
Bonus, 15
Benefit In Kind, 15
```

#### Name

```csv
PPSN, Name
1234567A, John Doe
```

#### Timetable

```csv
PPSN, hours
1234567A, 36
```

#### Rate

```csv
PPSN, Rate
1234567A, 15
```

#### Bonuses

```csv
PPSN, Bonus
1234567A, 15
```

#### BIK

```csv
PPSN,BenefitInKind
1234567A, 15
```

### Output format

#### Payroll table

```csv
PPSN,Name,Salary,Bonuses,Taxex,BenefitInKind,NetPay
1234567A,John Doe,100,15,-25,5,95
```

## Testing Approach

The testing approach for this application will consist of manually run and observed tests of certain elements or functions within the application. This is manageable because the scope of the project is small but the ideal approach would have involved unit testing.

Particularly using an IDE like VSCode, Unit Testing provides unique insights into not just whether or not a testing benchmark was hit, but how the program went about doing so, including factors like memory management which is an essential component of the procedural programming paradigm.