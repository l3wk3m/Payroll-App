# Software Design Document

**Payroll processing app**

Luke Maycock

- [Software Design Document](#software-design-document)
  - [Program Overview](#program-overview)
  - [Stakeholders Interviews](#stakeholders-interviews)
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

## Stakeholders Interviews

Stakeholder interviews have uncovered the following project requirements going forward:

- If providing the data in separate csvs they will at least provide one linking piece of data. In the case of this application we have agreed that this will be the employee's ppsn
- If providing employee hours worked we will also need to know their contract type (i.e. whether the employee is paid per hour, per day, per week, per month or per annum)
- 
- The program will be able to calculate the employee's tax band based off their contracted salary or by calculating their gross pay.

## Program Requirements

### Functional Requirements

- Read timetable, rate, bonuses, PPSN from CSV
- Calculate employee's salary
- Calculate taxes and subtract them from salary
- Add bonuses to pay
- Generate one csv with all of the gathered and calculated data
- Use that csv to generate a payslip for every worker based off an Excel template
- The date the payslip was generated should be printed in each payslip

### Technical Requirements

- Platform: cross-platform (Windows, Linux, MacOS)
- Language: Developed in Python, ensuring wide support and maintainability
- Input: CSV files

### Program Flow

#### Sequence

1. Established the paths of the csv files as PERMANENT VARIABLES.
2. Program reads the first row of the csv for the number of values in the row
3. If the second item in the row is a string, this is formatted with a header
4. If the second value is an int, the csv is formatted with headers on the left
5. Program reads the data with 'import csv' library (if individual files this can be sorted into a dict with kv pairs)(otherwise may have to be organised into key-dict dictionaries)

Sample:

given input: {"ppsn": 1234567A, {"name": "John Doe", "hours":12, "rate": 20, "bonuses": 25}}

6. Based on the employee's hourly rate, the program calculates the employee's gross pay.
7. The program calls a function to determine this employee's tax band and their payable tax and saves these values to variables.
8. The program calculates the employee's net pay by subtracting the payable tax from their gross pay.

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