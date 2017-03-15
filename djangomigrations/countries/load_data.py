csv_filepathname="/Users/nadiamounzih/TIY/Week_4/django-search-engine/djangomigrations/countries/countries.csv"

django_project_home = '/Users/nadiamounzih/TIY/Week_4/django-search-engine/djangomigrations/'

import sys, os
sys.path.append(django_project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from countries.models import countries

import csv
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='""')

for row in dataReader:
    countries = Countries()
    countries.name = row[0]
    countries.capital = row[1]
    countries.population = row[2]
    countries.aggregate = row[3]
    countries.status = row[4]
    countries.language = row[5]
    countries.export = row[6]
