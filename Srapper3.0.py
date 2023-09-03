from bs4 import BeautifulSoup
import requests
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials


Credentials = ServiceAccountCredentials.from_json_keyfile_name(r'C:\Users\INDIA\OneDrive\Documents\Python\Automation\Web Scrapper 3.0\venv\jobs.json')
file = gspread.authorize(credentials=Credentials)

sheet = file.open('Jobs listings')

sheet = sheet.sheet1



def find_jobs():
    unfamiliar_skill = input('Enter any unfamiliar skill: ')
    website = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Front+End+Developer&txtLocation=').text
    soup = BeautifulSoup(website, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

    for job in jobs:
        posted_date = job.find('span', class_ = 'sim-posted').span.text
        if 'few' in posted_date:
            Company = job.find('h3', class_ = 'joblist-comp-name').text.replace('  ', '')
            Skills = job.find('span', class_ = 'srp-skills').text.replace('  ', '')
            Details = job.find('ul', class_ = 'top-jd-dtl clearfix').text
            more_info = job.find('h2').a['href']
            
            if unfamiliar_skill not in Skills:
                print(f"Company name: {Company.strip()}")
                print(f"Skills: {Skills.strip()}")
                print(f"Details: {Details.strip()}")
                print(f'More info: {more_info}')

                print('')

                for i in range(1, 2000):
                    sheet.update_acell('A'+str(i+1), Company)
                    sheet.update_acell('B'+str(i+1), Skills)
                    sheet.update_acell('C'+str(i+1), Details)
                    sheet.update_acell('D'+str(i+1), more_info)

                    time.sleep(5)

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 1
        print(f"Waiting to load for {time_wait} day")
        time.sleep(time_wait * 86400)