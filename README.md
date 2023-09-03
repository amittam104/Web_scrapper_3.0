# Job Listing Web Scraper

A Python script that scrapes job listings from a job search website and updates the data in a Google Sheets spreadsheet.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

This project is a web scraper that extracts job listings for a specific keyword and location from the TimesJobs website. It then stores the job data in a Google Sheets spreadsheet for further analysis or tracking.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system.
- Necessary Python libraries (requests, BeautifulSoup, gspread, oauth2client) installed. You can install them using pip:
- A Google Sheets API key file (`jobs.json`) with appropriate permissions to access the Google Sheets you want to update.

## Getting Started

1. Clone this repository to your local machine:
2. Install the required Python libraries as mentioned in the Prerequisites section.
3. Replace `jobs.json` with your Google Sheets API key file.

## Usage

1. Run the script using the command.
2. Enter any unfamiliar skill when prompted.
3. The script will start scraping job listings from the TimesJobs website, and for each job that matches your criteria, it will display details and update the Google Sheets spreadsheet.
4. The script will continue to run, waiting for a day between iterations, and scrape more job listings.

## Configuration

You can customize the script by modifying the following parameters:

- Change the job search URL in the `requests.get` method to target a different job search.
- Adjust the sleep duration in the `time.sleep` method to control how long the script waits between updates.
