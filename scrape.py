import csv
import os
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def append_to_csv(filename, data, time):
    file_exists = os.path.isfile(filename)
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(['name', 'placement', 'wins', 'losses', 'time'])
        for row in data:
            row.append(time)
            writer.writerow(row)


time_now = time.strftime("%d-%m-%Y", time.localtime(time.time()))

URL = "https://lolesports.com/standings/lec/lec_spring_2024/regular_season"
chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)
time.sleep(1)
element = driver.find_element(By.TAG_NAME, "main").get_attribute('innerHTML')
driver.quit()

soup = BeautifulSoup(element, "html.parser")
records = []
group = soup.find(class_="group")
group_rows = group.find_all(class_="ranking")
for row in group_rows:
    record = row.find(class_="record").get_text()
    placement = int(row.find(class_="ordinal").get_text())
    name = row.find(class_="name").get_text()
    score = record.split("-")
    wins = int(score[0][:-1])
    losses = int(score[1][:-1])
    records.append([name, placement, wins, losses])

append_to_csv("data.csv", records, time_now)
