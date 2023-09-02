from bs4 import BeautifulSoup
import requests


website = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Front+End+Developer&txtLocation=').text

soup = BeautifulSoup(website, 'lxml')
job = soup.find('li', class_ = 'clearfix job-bx wht-shd-bx')
Company = job.find('h3', class_ = 'joblist-comp-name').text.replace('  ', '')
Skills = job.find('span', class_ = 'srp-skills').text.replace('  ', '')
Details = job.find('ul', class_ = 'top-jd-dtl clearfix').text
print(Company)
print(Skills)
print(Details)