# Monthly Analytics Generator
This generates the HTML for the monthly analytics found at https://open.canada.ca/en/content/open-government-analytics

## Instructions:

1) Download this repo https://github.com/open-data/monthly-analytics-generator/archive/master.zip and unzip it. ___OR___ clone the repository: `git clone https://github.com/open-data/monthly-analytics-generator.git`
2) run `pip install requests`
3) run `pip install pyyaml` 

4) run `pip install python-dateutil`

5) run `py create_html_analytics.py`

6) Copy all HTML from the final **two** `.txt` files generated and paste this in the Drupal `source` section of the editing admin on https://open.canada.ca/en/content/open-government-analytics. Each file contains one language, so paste the HTML from the file ending in `en` on the English page, and the HTML from the file ending in `fr` on the French page.

7) Submit these as **drafts** first to ensure everything looks correct. Once confirmed, save the pages as newly published content.
