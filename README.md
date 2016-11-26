# Google Keep Scraper
Apparently there's no simple way to export your notes from Google Keep to a CSV or spreadsheet. This does that from a Google Takeout archive. Instructions:

1. Go to [Google Takeout](https://takeout.google.com/settings/takeout)
2. Make sure the 'Keep' checkbox is selected (you can deselect all others)
3. Download and export the archive to a folder that has the 'Keep' folder
4. Run ``python keep-scrape.py``. That should export your notes to a CSV.

**Requires**:
- [Beautiful Soup 4](https://pypi.python.org/pypi/beautifulsoup4)
- [DateUtils](https://pypi.python.org/pypi/dateutils)
- [UnicodeCSV](https://pypi.python.org/pypi/unicodecsv)

You can install these requirements with `pip install -r requirements.txt`.