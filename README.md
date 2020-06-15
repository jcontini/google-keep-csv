# Google Keep Scraper
Apparently there's no simple way to export your notes from Google Keep to CSV. This script accepts the Keep folder Google Takeout archive, and outputs all of the Keep notes as lines in a single CSV file.

*Update 2020.06.15*: It seems that Google Keep now exports JSON files as well in the export. This may be easier to parse, but this script will still parse the HTML files instead.

## Install
1. Clone or download this repository
1. Open a terminal to the repository folder (`google-keep-scraper`)
1. Run `pipenv install` to install dependencies

## Import Keep Archive
First we need to download all the Keep files through Google Takeout.
1. Go to [Google Takeout](https://takeout.google.com/settings/takeout)
1. Make sure the 'Keep' checkbox is selected (you can deselect all others)
1. When archive is ready, download and unzip it.
1. Open the `Takeout` folder, and move the `Keep` folder into this repo folder so it's alongside `keep.py`

## Run
1. Run `pipenv shell` to ensure dependencies are loaded
1. Run `python keep.py`
1. All of your Keep notes should be exported to CSV in the same folder

## Troubleshooting
If you get an error about a missing dependency, be sure to run `pipenv install` prior to running the script so that it can download the dependencies needed.