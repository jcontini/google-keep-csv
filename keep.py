#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, bs4, glob, csv
from dateutil.parser import parse
from datetime import datetime

files = glob.glob("Keep/*.html")
notes = []

# Prep CSV file
now = datetime.now()
csvout = "notes_%s.csv" % now.strftime("%Y-%m-%d_%H%M")

with open(csvout, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["file", "date", "title", "content"])

    for file in files:
        print(file)
        with open(file, mode="r") as page:
            soup = bs4.BeautifulSoup(page.read(), "html.parser")

        # Make Excel-Friendly date
        googDate = soup.select(".heading")[0].getText().strip()
        xlDate = datetime.strftime(parse(googDate), "%m/%d/%Y %H:%M")

        # Get title
        if len(soup.select(".title")) == 0:
            title = ""
        else:
            title = soup.select(".title")[0].getText()

        # Parse Content
        html = soup.select(".content")[0]
        # Convert linebreaks
        for br in soup.find_all("br"):
            br.replace_with("\n")
        content = html.getText()

        note = {"date": xlDate, "title": title, "content": content}
        writer.writerow([file, note["date"], note["title"], note["content"]])

print("\n" + "-" * 50 + "\nDone! %s notes saved to %s\n" % (len(files), csvout))
