"""
App to process payrol information from multiple CSV files
and print detailed information per each employee.
"""

import os
import csv
import pprint

CURRENT_DIRECTORY = os.path.dirname(__file__)
INPUT_PPSN_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'PPSN.csv')
INPUT_RATE_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'rate.csv')
INPUT_BONUSES_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'bonuses.csv')
INPUT_BENEFITS_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'benefits.csv')
INPUT_HOURS_CSV_FILENAME = os.path.join(CURRENT_DIRECTORY, 'Input', 'hours.csv')
# etc.

# with open(INPUT_PPSN_CSV_FILENAME, encoding='utf-8') as f:
#   reader = csv.DictReader(f)
#   for row in reader:
#     ppsn = row['PPSN']
#     name = row['Name']
#     person_dict = salary_dict.get(row['PPSN'], {})
# ^ Tries to get dict associated with this PPSN. Otherwise returns an empty dictionary ^
#     person_dict['Name'] = name
#     salary_dict[ppsn] = person_dict

# Make a function to calculate tax

def calculate_tax(record):
    """
    Calculate the tax for a given record.
    """
    salary_bonus = record.get('salary', 0) + record.get('bonus', 0)
    if salary_bonus <= 44000:
        tax = salary_bonus * 0.2
    else:
        tax = (44000 * 0.2) + ((salary_bonus - 44000) * 0.4)
    record['tax'] = tax

# Make this into a function that can scan every csv

def read_csv(filename, dict_to_update, field_name, function_to_process=None):
    """
    Function to read data from csv file of any type:
    """
    with open(filename, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # currently optional function to parse csv for alternative structures:
            # if isinstance(row[1], float):
            ppsn = row['PPSN']
            field = row[field_name]
            person_dict = dict_to_update.get(row['PPSN'], {})
            # ^ Tries to get dict associated with this PPSN. Otherwise returns an empty dictionary
            person_dict[field_name] = field
            if function_to_process:
                person_dict[field_name] = function_to_process(person_dict[field_name])
            dict_to_update[ppsn] = person_dict

salary_dict = {}

read_csv(INPUT_PPSN_CSV_FILENAME, salary_dict, 'name')
read_csv(INPUT_HOURS_CSV_FILENAME, salary_dict, 'hours', float)
read_csv(INPUT_RATE_CSV_FILENAME, salary_dict, 'rate', float)
read_csv(INPUT_BONUSES_CSV_FILENAME, salary_dict, 'bonuses', float)
read_csv(INPUT_BENEFITS_CSV_FILENAME, salary_dict, 'benefits', float)

print(salary_dict)



# Calculate Tax
for ppsn, record in salary_dict.items():
    record['salary'] = record.get('hours', 0) * record.get('rate', 0)

for ppsn, record in salary_dict.items():
    calculate_tax(record)


# Netpay

pprint.pprint(salary_dict)
