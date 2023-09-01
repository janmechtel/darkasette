# darkasette
A [datasette](https://datasette.io/) exploration of the [Hunchly Dark Web Reports](https://www.hunch.ly/darkweb-osint/)

WARNING! Like Hunchly, this project is not analyzing the hidden services for content. The hidden service addresses you receive could contain links to drug markets, child pornography, malware or more benign things like pictures of cats. Use your own discretion, and your common sense.

If you do discover child pornography please report it to the National Center for Exploited and Missing Children by clicking [here](http://www.missingkids.com/).

# How to reproduce
1. Clone this repo
1. Sign up for the [Hunchly Dark Web Reports](https://www.hunch.ly/darkweb-osint/)
1. You'll receive a dropbox link to download the reports
1. Put report files (.xlsx) into the folder `rawreports/` 
    1. Either download individual reports - or -
    1. Click "Download Archive" and extract all files from the .zip file 
1. Run all cells in the `import.ipynb` notebook
1. Run `datasette serve darkasette.db --metadata metadata.yaml` to start the server
1. Browse to the server at for example at http://127.0.0.1:8001/


# Requirements
- `pip install datasette, sqlite3, pandas, openpyxl, sqlite-utils`
- `datasette install datasette-dashboards`