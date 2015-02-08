import csv

def MultiFamilyCSVload():
    multi_family_db_data = []    
    with open('data/MULTIFAMILY_PROPERTIES.csv') as csvfile:    
        for row in csv.DictReader(csvfile):
            multi_family_db_data.append(row)

