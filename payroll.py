"""
App to process payrol information from multiple CSV files
and print detailed information per each employee to an Excel workbook.

Author: Luke Maycock

Date: 30/01/2026
"""

import os
import csv
import pprint
from datetime import date
import openpyxl

CURRENT_DIRECTORY = os.path.dirname(__file__)
INPUT_NAMES_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Inputs', 'names.csv')
INPUT_RATES_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Inputs', 'rates.csv')
INPUT_BONUSES_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Inputs', 'bonuses.csv')
INPUT_BENEFITS_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Inputs', 'bik.csv')
INPUT_HOURS_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Inputs', 'hours.csv')

OUTPUT_FILE_NAME = os.path.join(CURRENT_DIRECTORY, 'Outputs', 'output.csv')

TEMPLATE_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Templates', 'Payslip_template.xlsx')
OUTPUT_FOLDERNAME = os.path.join(CURRENT_DIRECTORY, 'Outputs', 'Payslips')


# Functions
def calculate_salary(record):
    """
    Calculate the salary for a given record.
    """
    hours = record.get('Hours', 0)
    rate = record.get('Hourly Rate', 0)
    salary = hours * rate
    record['salary'] = salary

def calculate_tax(record):
    """
    Calculate the tax for a given record.
    """
    salary_bonus = record.get('salary', 0) + record.get('Bonus', 0) + record.get('Benefit In Kind', 0)
    record['grosspay'] = salary_bonus
    if salary_bonus <= 44000:
        tax = salary_bonus * 0.2
    else:
        tax = (44000 * 0.2) + ((salary_bonus - 44000) * 0.4)
    record['tax'] = round(tax, 2)

def read_csv(filename, dict_to_update, field_name, function_to_process=None):
    """
    Function to read data from csv file of any type:
    """
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ppsn = row['PPSN']
            field = row[field_name]
            person_dict = dict_to_update.get(row['PPSN'], {})
            person_dict[field_name] = field
            if function_to_process:
                person_dict[field_name] = function_to_process(person_dict[field_name])
            dict_to_update[ppsn] = person_dict
            # Add PPSN and current date to each person's dictionary
            dict_to_update[ppsn]['ppsn'] = ppsn
            dict_to_update[ppsn]['currentdate'] = date.today().strftime("%d/%m/%Y")

def fill_payslip_template(template_filename, output_filename, person_dict):
    """
    Function to fill in the payslip template for a given person.
    """
    template = openpyxl.load_workbook(template_filename)
    sheet = template.active

    for row in sheet.iter_rows():
        for cell in row:
            if cell.value and cell.value[0] == '<' and cell.value[-1] == '>':
                key = cell.value[1:-1]
                value = person_dict.get(key)
                if value:
                    cell.value = value

    template.save(output_filename)

salary_dict = {}

read_csv(INPUT_NAMES_CSV_FILENAME, salary_dict, 'Name')
read_csv(INPUT_HOURS_CSV_FILENAME, salary_dict, 'Hours', float)
read_csv(INPUT_RATES_CSV_FILENAME, salary_dict, 'Hourly Rate', float)
read_csv(INPUT_BONUSES_CSV_FILENAME, salary_dict, 'Bonus', float)
read_csv(INPUT_BENEFITS_CSV_FILENAME, salary_dict, 'Benefit In Kind', float)

# Debug the read_csv function
# pprint.pprint(salary_dict)

# Calculate Salary
for ppsn, record in salary_dict.items():
    calculate_salary(record)

# Calculate Tax
for ppsn, record in salary_dict.items():
    calculate_tax(record)

# Calculate Netpay
for ppsn, record in salary_dict.items():
    record['netpay'] = round(record.get('salary', 0) + record.get('Bonus', 0) + record.get('Benefit In Kind', 0) - record.get('tax', 0), 2)

# Debug the Salary, Tax and Netpay calculations
# pprint.pprint(salary_dict)

# Export data to csv 
keys = list(salary_dict.values())[0].keys()

with open(OUTPUT_FILE_NAME, "w", encoding='utf-8') as my_file:
    writer = csv.DictWriter(my_file, keys)
    writer.writeheader()
    writer.writerows(salary_dict.values())

# Generate a payslip per employee
for ppsn, record in salary_dict.items():
    output_filename = os.path.join(OUTPUT_FOLDERNAME, f'{record["Name"]}.xlsx')
    fill_payslip_template(TEMPLATE_FILENAME, output_filename, record)