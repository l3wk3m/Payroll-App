# Software Design Document

**Payroll processing app**

Student name

- [Software Design Document - Example](#software-design-document---example)
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

The payroll application is a software that assists users in ~~doing things~~. Users can do ~~(a list of build in operation)~~. The software aims to provide a simple and efficient way to ~~(a list of advantages that user can get using this application)~~.

The application will be developed using the Python programming language in conjunction with the procedural design philosophy.

## Stakeholders Interviews

Stakeholder interviews have uncovered the following project requirements going forward:

- They need to be able to pre-format the data in whatever way they like, so long as either the data's key appears consistently (i.e. all the keys are found in the same column or all in the same row)
- If providing the data in separate csvs they will at least provide one linking piece of data, i.e. the employee's ppsn
- If providing employee hours worked we will also need to know their contract type (i.e. whether the employee is paid per hour, per day, per week, per month or per annum)
- This can be provided in separate csvs or together in the one csv, as the department wishes.
- The program will be able to calculate the employee's tax band based off their contracted salary or by calculating their gross pay.
- The program should be able exclude bonuses and gift cards from taxable income.

## Program Requirements

### Functional Requirements

- Read timetable, rate, bonuses, gift card data, PPSN ~~(etc.)~~ from CSV (regardless of how data keys are stored)
- Calculate salary
- Calculate taxes and subtract them from salary
- Add bonuses and gift card amount and add to pay after taxes
- Pivot table with all the calculated data
- Payslip for every worker

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

```python
CURRENT_DIRECTORY = os.path.dirname(__file__)
INPUT_PPSN_CSV_FILENAME = os,path.join(CURRENT_DIRECTORY, 'Input', 'PPSN.csv')
INPUT_RATE_CSV_FILENAME = os,path.join(CURRENT_DIRECTORY, 'Input', 'rate.csv')
INPUT_BONUSES_CSV_FILENAME = os,path.join(CURRENT_DIRECTORY, 'Input', 'bonuses.csv')
INPUT_BENEFITS_CSV_FILENAME = os,path.join(CURRENT_DIRECTORY, 'Input', 'benefits.csv')
INPUT_HOURS_CSV_FILENAME = os,path.join(CURRENT_DIRECTORY, 'Input', 'hours.csv')
# etc.

with open(INPUT_PPSN_CSV_FILENAME, encoding='utf-8') as f:
  reader = csv.DictReader(f)
  for row in reader:
    ppsn = row['PPSN']
    name = row['Name']
    person_dict = salary_dict.get(row['PPSN'], {}) # Tries to get dict associated with this PPSN. Otherwise returns an empty dictionary
    person_dict['Name'] = name
    salary_dict[ppsn] = person_dict

# Make this into a function that can scan every csv

def read_csv(filename, dict_to_update, field_name):
  """
  Function to read data from csv file of any type:
  """
  with open(INPUT_PPSN_CSV_FILENAME, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
      ppsn = row['PPSN']
      filed_name = row[field_name]
      person_dict = dict_to_update.get(row['PPSN'], {}) # Tries to get dict associated with this PPSN. Otherwise returns an empty dictionary
      dict_to_update[field_name] = name
      dict_to_update[ppsn] = person_dict
```
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

The approach to testing this application will be multifaceted but primarily focus on the concept of unit test, where ~~(every function what?)~~.
