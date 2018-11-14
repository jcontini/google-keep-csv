# Google Keep Scraper
Apparently there's no simple way to export your notes from Google Keep to CSV. This script accepts the Keep folder Google Takeout archive, and outputs all of the Keep notes as lines in a single CSV file.

## Install
1. Clone or download this repository
1. Open a terminal to the repository folder (`google-keep-scraper`)
1. Run `pip install -r requirements.txt` to install dependencies

## Run
First we need to download all the Keep files through Google Takeout.
1. Go to [Google Takeout](https://takeout.google.com/settings/takeout)
1. Make sure the 'Keep' checkbox is selected (you can deselect all others)
1. Download and export the archive to a folder that has the 'Keep' folder
1. Move the `Keep` folder into this folder, so it's alongside `keep-scrape.py`
1. Run `python keep-scrape.py`
1. All of your Keep notes should be exported to CSV in the same folder

## Troubleshooting
If you get an error about a missing dependency, be sure to run `pip install -r requirements.txt` prior to running the script so that it can download the dependencies needed.