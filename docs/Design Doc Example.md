# Software Design Document - Example

**Payroll processing app**

Student name

- [Software Design Document - Example](#software-design-document---example)
  - [Program Overview](#program-overview)
  - [Program Requirements](#program-requirements)
    - [Functional Requirements](#functional-requirements)
    - [Technical Requirements](#technical-requirements)
    - [Input format](#input-format)
      - [PPSN](#ppsn)
      - [Timetable](#timetable)
      - [Rate](#rate)
      - [Bonuses](#bonuses)
      - [Rate](#rate-1)
    - [Output format](#output-format)
      - [Payroll table](#payroll-table)
  - [Testing Approach](#testing-approach)

## Program Overview

The payroll application is a software that assists users in ~~doing things~~. Users can do ~~(a list of build in operation)~~. The software aims to provide a simple and efficient way to ~~(a list of advantages that user can get using this application)~~.

The application will be developed using the Python programming language in conjunction with the procedural design philosophy.

## Program Requirements

### Functional Requirements

- Read timetable, rate, bonuses, gift card data, PPSN ~~(etc.)~~ from CSV
- Calculate salary
- Add taxes to salary
- Add bonuses
- Add gift card amount
- Pivot table with all the calculated data
- Payslip for every worker

### Technical Requirements

- Platform: cross-platform (Windows, Linux, MacOS)
- Language: Developed Python, ensuring wide support and maintainability
- Database: CSV files

### Input format

#### PPSN

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

#### Rate

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

The approach to testing this application will be multifaceted but primarily focus on the concept of unit test, where ~~(every function what?)~~.
