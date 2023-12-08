import csv

with open('playlist.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        title = row['Название']
        print(title)
