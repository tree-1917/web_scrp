# Web Scriping
import requests
import lxml
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# You Have 15 Job In This Page
job_title = []
company_name = []
location_name = []
skills = []
job_links = []
salary = []
sub_domin_name = 'https://wuzzuf.net'
#  Use Requests to fetch the rul
result = requests.get('https://wuzzuf.net/search/jobs/?q=python&a=navbg')

# save page content/markup
src = result.content

# create soup object to parse content
soup = BeautifulSoup(src, 'lxml')

# find The elements contains info we need
# [job Titles , job skills , company name , location]
job_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_titles = soup.find_all("a", {"class": "css-17s97q8"})
locations_names = soup.find_all("span", {"class": "css-5wys0k"})
job_skills = soup.find_all("div", {"class": "css-y4udm8"})

# Loop Over Returned lists to extract needed info into other list

for i in range(len(job_titles)):
    job_title.append(job_titles[i].text)
    company_name.append(company_titles[i].text)
    location_name.append(locations_names[i].text)
    skills.append(job_skills[i].text)
    job_links.append(sub_domin_name + job_titles[i].find("a").attrs["href"])

for link in job_links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    salaries = soup.find("h1", {"class":"css-f9uh36"})
    print(salaries)
    salary.append(salaries)


# Create Csv File To Store This file
# Zip_longest is So Cool To Make Match Between Tow list

file_list = [job_title, company_name, location_name, skills, job_links, salary]
exported = zip_longest(*file_list)
with open('./job.csv', 'w') as jobs:
    wr = csv.writer(jobs)
    wr.writerow(['job Title', 'company Name', 'location Name', 'skills', 'links', 'Salary'])
    wr.writerows(exported)
