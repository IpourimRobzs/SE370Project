
"""
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.schooldigger.com/go/NC/city/Fayetteville/search.aspx'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'id': 'tabSchooList'})
if not table:
    print('Error: Could not find table on page')
    exit()

rows = table.find_all('tr')

# Open CSV file for writing
with open('schools.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Write headers
    headers = ['Name', 'Type', 'Grade', 'District', 'Enrollment', 'Student/Teacher Ratio', 'Free/Discounted Lunch Receipts', 'SchoolDigger Rating']
    writer.writerow(headers)

    # Write data rows
    for row in rows[1:]:  # Skip first row as it contains headers
        cells = row.find_all('td')
        if cells:
            school_name = cells[0].find('a').text.strip()
            school_type = cells[1].text.strip()
            grades = cells[2].text.strip()
            district = cells[3].text.strip()
            enrollment = cells[4].text.strip()
            ratio = cells[5].text.strip()
            lunch = cells[6].text.strip()
            rating = cells[7].text.strip()
            writer.writerow([school_name, school_type, grades, district, enrollment, ratio, lunch, rating])

print('Data written to schools.csv')



"""
import requests
import csv
from bs4 import BeautifulSoup

url = 'https://www.schooldigger.com/go/NC/city/Fayetteville/search.aspx'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find('table', {'id': 'tabSchooList'})
if not table:
    print('Error: Could not find table on page')
    exit()

rows = table.find_all('tr')

# Open CSV file for writing
with open('schools.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)

    # Write headers
    headers = ['Name', 'Type', 'Grade', 'Address', 'City', 'Zipcode', 'County', 'School District']
    writer.writerow(headers)

    # Write data rows
    for row in rows[1:]:  # Skip first row as it contains headers
        cells = row.find_all('td')
        if cells:
            school_name = cells[0].find('a').text.strip()
            school_type = cells[1].text.strip()
            grade = cells[2].text.strip()
            address = cells[3].text.strip()
            city = cells[4].text.strip()
            zipcode = cells[5].text.strip()
            county = cells[6].text.strip()
            school_district = cells[7].text.strip()
            writer.writerow([school_name, school_type, f'"{grade}"', address, city, zipcode, county, school_district])

print('Data written to schools.csv')

