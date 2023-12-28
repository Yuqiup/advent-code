#!/usr/bin/env python3

import requests
import sys
from bs4 import BeautifulSoup

url = "https://adventofcode.com/2023/day/9/input"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
data = soup.find_all("tag_name", class_="class_name")  # Adapt tag and class accordingly
